"""empty message

Revision ID: 6dd5306146fe
Revises: 9a90544a09f5
Create Date: 2019-05-17 22:11:24.407875

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6dd5306146fe'
down_revision = '9a90544a09f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('permissions', sa.Integer(), nullable=True))
    op.alter_column('cms_role', 'desc',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.drop_column('cms_role', 'permission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('permission', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.alter_column('cms_role', 'desc',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.drop_column('cms_role', 'permissions')
    # ### end Alembic commands ###