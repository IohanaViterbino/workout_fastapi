"""alterando coluna de id

Revision ID: 1692df96a830
Revises: 88a64aa830f5
Create Date: 2024-05-31 22:27:00.601265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1692df96a830'
down_revision: Union[str, None] = '88a64aa830f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('atletas', 'id',
               existing_type=sa.BINARY(length=16),
               type_=sa.CHAR(length=36),
               existing_nullable=False)
    op.alter_column('categorias', 'id',
               existing_type=sa.BINARY(length=16),
               type_=sa.CHAR(length=36),
               existing_nullable=False)
    op.alter_column('centros_treinamento', 'id',
               existing_type=sa.BINARY(length=16),
               type_=sa.CHAR(length=36),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('centros_treinamento', 'id',
               existing_type=sa.CHAR(length=36),
               type_=sa.BINARY(length=16),
               existing_nullable=False)
    op.alter_column('categorias', 'id',
               existing_type=sa.CHAR(length=36),
               type_=sa.BINARY(length=16),
               existing_nullable=False)
    op.alter_column('atletas', 'id',
               existing_type=sa.CHAR(length=36),
               type_=sa.BINARY(length=16),
               existing_nullable=False)
    # ### end Alembic commands ###
