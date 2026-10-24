"""Create categories table

Revision ID: 002_create_categories
Revises: 001_create_users
"""
from alembic import op
import sqlalchemy as sa

revision = "002_create_categories"
down_revision = "001_create_users"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False, unique=True),
        sa.Column("description", sa.String(length=255), nullable=True),
    )
    op.create_index("ix_categories_id", "categories", ["id"])


def downgrade():
    op.drop_index("ix_categories_id", table_name="categories")
    op.drop_table("categories")
