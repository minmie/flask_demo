"""创建多对多

Revision ID: fc7cfcbd17b4
Revises: acaa241af327
Create Date: 2021-04-02 08:26:26.712846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc7cfcbd17b4'
down_revision = 'acaa241af327'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_author_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['tbl_author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['tbl_book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_author_book')
    # ### end Alembic commands ###
