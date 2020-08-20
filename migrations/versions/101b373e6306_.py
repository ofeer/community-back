"""empty message

Revision ID: 101b373e6306
Revises: 13e0b0c6dbc0
Create Date: 2020-08-16 15:58:38.824336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '101b373e6306'
down_revision = '13e0b0c6dbc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'carpool', ['date'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'carpool', type_='unique')
    # ### end Alembic commands ###
