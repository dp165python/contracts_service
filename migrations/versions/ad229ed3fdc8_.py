"""empty message

Revision ID: ad229ed3fdc8
Revises: 
Create Date: 2019-07-19 01:46:39.606436

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ad229ed3fdc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contract',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('information', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('rule',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('rule_name', sa.String(length=250), nullable=False),
    sa.Column('contract_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('f_operand', sa.String(length=250), nullable=False),
    sa.Column('s_operand', sa.String(length=250), nullable=False),
    sa.Column('operator', sa.String(length=2), nullable=False),
    sa.Column('coefficient', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rule_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rule')
    op.drop_table('contract')
    # ### end Alembic commands ###