# +----------------------------------------------------------------------
# | DjangoAdmin敏捷开发框架 [ 赋能开发者，助力企业发展 ]
# +----------------------------------------------------------------------
# | 版权所有 2021~2024 北京DjangoAdmin研发中心
# +----------------------------------------------------------------------
# | Licensed LGPL-3.0 DjangoAdmin并不是自由软件，未经许可禁止去掉相关版权
# +----------------------------------------------------------------------
# | 官方网站: https://www.djangoadmin.cn
# +----------------------------------------------------------------------
# | 作者: @一米阳光 团队荣誉出品
# +----------------------------------------------------------------------
# | 版权和免责声明:
# | 本团队对该软件框架产品拥有知识产权（包括但不限于商标权、专利权、著作权、商业秘密等）
# | 均受到相关法律法规的保护，任何个人、组织和单位不得在未经本团队书面授权的情况下对所授权
# | 软件框架产品本身申请相关的知识产权，禁止用于任何违法、侵害他人合法权益等恶意的行为，禁
# | 止用于任何违反我国法律法规的一切项目研发，任何个人、组织和单位用于项目研发而产生的任何
# | 意外、疏忽、合约毁坏、诽谤、版权或知识产权侵犯及其造成的损失 (包括但不限于直接、间接、
# | 附带或衍生的损失等)，本团队不承担任何法律责任，本软件框架禁止任何单位和个人、组织用于
# | 任何违法、侵害他人合法利益等恶意的行为，如有发现违规、违法的犯罪行为，本团队将无条件配
# | 合公安机关调查取证同时保留一切以法律手段起诉的权利，本软件框架只能用于公司和个人内部的
# | 法律所允许的合法合规的软件产品研发，详细声明内容请阅读《框架免责声明》附件；
# +----------------------------------------------------------------------

from flask import Blueprint

# 创建蓝图，参数依次是：蓝图名字、蓝图所在位置、URL前缀(注意：URL前缀对该蓝图下所有route都起作用)

# 系统登录
login_blue = Blueprint('login', __name__, url_prefix='/')
# 系统主页
index_blue = Blueprint('index', __name__, url_prefix='/index')
# 上传文件蓝图
upload_blue = Blueprint('upload', __name__, url_prefix='/upload')
# 职级蓝图
level_blue = Blueprint('level', __name__, url_prefix='/level')
# 岗位蓝图
position_blue = Blueprint('position', __name__, url_prefix='/position')
# 部门蓝图
dept_blue = Blueprint('dept', __name__, url_prefix='/dept')
# 角色蓝图
role_blue = Blueprint('role', __name__, url_prefix='/role')
# 角色菜单蓝图
rolemenu_blue = Blueprint('rolemenu', __name__, url_prefix='/rolemenu')
# 菜单蓝图
menu_blue = Blueprint('menu', __name__, url_prefix='/menu')
# 用户蓝图
user_blue = Blueprint('user', __name__, url_prefix='/user')
# 城市蓝图
city_blue = Blueprint('city', __name__, url_prefix='/city')
# 通知公告
notice_blue = Blueprint('notice', __name__, url_prefix='/notice')
# 站点蓝图
item_blue = Blueprint('item', __name__, url_prefix='/item')
# 栏目蓝图
itemcate_blue = Blueprint('itemcate', __name__, url_prefix='/itemcate')
# 友链蓝图
link_blue = Blueprint('link', __name__, url_prefix='/link')
# 广告位蓝图
adsort_blue = Blueprint('adsort', __name__, url_prefix='/adsort')
# 广告蓝图
ad_blue = Blueprint('ad', __name__, url_prefix='/ad')
# 会员等级蓝图
memberlevel_blue = Blueprint('memberlevel', __name__, url_prefix='/memberlevel')
# 会员蓝图
member_blue = Blueprint('member', __name__, url_prefix='/member')
# 字典蓝图
dict_blue = Blueprint('dict', __name__, url_prefix='/dict')
# 配置蓝图
dictdata_blue = Blueprint('dictdata', __name__, url_prefix='/dictdata')
# 配置蓝图
config_blue = Blueprint('config', __name__, url_prefix='/config')
# 配置项蓝图
configdata_blue = Blueprint('configdata', __name__, url_prefix='/configdata')
# 网站配置
configweb_blue = Blueprint('configweb', __name__, url_prefix='/configweb')

from .login import login_blue
from .index import index_blue
from .upload import upload_blue
from .level import level_blue
from .position import position_blue
from .dept import dept_blue
from .role import role_blue
from .role_menu import rolemenu_blue
from .menu import menu_blue
from .user import user_blue
from .city import city_blue
from .notice import notice_blue
from .item import item_blue
from .item_cate import itemcate_blue
from .link import link_blue
from .ad_sort import adsort_blue
from .ad import ad_blue
from .member_level import memberlevel_blue
from .member import member_blue
from .dicts import dict_blue
from .dicts_data import dictdata_blue
from .config import config_blue
from .config_data import configdata_blue
from .config_web import configweb_blue


# 注册蓝图
def register_blueprint(app):
    # 系统登录
    app.register_blueprint(login_blue)
    # 系统主页
    app.register_blueprint(index_blue)
    # 上传文件
    app.register_blueprint(upload_blue)
    # 职级模块
    app.register_blueprint(level_blue)
    # 岗位模块
    app.register_blueprint(position_blue)
    # 部门模块
    app.register_blueprint(dept_blue)
    # 角色模块
    app.register_blueprint(role_blue)
    # 角色菜单
    app.register_blueprint(rolemenu_blue)
    # 菜单模块
    app.register_blueprint(menu_blue)
    # 用户模块
    app.register_blueprint(user_blue)
    # 城市模块
    app.register_blueprint(city_blue)
    # 通知公告
    app.register_blueprint(notice_blue)
    # 站点模块
    app.register_blueprint(item_blue)
    # 栏目模块
    app.register_blueprint(itemcate_blue)
    # 友链模块
    app.register_blueprint(link_blue)
    # 广告位模块
    app.register_blueprint(adsort_blue)
    # 广告模块
    app.register_blueprint(ad_blue)
    # 会员等级模块
    app.register_blueprint(memberlevel_blue)
    # 会员模块
    app.register_blueprint(member_blue)
    # 字典模块
    app.register_blueprint(dict_blue)
    # 字典项模块
    app.register_blueprint(dictdata_blue)
    # 配置模块
    app.register_blueprint(config_blue)
    # 配置项模块
    app.register_blueprint(configdata_blue)
    # 网站配置
    app.register_blueprint(configweb_blue)
    return
