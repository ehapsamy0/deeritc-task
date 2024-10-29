"""Add Book Model And Booking Model

Revision ID: 6fa9297bc118
Revises: c7722ab3bf40
Create Date: 2024-10-28 23:54:00.445722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fa9297bc118'
down_revision = 'c7722ab3bf40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'books', 'users', ['author_id'], ['id'])
    op.drop_column('books', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'author_id')
    # ### end Alembic commands ###
