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
from wtforms import IntegerField, StringField, DateField, Field
from wtforms.validators import NumberRange, DataRequired, Length, ValidationError

from apps.models.user import User


# 用户表单验证
class UserForm(FlaskForm):
    # 用户ID
    id = IntegerField(
        # 文本描述
        label='用户ID',
        # 验证规则
        validators=[
        ]
    )
    # 用户姓名
    realname = StringField(
        label='用户姓名',
        validators=[
            DataRequired(message='用户姓名不能为空'),
            Length(max=150, message='用户姓名长度不得超过150个字符')
        ]
    )
    # 用户昵称
    nickname = StringField(
        label='用户昵称',
        validators=[
            DataRequired(message='用户昵称不能为空'),
            Length(max=150, message='用户昵称长度不得超过150个字符')
        ]
    )
    # 性别：1-男 2-女 3-保密
    gender = IntegerField(
        label='性别',
        validators=[
            DataRequired(message='性别不能为空'),
            NumberRange(min=1, max=3, message='性别值在1~3之间')
        ]
    )
    # 头像
    avatar = StringField(
        label='头像',
        validators=[
            DataRequired(message='头像不能为空'),
            Length(max=255, message='头像长度不得超过255个字符')
        ]
    )
    # 手机号
    mobile = StringField(
        label='手机号',
        validators=[
            DataRequired(message='手机号不能为空'),
            Length(max=30, message='手机号长度不得超过30个字符')
        ]
    )
    # 邮箱
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired(message='邮箱不能为空'),
            Length(max=30, message='邮箱长度不得超过30个字符')
        ]
    )
    # 出生日期
    birthday = DateField(
        label='出生日期',
        validators=[
            DataRequired(message='出生日期不能为空'),
        ]
    )
    # 部门ID
    dept_id = IntegerField(
        label='部门ID',
        validators=[
            DataRequired(message='部门ID不能为空'),
            NumberRange(min=0, message='部门ID不得小于0')
        ]
    )
    # 职级ID
    level_id = IntegerField(
        label='职级ID',
        validators=[
            DataRequired(message='职级ID不能为空'),
            NumberRange(min=0, message='职级ID不得小于0')
        ]
    )
    # 岗位ID
    position_id = IntegerField(
        label='岗位ID',
        validators=[
            DataRequired(message='岗位ID不能为空'),
            NumberRange(min=0, message='岗位ID不得小于0')
        ]
    )
    # 行政区划
    city = Field(
        label='行政区划',
        validators=[
            DataRequired(message='请选择行政区划'),
        ]
    )
    # 省份编码
    province_code = StringField(
        label='省份编码',
        validators=[
        ]
    )
    # 城市编码
    city_code = StringField(
        label='城市编码',
        validators=[
        ]
    )
    # 县区编码
    district_code = StringField(
        label='县区编码',
        validators=[
        ]
    )
    # 详细地址
    address = StringField(
        label='详细地址',
        validators=[
            DataRequired(message='详细地址不能为空'),
            Length(max=255, message='详细地址长度不得超过255个字符')
        ]
    )
    # 登录账号
    username = StringField(
        label='登录账号',
        validators=[
            DataRequired(message='登录账号不能为空'),
            Length(max=30, message='登录账号长度不得超过30个字符')
        ]
    )
    # 登录密码
    password = StringField(
        label='登录密码',
        validators=[
            Length(max=255, message='登录密码长度不得超过255个字符')
        ]
    )
    # 个人简介
    intro = StringField(
        label='个人简介',
        validators=[
            Length(max=255, message='个人简介长度不得超过255个字符')
        ]
    )
    # 用户状态
    status = IntegerField(
        label='用户状态',
        validators=[
            DataRequired(message='用户状态不能为空'),
            NumberRange(min=1, max=2, message='用户状态值在1~2之间')
        ]
    )
    # 用户备注
    note = StringField(
        label='用户备注',
        validators=[
            Length(max=255, message='用户备注长度不得超过255个字符')
        ]
    )
    # 用户排序
    sort = IntegerField(
        label='用户排序',
        validators=[
            DataRequired(message='用户排序不能为空'),
            NumberRange(min=0, max=99999, message='用户排序值在0~99999之间')
        ]
    )
    # 用户角色
    roles = Field(
        label='用户角色',
        validators=[
        ]
    )

    # 登录账号自定义重复性验证
    def validate_username(self, field):
        # 查询单条数据
        if not field.data and User.query.filter(User.username == field.data).first():
            raise ValidationError("登录账号不能重复")


# 状态设置表单
class UserStatusForm(FlaskForm):
    # 用户ID
    id = IntegerField(
        # 文本描述
        label='用户ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='用户ID必须大于0')
        ]
    )
    # 用户状态
    status = IntegerField(
        label='用户状态',
        validators=[
            DataRequired(message='用户状态不能为空'),
            NumberRange(min=1, max=2, message='用户状态值在1~2之间')
        ]
    )


# 修改个人信息表单验证
class UserInfoForm(FlaskForm):
    # 用户姓名
    realname = StringField(
        label='用户姓名',
        validators=[
            DataRequired(message='用户姓名不能为空'),
            Length(max=150, message='用户姓名长度不得超过150个字符')
        ]
    )
    # 用户昵称
    nickname = StringField(
        label='用户昵称',
        validators=[
            DataRequired(message='用户昵称不能为空'),
            Length(max=150, message='用户昵称长度不得超过150个字符')
        ]
    )
    # 性别：1-男 2-女 3-保密
    gender = IntegerField(
        label='性别',
        validators=[
            DataRequired(message='性别不能为空'),
            NumberRange(min=1, max=3, message='性别值在1~3之间')
        ]
    )
    # 手机号
    mobile = StringField(
        label='手机号',
        validators=[
            DataRequired(message='手机号不能为空'),
            Length(max=30, message='手机号长度不得超过30个字符')
        ]
    )
    # 邮箱
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired(message='邮箱不能为空'),
            Length(max=30, message='邮箱长度不得超过30个字符')
        ]
    )
    # 详细地址
    address = StringField(
        label='详细地址',
        validators=[
            DataRequired(message='详细地址不能为空'),
            Length(max=255, message='详细地址长度不得超过255个字符')
        ]
    )
    # 个人简介
    intro = StringField(
        label='个人简介',
        validators=[
            Length(max=255, message='个人简介长度不得超过255个字符')
        ]
    )


# 修改密码表单验证
class UpdatePwdForm(FlaskForm):
    # 原始密码
    oldPassword = StringField(
        label='原始密码',
        validators=[
            DataRequired(message='原始密码不能为空'),
            Length(min=6, max=12, message='原始密码长度为6~12个字符')
        ]
    )
    # 新密码
    newPassword = StringField(
        label='新密码',
        validators=[
            DataRequired(message='新密码不能为空'),
            Length(min=6, max=12, message='新密码长度为6~12个字符')
        ]
    )
    # 确认密码
    rePassword = StringField(
        label='确认密码',
        validators=[
            DataRequired(message='确认密码不能为空'),
            Length(min=6, max=12, message='确认密码长度为6~12个字符')
        ]
    )


# 重置密码表单
class ResetPwdForm(FlaskForm):
    # 用户ID
    id = IntegerField(
        # 文本描述
        label='用户ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='用户ID必须大于0')
        ]
    )
