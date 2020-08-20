"""empty message

Revision ID: 86f18baa1812
Revises: 594dbf8a8b2a
Create Date: 2020-08-16 15:42:23.548753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86f18baa1812'
down_revision = '594dbf8a8b2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpool', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('carpool', 'date')
    # ### end Alembic commands ###