"""empty message

Revision ID: edc7854b35f0
Revises: 
Create Date: 2020-07-23 16:14:11.416019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edc7854b35f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_signup', sa.Column('content', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('email_signup', 'content')
    # ### end Alembic commands ###
