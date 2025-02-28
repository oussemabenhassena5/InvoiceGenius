# app/models/ai_invoice_model.py
from pydantic import BaseModel
from typing import Optional


class InvoiceDetails(BaseModel):
    expense_type: str
    approval: str
    job_location: Optional[str] = ""


class ExtractedInvoice(BaseModel):
    vendor_name: Optional[str]
    date: Optional[str]
    total_value: Optional[str]
    invoice_number: Optional[str]
    expense_type: Optional[str]
    approval: Optional[str]
    job_location: Optional[str]
