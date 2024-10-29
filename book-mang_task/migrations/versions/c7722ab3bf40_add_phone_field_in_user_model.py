"""Add Phone field in user model

Revision ID: c7722ab3bf40
Revises: 
Create Date: 2024-10-28 23:32:02.639055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7722ab3bf40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('departments')
    op.add_column('users', sa.Column('phone', sa.String(length=20), nullable=True))
    op.create_unique_constraint(None, 'users', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'phone')
    op.create_table('departments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='departments_pkey'),
    sa.UniqueConstraint('name', name='departments_name_key')
    )
    # ### end Alembic commands ###
