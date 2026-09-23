"""allow nullable dataset table name

Revision ID: f492c34f892d
Revises: 5975527672b9
Create Date: 2026-09-14 21:45:59.856667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f492c34f892d'
down_revision: Union[str, Sequence[str], None] = '5975527672b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "datasets",
        "table_name",
        existing_type=sa.String(length=255),
        nullable=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "datasets",
        "table_name",
        existing_type=sa.String(length=255),
        nullable=False,
    )
