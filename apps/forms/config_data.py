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


# 配置项表单验证
class ConfigDataForm(FlaskForm):
    # 配置项ID
    id = IntegerField(
        # 文本描述
        label='配置项ID',
        # 验证规则
        validators=[
        ]
    )
    # 配置项标题
    title = StringField(
        label='配置项标题',
        validators=[
            DataRequired(message='配置项标题不能为空'),
            Length(max=150, message='配置项标题长度不得超过150个字符')
        ]
    )
    # 配置项编码
    code = StringField(
        label='配置项编码',
        validators=[
            DataRequired(message='配置项编码不能为空'),
            Length(max=150, message='配置项编码长度不得超过150个字符')
        ]
    )
    # 配置项值
    value = StringField(
        label='配置项值',
        validators=[
            DataRequired(message='配置项值不能为空'),
            Length(max=1000, message='配置项值长度不得超过1000个字符')
        ]
    )
    # 配置选项
    options = StringField(
        label='配置选项',
        validators=[
            # DataRequired(message='配置选项不能为空'),
            Length(max=1000, message='配置选项长度不得超过1000个字符')
        ]
    )
    # 配置ID
    config_id = IntegerField(
        label='配置ID',
        validators=[
            DataRequired(message='配置ID不能为空'),
            NumberRange(min=0, message='配置ID不得小于0')
        ]
    )
    # 配置类型
    type = StringField(
        label='配置类型',
        validators=[
            DataRequired(message='配置类型不能为空'),
            Length(max=150, message='配置类型长度不得超过150个字符')
        ]
    )
    # 配置项排序
    sort = IntegerField(
        label='配置项排序',
        validators=[
            DataRequired(message='字配置项排序不能为空'),
            NumberRange(min=0, max=99999, message='配置项排序值在0~99999之间')
        ]
    )
    # 配置项备注
    note = StringField(
        label='配置项备注',
        validators=[
            Length(max=255, message='配置项备注长度不得超过255个字符')
        ]
    )


# 状态设置表单
class ConfigDataStatusForm(FlaskForm):
    # 配置项ID
    id = IntegerField(
        # 文本描述
        label='配置项ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='配置项ID必须大于0')
        ]
    )
    # 配置项状态
    status = IntegerField(
        label='配置项状态',
        validators=[
            DataRequired(message='配置项状态不能为空'),
            NumberRange(min=1, max=2, message='配置项状态值在1~2之间')
        ]
    )
