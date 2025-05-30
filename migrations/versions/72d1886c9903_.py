"""empty message

Revision ID: 72d1886c9903
Revises: 
Create Date: 2023-04-12 13:45:01.665598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d1886c9903'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flask_ad',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('title', sa.String(length=255), nullable=False, comment='广告标题'),
    sa.Column('sort_id', sa.Integer(), nullable=True, comment='广告ID'),
    sa.Column('type', sa.Integer(), nullable=True, comment='广告类型：1-图片 2-文字 3-视频 4-推荐'),
    sa.Column('cover', sa.String(length=255), nullable=False, comment='广告封面'),
    sa.Column('url', sa.String(length=255), nullable=False, comment='广告地址'),
    sa.Column('width', sa.Integer(), nullable=True, comment='广告宽度'),
    sa.Column('height', sa.Integer(), nullable=True, comment='广告高度'),
    sa.Column('start_time', sa.DateTime(), nullable=True, comment='开始时间'),
    sa.Column('end_time', sa.DateTime(), nullable=True, comment='结束时间'),
    sa.Column('click', sa.Integer(), nullable=True, comment='点击率'),
    sa.Column('status', sa.Integer(), nullable=True, comment='广告状态：1-正常 2-停用'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='广告备注'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='广告排序'),
    sa.Column('content', sa.Text(), nullable=True, comment='广告内容'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_ad_sort',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=255), nullable=False, comment='广告位名称'),
    sa.Column('item_id', sa.Integer(), nullable=True, comment='站点ID'),
    sa.Column('cate_id', sa.Integer(), nullable=True, comment='栏目ID'),
    sa.Column('loc_id', sa.Integer(), nullable=True, comment='广告位位置'),
    sa.Column('platform', sa.Integer(), nullable=True, comment='投放平台：1-PC站 2-WAP站 3-微信小程序 4-APP应用'),
    sa.Column('description', sa.String(length=255), nullable=True, comment='广告位描述'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='广告位排序'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_city',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('city_code', sa.String(length=6), nullable=False, comment='城市区号'),
    sa.Column('area_code', sa.String(length=20), nullable=False, comment='行政编码'),
    sa.Column('parent_code', sa.String(length=20), nullable=False, comment='上级行政编码'),
    sa.Column('zip_code', sa.String(length=6), nullable=False, comment='邮政编码'),
    sa.Column('level', sa.Integer(), nullable=True, comment='城市级别：1-省份 2-城市 3-县区 4-街道'),
    sa.Column('pid', sa.Integer(), nullable=True, comment='上级城市ID'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='城市名称'),
    sa.Column('short_name', sa.String(length=150), nullable=False, comment='城市简称'),
    sa.Column('full_name', sa.String(length=150), nullable=True, comment='城市全称'),
    sa.Column('pinyin', sa.String(length=150), nullable=True, comment='城市拼音'),
    sa.Column('lng', sa.String(length=150), nullable=True, comment='城市经度'),
    sa.Column('lat', sa.String(length=150), nullable=True, comment='城市纬度'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_config',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='配置名称'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='配置排序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='配置备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_config_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('title', sa.String(length=150), nullable=False, comment='配置项标题'),
    sa.Column('code', sa.String(length=150), nullable=False, comment='配置项编码'),
    sa.Column('value', sa.String(length=1000), nullable=True, comment='配置项值'),
    sa.Column('options', sa.Text(), nullable=True, comment='配置选项'),
    sa.Column('config_id', sa.Integer(), nullable=True, comment='配置ID'),
    sa.Column('type', sa.String(length=150), nullable=False, comment='配置类型'),
    sa.Column('status', sa.Integer(), nullable=True, comment='配置状态：1-正常 2-停用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='配置项顺序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='配置项备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_dept',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='部门名称'),
    sa.Column('code', sa.String(length=150), nullable=False, comment='部门编码'),
    sa.Column('type', sa.Integer(), nullable=True, comment='部门类型：1-公司 2-子公司 3-部门 4-小组'),
    sa.Column('pid', sa.Integer(), nullable=True, comment='上级部门ID'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='部门排序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_dict',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='字典名称'),
    sa.Column('code', sa.String(length=150), nullable=False, comment='字典编码'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='字典排序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='字典备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_dict_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='字典项名称'),
    sa.Column('value', sa.String(length=150), nullable=False, comment='字典项值'),
    sa.Column('dict_id', sa.Integer(), nullable=True, comment='字典ID'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='字典项顺序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='字典项备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='站点名称'),
    sa.Column('type', sa.Integer(), nullable=True, comment='站点类型：1-普通站点 2-其他站点'),
    sa.Column('url', sa.String(length=255), nullable=True, comment='站点地址'),
    sa.Column('image', sa.String(length=255), nullable=True, comment='站点图片'),
    sa.Column('status', sa.Integer(), nullable=True, comment='站点状态：1-正常 2-停用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='站点顺序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='站点备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_item_cate',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='栏目名称'),
    sa.Column('pid', sa.Integer(), nullable=True, comment='上级ID'),
    sa.Column('item_id', sa.Integer(), nullable=True, comment='站点ID'),
    sa.Column('pinyin', sa.String(length=150), nullable=False, comment='拼音(全拼)'),
    sa.Column('code', sa.String(length=150), nullable=False, comment='拼音(简拼)'),
    sa.Column('is_cover', sa.Integer(), nullable=True, comment='是否有封面：1-是 2-否'),
    sa.Column('cover', sa.String(length=255), nullable=False, comment='封面地址'),
    sa.Column('status', sa.Integer(), nullable=True, comment='栏目状态：1-正常 2-停用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='栏目排序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='栏目备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_level',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=255), nullable=False, comment='职级名称'),
    sa.Column('status', sa.Integer(), nullable=True, comment='职级状态：1-在用 2-停用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='职级排序'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_link',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=255), nullable=False, comment='友链名称'),
    sa.Column('type', sa.Integer(), nullable=True, comment='友链类型：1-友情链接 2-合作伙伴'),
    sa.Column('url', sa.String(length=255), nullable=True, comment='友链URL'),
    sa.Column('item_id', sa.Integer(), nullable=True, comment='站点ID'),
    sa.Column('cate_id', sa.Integer(), nullable=True, comment='栏目ID'),
    sa.Column('platform', sa.Integer(), nullable=True, comment='投放平台：1-PC站 2-WAP站 3-微信小程序 4-APP应用'),
    sa.Column('form', sa.Integer(), nullable=True, comment='友链形式：1-文字链接 2-图片链接'),
    sa.Column('image', sa.String(length=255), nullable=True, comment='友链图片'),
    sa.Column('status', sa.Integer(), nullable=True, comment='友链状态：1-正常 2-停用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='友链顺序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='友链备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('realname', sa.String(length=150), nullable=False, comment='用户姓名'),
    sa.Column('nickname', sa.String(length=150), nullable=False, comment='用户昵称'),
    sa.Column('gender', sa.Integer(), nullable=True, comment='性别：1-男 2-女 3-保密'),
    sa.Column('avatar', sa.String(length=255), nullable=False, comment='用户头像'),
    sa.Column('birthday', sa.DateTime(), nullable=False, comment='出生日期'),
    sa.Column('email', sa.String(length=50), nullable=False, comment='邮箱'),
    sa.Column('province_code', sa.String(length=30), nullable=False, comment='省份编码'),
    sa.Column('city_code', sa.String(length=30), nullable=False, comment='城市编码'),
    sa.Column('district_code', sa.String(length=30), nullable=False, comment='县区编码'),
    sa.Column('address_info', sa.String(length=255), nullable=True, comment='省市区信息'),
    sa.Column('address', sa.String(length=255), nullable=False, comment='详细地址'),
    sa.Column('username', sa.String(length=30), nullable=True, comment='用户名'),
    sa.Column('password', sa.String(length=255), nullable=True, comment='密码'),
    sa.Column('member_level', sa.Integer(), nullable=True, comment='会员等级'),
    sa.Column('source', sa.Integer(), nullable=True, comment='注册来源：1-网站注册 2-客户端注册 3-小程序注册 4-手机站注册 5-后台添加'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态：1-正常 2-禁用'),
    sa.Column('intro', sa.String(length=255), nullable=True, comment='个人简介'),
    sa.Column('signature', sa.String(length=255), nullable=True, comment='个人签名'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_member_level',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='等级名称'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_menu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('title', sa.String(length=150), nullable=False, comment='菜单标题'),
    sa.Column('icon', sa.String(length=50), nullable=True, comment='菜单图标'),
    sa.Column('parent_id', sa.Integer(), nullable=True, comment='上级ID'),
    sa.Column('path', sa.String(length=255), nullable=True, comment='菜单路径'),
    sa.Column('component', sa.String(length=255), nullable=True, comment='菜单组件'),
    sa.Column('target', sa.String(length=30), nullable=True, comment='打开方式：1-内部打开 2-外部打开'),
    sa.Column('permission', sa.String(length=150), nullable=True, comment='权限节点'),
    sa.Column('type', sa.Integer(), nullable=True, comment='菜单类型：0-菜单 1-节点'),
    sa.Column('status', sa.Integer(), nullable=True, comment='菜单状态：1-正常 2-停用'),
    sa.Column('hide', sa.Integer(), nullable=True, comment='是否可见：0-可见 1-不可见'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_notice',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('title', sa.String(length=255), nullable=False, comment='通知标题'),
    sa.Column('source', sa.Integer(), nullable=True, comment='通知来源：1-官方平台 2-开源中国 3-CSDN官方 4-新浪微博'),
    sa.Column('url', sa.String(length=255), nullable=True, comment='外部地址'),
    sa.Column('click', sa.Integer(), nullable=True, comment='点击率'),
    sa.Column('status', sa.Integer(), nullable=True, comment='通知状态：1-正常 2-停用'),
    sa.Column('is_top', sa.Integer(), nullable=True, comment='是否置顶：1-是 2-否'),
    sa.Column('content', sa.Text(), nullable=True, comment='通知公告内容'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=255), nullable=False, comment='岗位名称'),
    sa.Column('status', sa.Integer(), nullable=True, comment='岗位状态：1-在用 2-停用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='岗位排序'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('name', sa.String(length=150), nullable=False, comment='角色名称'),
    sa.Column('code', sa.String(length=30), nullable=False, comment='角色编码'),
    sa.Column('status', sa.Integer(), nullable=True, comment='角色状态：1-正常 2-停用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='角色排序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='角色备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_role_menu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('role_id', sa.Integer(), nullable=True, comment='角色ID'),
    sa.Column('menu_id', sa.Integer(), nullable=True, comment='菜单ID'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('realname', sa.String(length=150), nullable=False, comment='用户姓名'),
    sa.Column('nickname', sa.String(length=150), nullable=False, comment='用户昵称'),
    sa.Column('gender', sa.Integer(), nullable=True, comment='性别：1-男 2-女 3-保密'),
    sa.Column('avatar', sa.String(length=255), nullable=False, comment='用户头像'),
    sa.Column('mobile', sa.String(length=30), nullable=False, comment='手机号'),
    sa.Column('email', sa.String(length=30), nullable=False, comment='邮箱'),
    sa.Column('birthday', sa.Date(), nullable=True, comment='出生日期'),
    sa.Column('dept_id', sa.Integer(), nullable=True, comment='部门ID'),
    sa.Column('level_id', sa.Integer(), nullable=True, comment='职级ID'),
    sa.Column('position_id', sa.Integer(), nullable=True, comment='岗位ID'),
    sa.Column('province_code', sa.String(length=30), nullable=False, comment='省份编码'),
    sa.Column('city_code', sa.String(length=30), nullable=False, comment='城市编码'),
    sa.Column('district_code', sa.String(length=30), nullable=False, comment='县区编码'),
    sa.Column('address_info', sa.String(length=255), nullable=True, comment='省市区信息'),
    sa.Column('address', sa.String(length=255), nullable=False, comment='详细地址'),
    sa.Column('username', sa.String(length=30), nullable=True, comment='用户名'),
    sa.Column('password', sa.String(length=255), nullable=True, comment='密码'),
    sa.Column('salt', sa.String(length=30), nullable=True, comment='加密盐'),
    sa.Column('intro', sa.String(length=255), nullable=True, comment='个人简介'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态：1-正常 2-禁用'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('note', sa.String(length=255), nullable=True, comment='个人备注'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_user_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('create_user', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_time', sa.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_user', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_time', sa.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), nullable=True, comment='删除标识：0-正常 1-已删除'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='用户ID'),
    sa.Column('role_id', sa.Integer(), nullable=True, comment='角色ID'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flask_user_role')
    op.drop_table('flask_user')
    op.drop_table('flask_role_menu')
    op.drop_table('flask_role')
    op.drop_table('flask_position')
    op.drop_table('flask_notice')
    op.drop_table('flask_menu')
    op.drop_table('flask_member_level')
    op.drop_table('flask_member')
    op.drop_table('flask_link')
    op.drop_table('flask_level')
    op.drop_table('flask_item_cate')
    op.drop_table('flask_item')
    op.drop_table('flask_dict_data')
    op.drop_table('flask_dict')
    op.drop_table('flask_dept')
    op.drop_table('flask_config_data')
    op.drop_table('flask_config')
    op.drop_table('flask_city')
    op.drop_table('flask_ad_sort')
    op.drop_table('flask_ad')
    # ### end Alembic commands ###
