"""Added column date_completed

Revision ID: 334fcd49c548
Revises: 
Create Date: 2023-03-12 21:37:08.614056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '334fcd49c548'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('FaultDetails', sa.Column('date_completed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('FaultDetails', 'date_completed')
    # ### end Alembic commands ###
