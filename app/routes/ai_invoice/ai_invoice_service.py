# app/routes/ai_invoice/ai_invoice_service.py
from app.core.settings import settings
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from fastapi import HTTPException
import os
from typing import Dict, Any

from app.models.ai_invoice_model import ExtractedInvoice, InvoiceDetails
from app.routes.invoice.invoice_dao import InvoiceDAO
from app.models.responses import StandardResponse


class AIInvoiceService:
    def __init__(self, config: Dict[str, str]):
        self.document_client = DocumentIntelligenceClient(
            endpoint=config["DOCUMENT_INTELLIGENCE_ENDPOINT"],
            credential=AzureKeyCredential(config["DOCUMENT_INTELLIGENCE_API_KEY"]),
        )
        self.config = config

    async def process_invoice(self, file_data: bytes) -> ExtractedInvoice:
        try:
            # Extract fields using Azure Document Intelligence
            extracted_fields = await self._extract_fields(file_data)

            # Get full text content
            text_content = await self._get_text_content(file_data)

            # Extract additional fields using LLM
            llm_analysis = await self._analyze_with_llm(text_content, extracted_fields)

            return ExtractedInvoice(**extracted_fields, **llm_analysis)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Invoice processing failed: {str(e)}")

    async def _extract_fields(self, file_data: bytes) -> dict:
        """Extract fields using Azure Document Intelligence"""
        try:
            # Updated to use the current API version
            poller = self.document_client.begin_analyze_document(
                "prebuilt-invoice",
                file_data,
            )
            result = poller.result()

            # Extract fields from result
            extracted_data = {}
            if result.documents:
                doc = result.documents[0]
                fields = doc.fields
                extracted_data = {
                    "vendor_name": fields.get("VendorName", {}).get("content") if "VendorName" in fields else None,
                    "date": fields.get("InvoiceDate", {}).get("content") if "InvoiceDate" in fields else None,
                    "total_value": fields.get("InvoiceTotal", {}).get("content") if "InvoiceTotal" in fields else None,
                    "invoice_number": fields.get("InvoiceId", {}).get("content") if "InvoiceId" in fields else None,
                }
            return extracted_data

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Field extraction failed: {str(e)}")

    async def _get_text_content(self, file_data: bytes) -> str:
        """Extract full text content from invoice"""
        try:
            poller = self.document_client.begin_analyze_document(
                "prebuilt-invoice",
                file_data,
            )
            result = poller.result()
            return result.content

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Text extraction failed: {str(e)}")

    async def _analyze_with_llm(self, text: str, extracted_fields: dict) -> dict:
        """Analyze invoice text with Azure OpenAI"""
        try:
            from app.model_hub.llm_factory import LLMFactory

            llm = LLMFactory("azure", self.config)
            completion = llm.create_completion(
                response_model=InvoiceDetails,
                messages=[
                    {"role": "system", "content": "You are an expert in analyzing invoice content."},
                    {
                        "role": "user",
                        "content": f"Analyze this invoice text and determine:\n"
                        f"1. Type of expense (Rental, Material, Site Expenses, Reimbursement, Other)\n"
                        f"2. Approval status (Approved, Denied, Not Specified)\n"
                        f"3. Job location if mentioned\n\n"
                        f"Invoice text:\n{text}\n\n"
                        f"Extracted fields:\n{extracted_fields}",
                    },
                ],
            )
            return completion.model_dump()

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"LLM analysis failed: {str(e)}")
