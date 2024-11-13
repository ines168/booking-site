"""empty message

Revision ID: 6d93a31fc5ac
Revises: 9f7730b0de7e
Create Date: 2024-11-13 10:41:52.878994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d93a31fc5ac'
down_revision = '9f7730b0de7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artists', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('phone', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artists', schema=None) as batch_op:
        batch_op.drop_column('phone')
        batch_op.drop_column('address')

    # ### end Alembic commands ###
