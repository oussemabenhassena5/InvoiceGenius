"""
Invoice Table for storing invoice price, client contact, invoice contact etc
"""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from pydantic import validator

from app.models.client_contact_model import ClientContact
from app.models.invoice_contact_model import InvoiceContact
from app.models.invoice_item_model import InvoiceItem
from app.models.note_model import Note


class InvoiceInput(SQLModel):
    total_price: float = Field(nullable=False, gt=0)  # Added validation
    client_contact_id: int = Field(foreign_key="ClientContact.id", gt=0)
    invoice_contact_id: int = Field(foreign_key="InvoiceContact.id", gt=0)

    @validator("total_price")
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("Total price must be greater than zero")
        return round(v, 2)  # Round to 2 decimal places


class InvoiceBase(InvoiceInput):
    # Make all timestamp fields Optional with default values
    created_at: Optional[datetime] = Field(default_factory=datetime.now, nullable=False)
    modified_at: Optional[datetime] = Field(default_factory=datetime.now, nullable=False)
    deleted_at: Optional[datetime] = Field(default=None, nullable=True)


class Invoice(InvoiceBase, table=True):
    __tablename__: str = "Invoice"

    id: Optional[int] = Field(default=None, primary_key=True)

    client_contact: Optional[ClientContact] = Relationship(
        back_populates="invoices",
        sa_relationship_kwargs=dict(primaryjoin="Invoice.client_contact_id==ClientContact.id"),
    )  # child

    invoice_contact: Optional[InvoiceContact] = Relationship(
        back_populates="invoices",
        sa_relationship_kwargs=dict(primaryjoin="Invoice.invoice_contact_id==InvoiceContact.id"),
    )  # child

    items: list[InvoiceItem] = Relationship(
        back_populates="invoice",
        sa_relationship_kwargs=dict(
            primaryjoin="Invoice.id==InvoiceItem.invoice_id",
        ),
    )  # parent
    notes: list[Note] = Relationship(
        back_populates="invoice", sa_relationship_kwargs=dict(primaryjoin="Invoice.id==Note.invoice_id")
    )  # parent


class InvoiceFull(InvoiceBase):
    id: int
    client_contact: Optional[ClientContact]
    invoice_contact: Optional[InvoiceContact]
    items: list[InvoiceItem]
    notes: list[Note]
