"""init migrations

Revision ID: bdab11e119e4
Revises: 
Create Date: 2024-01-22 10:18:46.757998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bdab11e119e4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "apilogs",
        sa.Column("rtsp_url", sa.String(length=500), nullable=False),
        sa.Column("hls_url", sa.String(length=500), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_apilogs_hls_url"), "apilogs", ["hls_url"], unique=False)
    op.create_index(op.f("ix_apilogs_rtsp_url"), "apilogs", ["rtsp_url"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_apilogs_rtsp_url"), table_name="apilogs")
    op.drop_index(op.f("ix_apilogs_hls_url"), table_name="apilogs")
    op.drop_table("apilogs")
    # ### end Alembic commands ###