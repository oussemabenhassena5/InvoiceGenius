"""
app/models/__init__.py

from https://github.com/tiangolo/sqlmodel/issues/121#issuecomment-935656778
Import the various model modules in one place and resolve forward refs.
"""

import pkgutil
from pathlib import Path

# Update these imports to use the correct module names
from app.models.client_contact_model import ClientContact, ClientContactWithInvoices
from app.models.invoice_contact_model import InvoiceContact, InvoiceContactWithInvoices
from app.models.invoice_item_model import InvoiceItem
from app.models.invoice_model import Invoice, InvoiceFull
from app.models.note_model import Note, NoteWithInvoice

# Remove these duplicate imports as they're using incorrect paths
# from .client_contact import ClientContact
# from .invoice import InvoiceFull
# from .invoice_contact import InvoiceContact
# from .invoice_item import InvoiceItem
# from .note import Note

# Use model_rebuild() for Pydantic v2 compatibility
InvoiceFull.model_rebuild()
InvoiceContactWithInvoices.model_rebuild()
ClientContactWithInvoices.model_rebuild()
NoteWithInvoice.model_rebuild()


def load_all_models() -> None:
    """Load all models from this folder."""
    package_dir = Path(__file__).resolve().parent
    modules = pkgutil.walk_packages(
        path=[str(package_dir)],
        prefix="app.models.",
    )
    for module in modules:
        print(module.name)
        __import__(module.name)  # noqa: WPS421
