"""update likes format

Revision ID: 056a4b226483
Revises: cdcccc87f2f2
Create Date: 2023-01-04 03:18:07.785866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '056a4b226483'
down_revision = 'cdcccc87f2f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('card_id', sa.Integer(), autoincrement=True, nullable=False))
    op.drop_column('card', '\u2003card_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('\u2003card_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('card', 'card_id')
    # ### end Alembic commands ###
