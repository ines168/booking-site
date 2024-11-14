"""empty message

Revision ID: e3924acfd215
Revises: 71eea1655488
Create Date: 2024-11-13 18:44:52.184732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3924acfd215'
down_revision = '71eea1655488'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venues', schema=None) as batch_op:
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venues', schema=None) as batch_op:
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###