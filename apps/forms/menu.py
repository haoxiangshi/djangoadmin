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


# 菜单表单验证
class MenuForm(FlaskForm):
    # 菜单ID
    id = IntegerField(
        # 文本描述
        label='菜单ID',
        # 验证规则
        validators=[
        ]
    )
    # 菜单标题
    title = StringField(
        label='菜单标题',
        validators=[
            DataRequired(message='菜单标题不能为空'),
            Length(max=150, message='菜单标题长度不得超过150个字符')
        ]
    )
    # 菜单图标
    icon = StringField(
        label='菜单图标',
        validators=[
            # DataRequired(message='菜单图标不能为空'),
            Length(max=50, message='菜单图标长度不得超过50个字符')
        ]
    )
    # 路由地址
    path = StringField(
        label='路由地址',
        validators=[
            # DataRequired(message='路由地址不能为空'),
            Length(max=255, message='路由地址长度不得超过255个字符')
        ]
    )
    # 组件路径
    component = StringField(
        label='组件路径',
        validators=[
            # DataRequired(message='组件路径不能为空'),
            Length(max=255, message='组件路径长度不得超过255个字符')
        ]
    )
    # 上级ID
    parent_id = IntegerField(
        label='上级ID',
        validators=[
        ]
    )
    # 菜单类型：0-菜单 1-节点
    type = IntegerField(
        label='菜单类型',
        validators=[
            # DataRequired(message='菜单类型不能为空'),
            NumberRange(min=0, max=1, message='菜单类型值在0~1之间')
        ]
    )
    # 打开方式：1-内部打开 2-外部打开
    target = StringField(
        label='打开方式',
        validators=[
            # DataRequired(message='打开方式不能为空'),
            Length(max=30, message='打开方式长度不得超过30个字符')
        ]
    )
    # 权限节点
    permission = StringField(
        label='权限节点',
        validators=[
            Length(max=150, message='权限节点长度不得超过150个字符')
        ]
    )
    # 是否可见：0-可见 1-不可见
    hide = IntegerField(
        label='是否可见',
        validators=[
            # DataRequired(message='是否可见不能为空'),
            NumberRange(min=0, max=1, message='是否可见值在0~1之间')
        ]
    )
    # 菜单状态：1-正常 2-禁用
    status = IntegerField(
        label='菜单状态',
        validators=[
            DataRequired(message='菜单状态不能为空'),
            NumberRange(min=1, max=2, message='菜单状态值在1~2之间')
        ]
    )
    # 菜单排序
    sort = IntegerField(
        label='菜单排序',
        validators=[
            DataRequired(message='菜单排序不能为空'),
            NumberRange(min=0, max=99999, message='菜单排序值在0~99999之间')
        ]
    )
    # 菜单备注
    note = StringField(
        label='菜单备注',
        validators=[
            Length(max=255, message='菜单备注长度不得超过255个字符')
        ]
    )
    # 权限节点
    checked_list = StringField(
        label='权限节点',
        validators=[
            Length(max=500, message='权限节点长度不得超过500个字符')
        ]
    )
