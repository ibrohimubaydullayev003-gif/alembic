"""Create products table

Revision ID: 003_create_products
Revises: 002_create_categories
"""
from alembic import op
import sqlalchemy as sa

revision = "003_create_products"
down_revision = "002_create_categories"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("category_id", sa.Integer(), sa.ForeignKey("categories.id"), nullable=False),
    )
    op.create_index("ix_products_id", "products", ["id"])


def downgrade():
    op.drop_index("ix_products_id", table_name="products")
    op.drop_table("products")
