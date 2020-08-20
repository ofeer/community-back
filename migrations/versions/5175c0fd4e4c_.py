"""empty message

Revision ID: 5175c0fd4e4c
Revises: 82ffecdd793c
Create Date: 2020-08-20 14:16:24.709895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5175c0fd4e4c'
down_revision = '82ffecdd793c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpool', sa.Column('driver_id', sa.String(length=255), nullable=True))
    op.drop_constraint('carpool_driver_name_fkey', 'carpool', type_='foreignkey')
    op.create_foreign_key(None, 'carpool', 'user', ['driver_id'], ['user_id'])
    op.drop_column('carpool', 'driver_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpool', sa.Column('driver_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'carpool', type_='foreignkey')
    op.create_foreign_key('carpool_driver_name_fkey', 'carpool', 'user', ['driver_name'], ['user_id'])
    op.drop_column('carpool', 'driver_id')
    # ### end Alembic commands ###
