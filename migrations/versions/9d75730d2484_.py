"""empty message

Revision ID: 9d75730d2484
Revises: 72d1886c9903
Create Date: 2023-04-12 13:46:19.874903

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9d75730d2484'
down_revision = '72d1886c9903'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flask_menu', sa.Column('title', sa.String(length=150), nullable=False, comment='菜单标题'))
    op.add_column('flask_menu', sa.Column('parent_id', sa.Integer(), nullable=True, comment='上级ID'))
    op.add_column('flask_menu', sa.Column('path', sa.String(length=255), nullable=True, comment='菜单路径'))
    op.add_column('flask_menu', sa.Column('component', sa.String(length=255), nullable=True, comment='菜单组件'))
    op.add_column('flask_menu', sa.Column('hide', sa.Integer(), nullable=True, comment='是否可见：0-可见 1-不可见'))
    op.drop_column('flask_menu', 'name')
    op.drop_column('flask_menu', 'pid')
    op.drop_column('flask_menu', 'url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flask_menu', sa.Column('url', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=255), nullable=True, comment='菜单URL'))
    op.add_column('flask_menu', sa.Column('pid', mysql.INTEGER(), autoincrement=False, nullable=True, comment='上级ID'))
    op.add_column('flask_menu', sa.Column('name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=150), nullable=False, comment='菜单名称'))
    op.drop_column('flask_menu', 'hide')
    op.drop_column('flask_menu', 'component')
    op.drop_column('flask_menu', 'path')
    op.drop_column('flask_menu', 'parent_id')
    op.drop_column('flask_menu', 'title')
    # ### end Alembic commands ###
