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

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import NumberRange, DataRequired, Length


# 通知表单验证
class NoticeForm(FlaskForm):
    # 通知ID
    id = IntegerField(
        # 文本描述
        label='通知ID',
        # 验证规则
        validators=[
        ]
    )
    # 通知标题
    title = StringField(
        label='通知标题',
        validators=[
            DataRequired(message='通知标题不能为空'),
            Length(max=255, message='通知标题长度不得超过255个字符')
        ]
    )
    # 通知来源：1-官方平台 2-开源中国 3-CSDN官方 4-新浪微博
    source = IntegerField(
        label='通知来源',
        validators=[
            DataRequired(message='通知来源不能为空'),
            NumberRange(min=1, max=4, message='通知来源值在1~4之间')
        ]
    )
    # 通知地址
    url = StringField(
        label='通知地址',
        validators=[
            Length(max=255, message='通知地址长度不得超过255个字符')
        ]
    )
    # 通知状态：1-正常 2-停用
    status = IntegerField(
        label='通知状态',
        validators=[
            DataRequired(message='通知状态不能为空'),
            NumberRange(min=1, max=2, message='通知状态值在1~2之间')
        ]
    )
    # 是否置顶：1-是 2-否
    is_top = IntegerField(
        label='是否置顶',
        validators=[
            DataRequired(message='是否置顶不能为空'),
            NumberRange(min=1, max=2, message='是否置顶值在1~2之间')
        ]
    )
    # 点击率
    click = IntegerField(
        label='点击率',
        validators=[
            DataRequired(message='点击率不能为空'),
            NumberRange(min=0, message='点击率值不得小于0')
        ]
    )
    # 通知内容
    content = StringField(
        label='通知内容',
        validators=[
        ]
    )
