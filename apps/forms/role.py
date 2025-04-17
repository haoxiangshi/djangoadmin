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
from wtforms.validators import NumberRange, DataRequired, Length, ValidationError

from apps.models.role import Role


# 角色表单验证
class RoleForm(FlaskForm):
    # 角色ID
    id = IntegerField(
        # 文本描述
        label='角色ID',
        # 验证规则
        validators=[
        ]
    )
    # 角色名称
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired(message='角色名称不能为空'),
            Length(max=150, message='角色名称长度不得超过150个字符')
        ]
    )
    # 角色编码
    code = StringField(
        label='角色编码',
        validators=[
            DataRequired(message='角色编码不能为空'),
            Length(max=30, message='角色编码长度不得超过30个字符')
        ]
    )
    # 角色状态
    status = IntegerField(
        label='角色状态',
        validators=[
            DataRequired(message='角色状态不能为空'),
            NumberRange(min=1, max=2, message='角色状态值在1~2之间')
        ]
    )
    # 角色排序
    sort = IntegerField(
        label='角色排序',
        validators=[
            DataRequired(message='角色排序不能为空'),
            NumberRange(min=0, max=99999, message='角色排序值在0~99999之间')
        ]
    )
    # 角色备注
    note = StringField(
        label='角色备注',
        validators=[
            Length(max=255, message='角色备注长度不得超过255个字符')
        ]
    )

    # 自定义验证名称不能重复
    def validate_name(self, field):
        # 查询单条数据
        if not field.data and Role.query.filter(Role.name == field.data).first():
            raise ValidationError("角色名称不能重复")


# 状态设置表单
class RoleStatusForm(FlaskForm):
    # 角色ID
    id = IntegerField(
        # 文本描述
        label='角色ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='角色ID必须大于0')
        ]
    )
    # 角色状态
    status = IntegerField(
        label='角色状态',
        validators=[
            DataRequired(message='角色状态不能为空'),
            NumberRange(min=1, max=2, message='角色状态值在1~2之间')
        ]
    )
