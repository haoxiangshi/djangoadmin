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
from wtforms import IntegerField, StringField, DateField, DateTimeField
from wtforms.validators import NumberRange, DataRequired, Length


# 广告表单验证
class AdForm(FlaskForm):
    # 广告ID
    id = IntegerField(
        # 文本描述
        label='广告ID',
        # 验证规则
        validators=[
        ]
    )
    # 广告标题
    title = StringField(
        label='广告标题',
        validators=[
            DataRequired(message='广告标题不能为空'),
            Length(max=255, message='广告标题长度不得超过255个字符')
        ]
    )
    # 广告位ID
    sort_id = IntegerField(
        label='广告位ID',
        validators=[
            DataRequired(message='广告位ID不能为空'),
            NumberRange(min=0, message='广告位ID不得小于0')
        ]
    )
    # 广告类型：1-图片 2-文字 3-视频 4-推荐
    type = IntegerField(
        label='广告类型',
        validators=[
            DataRequired(message='广告类型不能为空'),
            NumberRange(min=1, max=4, message='广告类型值在1~4之间')
        ]
    )
    # 广告封面
    cover = StringField(
        label='广告封面',
        validators=[
            DataRequired(message='广告封面不能为空'),
            Length(max=255, message='广告封面长度不得超过255个字符')
        ]
    )
    # 广告URL
    url = StringField(
        label='广告URL',
        validators=[
            DataRequired(message='广告URL不能为空'),
            Length(max=255, message='广告URL长度不得超过255个字符')
        ]
    )
    # 广告宽度
    width = IntegerField(
        label='广告宽度',
        validators=[
            DataRequired(message='广告宽度不能为空'),
            NumberRange(min=0, message='广告宽度不得小于0')
        ]
    )
    # 广告高度
    height = IntegerField(
        label='广告高度',
        validators=[
            DataRequired(message='广告高度不能为空'),
            NumberRange(min=0, message='广告高度不得小于0')
        ]
    )
    # 开始时间
    start_time = DateTimeField(
        label='开始时间',
        validators=[
            DataRequired(message='开始时间不能为空'),
        ]
    )
    # 结束时间
    end_time = DateTimeField(
        label='结束时间',
        validators=[
            DataRequired(message='结束时间不能为空'),
        ]
    )
    # 广告状态
    status = IntegerField(
        label='广告状态',
        validators=[
            DataRequired(message='广告状态不能为空'),
            NumberRange(min=1, max=2, message='广告状态值在1~2之间')
        ]
    )
    # 广告排序
    sort = IntegerField(
        label='广告排序',
        validators=[
            DataRequired(message='广告排序不能为空'),
            NumberRange(min=0, max=99999, message='广告排序值在0~99999之间')
        ]
    )
    # 广告备注
    note = StringField(
        label='广告备注',
        validators=[
            Length(max=255, message='广告备注长度不得超过255个字符')
        ]
    )
    # 广告内容
    content = StringField(
        label='广告内容',
        validators=[
        ]
    )


# 状态设置表单
class AdStatusForm(FlaskForm):
    # 广告ID
    id = IntegerField(
        # 文本描述
        label='广告ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='广告ID必须大于0')
        ]
    )
    # 广告状态
    status = IntegerField(
        label='广告状态',
        validators=[
            DataRequired(message='广告状态不能为空'),
            NumberRange(min=1, max=2, message='广告状态值在1~2之间')
        ]
    )
