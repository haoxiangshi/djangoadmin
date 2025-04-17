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

import os

from config.env import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE, \
    FLASK_SECRET_KEY, FLASK_UPLOAD_DIR, DB_DEBUG


# 应用全局配置
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = FLASK_SECRET_KEY
    WTF_CSRF_CHECK_DEFAULT = False
    # 全局禁用CSRF
    WTF_CSRF_ENABLED = False
    DATABASE_URL = 'sqlite://:memory:'
    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件夹路径
    STATIC_DIR = os.path.join(BASE_DIR, '../static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, '../templates')
    # 文件上传目录
    FLASK_UPLOAD_DIR = FLASK_UPLOAD_DIR
    pass


# 生产环境配置
class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    ENV = "production"
    pass


# 开发环境配置
class DevelopmentConfig(Config):
    # 打开调试模式
    DEBUG = DB_DEBUG
    ENV = "development"
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_demo'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT,
                                                                      DB_DATABASE)
    # 是否追踪数据库修改，一般不开启, 会影响性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否显示底层执行的SQL语句,打开调试模式
    SQLALCHEMY_ECHO = True
    SECRET_KEY = FLASK_SECRET_KEY
    pass


# 测试环境配置
class TestingConfig(Config):
    TESTING = True
    pass


if __name__ == '__main__':
    print(Config.FLASK_UPLOAD_DIR)
