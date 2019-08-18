"""empty message

Revision ID: 6c316c23ece6
Revises: c233e2171bd7
Create Date: 2019-08-18 12:07:26.779037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c316c23ece6'
down_revision = 'c233e2171bd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('confirmations', sa.Column('resume_file_name', sa.String(length=10000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('confirmations', 'resume_file_name')
    # ### end Alembic commands ###