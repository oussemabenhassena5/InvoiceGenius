"""init

Revision ID: 1c1a6f93459f
Revises: 
Create Date: 2022-11-21 12:05:43.802138

"""
import sqlalchemy as sa
import sqlmodel  # added
from alembic import op

# revision identifiers, used by Alembic.
revision = "1c1a6f93459f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ClientContact",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("client_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),  # type: ignore
        sa.Column("client_phone", sqlmodel.sql.sqltypes.AutoString(), nullable=False),  # type: ignore
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_ClientContact_client_name"), "ClientContact", ["client_name"], unique=False)
    op.create_index(op.f("ix_ClientContact_client_phone"), "ClientContact", ["client_phone"], unique=False)
    op.create_table(
        "InvoiceContact",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),  # type: ignore
        sa.Column("mobile", sqlmodel.sql.sqltypes.AutoString(), nullable=False),  # type: ignore
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_InvoiceContact_mobile"), "InvoiceContact", ["mobile"], unique=False)
    op.create_index(op.f("ix_InvoiceContact_name"), "InvoiceContact", ["name"], unique=False)
    op.create_table(
        "Invoice",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("total_price", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("invoice_contact_id", sa.Integer(), nullable=False),
        sa.Column("client_contact_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["client_contact_id"],
            ["ClientContact.id"],
        ),
        sa.ForeignKeyConstraint(
            ["invoice_contact_id"],
            ["InvoiceContact.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "InvoiceItem",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("invoice_id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(length=40), nullable=False),  # type: ignore
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("desc", sqlmodel.sql.sqltypes.AutoString(), nullable=True),  # type: ignore
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["invoice_id"],
            ["Invoice.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_InvoiceItem_name"), "InvoiceItem", ["name"], unique=False)
    op.create_table(
        "Note",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("note", sqlmodel.sql.sqltypes.AutoString(), nullable=False),  # type: ignore
        sa.Column("invoice_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["invoice_id"],
            ["Invoice.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_Note_note"), "Note", ["note"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_Note_note"), table_name="Note")
    op.drop_table("Note")
    op.drop_index(op.f("ix_InvoiceItem_name"), table_name="InvoiceItem")
    op.drop_table("InvoiceItem")
    op.drop_table("Invoice")
    op.drop_index(op.f("ix_InvoiceContact_name"), table_name="InvoiceContact")
    op.drop_index(op.f("ix_InvoiceContact_mobile"), table_name="InvoiceContact")
    op.drop_table("InvoiceContact")
    op.drop_index(op.f("ix_ClientContact_client_phone"), table_name="ClientContact")
    op.drop_index(op.f("ix_ClientContact_client_name"), table_name="ClientContact")
    op.drop_table("ClientContact")
    # ### end Alembic commands ###
