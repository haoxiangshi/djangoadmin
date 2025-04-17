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


# 城市表单验证
class CityForm(FlaskForm):
    # 城市ID
    id = IntegerField(
        # 文本描述
        label='城市ID',
        # 验证规则
        validators=[
        ]
    )
    # 城市名称
    name = StringField(
        label='城市名称',
        validators=[
            DataRequired(message='城市名称不能为空'),
            Length(max=150, message='城市名称长度不得超过150个字符')
        ]
    )
    # 城市简称
    short_name = StringField(
        label='城市简称',
        validators=[
            DataRequired(message='城市简称不能为空'),
            Length(max=150, message='城市简称长度不得超过150个字符')
        ]
    )
    # 城市拼音
    pinyin = StringField(
        label='城市拼音',
        validators=[
            DataRequired(message='城市拼音不能为空'),
            Length(max=150, message='城市拼音长度不得超过150个字符')
        ]
    )
    # 城市区号
    city_code = StringField(
        label='城市区号',
        validators=[
            DataRequired(message='城市区号不能为空'),
            Length(max=6, message='城市区号长度不得超过6个字符')
        ]
    )
    # 行政编码
    area_code = StringField(
        label='行政编码',
        validators=[
            DataRequired(message='行政编码不能为空'),
            Length(max=20, message='行政编码长度不得超过20个字符')
        ]
    )
    # 城市邮编
    zip_code = StringField(
        label='城市邮编',
        validators=[
            DataRequired(message='城市邮编不能为空'),
            Length(max=6, message='城市邮编长度不得超过6个字符')
        ]
    )
    # 城市级别：1-省份 2-城市 3-县区 4-街道
    level = IntegerField(
        label='城市级别',
        validators=[
            DataRequired(message='城市级别不能为空'),
            NumberRange(min=1, max=4, message='城市级别值在1~4之间')
        ]
    )
    # 城市经度
    lng = StringField(
        label='城市经度',
        validators=[
            DataRequired(message='城市经度不能为空'),
            Length(max=150, message='城市经度长度不得超过150个字符')
        ]
    )
    # 城市纬度
    lat = StringField(
        label='城市纬度',
        validators=[
            DataRequired(message='城市纬度不能为空'),
            Length(max=150, message='城市纬度长度不得超过150个字符')
        ]
    )
    # 上级ID
    pid = IntegerField(
        label='上级ID',
        validators=[
        ]
    )
