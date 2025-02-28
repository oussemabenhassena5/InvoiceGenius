# app/routes/ai_invoice/ai_invoice_view.py
from fastapi import APIRouter, File, UploadFile, Depends
from app.models.ai_invoice_model import ExtractedInvoice
from app.models.responses import StandardResponse
from .ai_invoice_service import AIInvoiceService
from app.core.settings import settings

router = APIRouter()


@router.post("/extract", response_model=StandardResponse)
async def extract_invoice(
    file: UploadFile = File(...),
    service: AIInvoiceService = Depends(
        lambda: AIInvoiceService(
            {
                "DOCUMENT_INTELLIGENCE_ENDPOINT": settings.document_intelligence.endpoint,
                "DOCUMENT_INTELLIGENCE_API_KEY": settings.document_intelligence.api_key,
                "AZURE_API_KEY": settings.azure_api_key,
                "AZURE_URL": settings.azure_url,
            }
        )
    ),
):
    content = await file.read()
    result = await service.process_invoice(content)
    return StandardResponse(success=True, message="Invoice processed successfully", data=result)
