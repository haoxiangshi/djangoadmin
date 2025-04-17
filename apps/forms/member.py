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

from apps.models.member import Member


# 会员表单验证
class MemberForm(FlaskForm):
    # 会员ID
    id = IntegerField(
        # 文本描述
        label='会员ID',
        # 验证规则
        validators=[
        ]
    )
    # 会员姓名
    realname = StringField(
        label='会员姓名',
        validators=[
            DataRequired(message='会员姓名不能为空'),
            Length(max=150, message='会员姓名长度不得超过150个字符')
        ]
    )
    # 会员昵称
    nickname = StringField(
        label='会员昵称',
        validators=[
            DataRequired(message='会员昵称不能为空'),
            Length(max=150, message='会员昵称长度不得超过150个字符')
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
    # 出生日期
    birthday = DateField(
        label='出生日期',
        validators=[
            DataRequired(message='出生日期不能为空'),
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
    # 会员等级
    member_level = IntegerField(
        label='会员等级',
        validators=[
            DataRequired(message='会员等级不能为空'),
            NumberRange(min=0, message='会员等级值不得小于0')
        ]
    )
    # 个人简介
    intro = StringField(
        label='个人简介',
        validators=[
            Length(max=255, message='个人简介长度不得超过255个字符')
        ]
    )
    # 个人签名
    signature = StringField(
        label='个人签名',
        validators=[
            Length(max=255, message='个人签名长度不得超过255个字符')
        ]
    )
    # 注册来源：1-网站注册 2-客户端注册 3-小程序注册 4-手机站注册 5-后台添加
    source = IntegerField(
        label='注册来源',
        validators=[
            DataRequired(message='注册来源不能为空'),
            NumberRange(min=1, max=5, message='注册来源值在1~5之间')
        ]
    )
    # 会员状态：1-正常 2-禁用
    status = IntegerField(
        label='会员状态',
        validators=[
            DataRequired(message='会员状态不能为空'),
            NumberRange(min=1, max=2, message='会员状态值在1~2之间')
        ]
    )

    # 登录账号重复性验证
    def validate_username(self, field):
        # 查询单条数据
        if not field.data and Member.query.filter(Member.username == field.data).first():
            raise ValidationError("登录账号不能重复")


# 状态设置表单
class MemberStatusForm(FlaskForm):
    # 会员ID
    id = IntegerField(
        # 文本描述
        label='会员ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='会员ID必须大于0')
        ]
    )
    # 会员状态
    status = IntegerField(
        label='会员状态',
        validators=[
            DataRequired(message='会员状态不能为空'),
            NumberRange(min=1, max=2, message='会员状态值在1~2之间')
        ]
    )
