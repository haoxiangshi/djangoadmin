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

# =============================================== 基础配置 =================================================


import os

# 应用名称
import platform

FLASK_NAME = os.getenv('FLASK_NAME', 'DEMO')
# 应用版本
FLASK_VERSION = os.getenv('FLASK_VERSION', 'v1.0.0')
# 应用秘钥
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'd67beaf46fbf4f048d2eeb26fd62ea49')
# 应用运行地址
FLASK_HOST = os.getenv('FLASK_HOST', '127.0.0.1')
# 应用运行端口
FLASK_PORT = os.getenv('FLASK_PORT', 8022)
# 应用启动文件
FLASK_APP = os.getenv('FLASK_APP', 'app.py')
# 应用环境变量
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
# 是否调试模式：是-True,否-False
FLASK_DEBUG = (os.getenv('FLASK_DEBUG', 'True') == 'True')
# 是否演示模式：是-True,否-False
FLASK_DEMO = (os.getenv('FLASK_DEMO', 'True') == 'True')
# 系统环境:windows、linux
FLASK_SYSTEM = platform.system().lower()

# 应用根目录
FLASK_ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 应用模板路径
FLASK_TEMPLATE_FOLDER = os.path.join(FLASK_ROOT_PATH, '/templates')
# 应用静态资源路径
FLASK_STATIC_FOLDER = os.path.join(FLASK_ROOT_PATH, '/static')
# 应用文件存储路径
FLASK_UPLOAD_DIR = os.getenv('FLASK_UPLOAD_DIR', os.path.join(FLASK_ROOT_PATH, '/uploads'))
# 正式图片路径
FLASK_IMAGE_PATH = FLASK_UPLOAD_DIR + '/images'
# 临时文件路径
FLASK_TEMP_PATH = FLASK_UPLOAD_DIR + '/temp'
# 应用图片域名
FLASK_IMAGE_URL = os.getenv('FLASK_IMAGE_URL', '')

# =============================================== 数据库配置 =================================================

# 数据库驱动
DB_DRIVER = os.getenv('DB_DRIVER', 'mysql')
# 数据库地址
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
# 数据库端口
DB_PORT = os.getenv('DB_PORT', 3306)
# 数据库名称
DB_DATABASE = os.getenv('DB_DATABASE', 'flask_admin')
# 数据库账号
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
# 数据库密码
DB_PASSWORD = os.getenv('DB_PASSWORD', '159159159')
# 数据表前缀
DB_PREFIX = os.getenv('DB_PREFIX', 'flask_')
# 是否开启调试模式：是-True,否-False
DB_DEBUG = (os.getenv('DB_DEBUG', 'True') == 'True')

# =============================================== 缓存配置 =================================================

# 缓存服务地址
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
# 缓存服务端口
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
# 缓存服务密码
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')
# 缓存服务密码
REDIS_INDEX = os.getenv('REDIS_INDEX', 0)
# AUTH 为 True 时需要进行 用户认证
REDIS_AUTH = (os.getenv('REDIS_AUTH', 'True') == 'True')
# 是否对查询结果进行编码处理
REDIS_DECODE_RESPONSES = (os.getenv('REDIS_DECODE_RESPONSES', 'True') == 'True')

# =============================================== 邮件配置 =================================================

# 邮寄者
MAIL_MAILER = os.getenv('MAIL_MAILER', 'smtp')
# 邮件服务
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.163.com')
# 邮件端口
MAIL_PORT = os.getenv('MAIL_PORT', 465)
# 邮件SSL证书
MAIL_USE_SSL = (os.getenv('DB_DEBUG', 'True') == 'True')
# 授权邮箱用户名
MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
# 授权邮箱授权码
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
# 邮件加密串
MAIL_ENCRYPTION = os.getenv('MAIL_ENCRYPTION', '')
# 邮件发件人名称
MAIL_FROM_NAME = os.getenv('MAIL_FROM_NAME', '')
# 邮件发件人地址
MAIL_FROM_ADDRESS = os.getenv('MAIL_FROM_ADDRESS', '')
