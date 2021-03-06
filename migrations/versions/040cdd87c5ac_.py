"""empty message

Revision ID: 040cdd87c5ac
Revises: 18c6546e1139
Create Date: 2020-08-11 15:42:20.536687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040cdd87c5ac'
down_revision = '18c6546e1139'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_history', sa.Column('sum_of_rating', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_history', 'sum_of_rating')
    # ### end Alembic commands ###
