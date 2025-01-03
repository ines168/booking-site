"""empty message

Revision ID: 1a986f080702
Revises: 6d93a31fc5ac
Create Date: 2024-11-13 15:35:33.572699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a986f080702'
down_revision = '6d93a31fc5ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shows', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('venue_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('artist_id', sa.Integer(), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.create_foreign_key(None, 'venues', ['venue_id'], ['id'])
        batch_op.create_foreign_key(None, 'artists', ['artist_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shows', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_column('artist_id')
        batch_op.drop_column('venue_id')
        batch_op.drop_column('date')

    # ### end Alembic commands ###
