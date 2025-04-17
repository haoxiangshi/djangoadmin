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

from apps.models.dict_data import DictData


# 字典项表单验证
class DictDataForm(FlaskForm):
    # 字典项ID
    id = IntegerField(
        # 文本描述
        label='字典项ID',
        # 验证规则
        validators=[
        ]
    )
    # 字典项名称
    name = StringField(
        label='字典项名称',
        validators=[
            DataRequired(message='字典项名称不能为空'),
            Length(max=150, message='字典项名称长度不得超过150个字符')
        ]
    )
    # 字典项值
    value = StringField(
        label='字典项值',
        validators=[
            DataRequired(message='字典项值不能为空'),
            Length(max=150, message='字典项值长度不得超过150个字符')
        ]
    )
    # 字典ID
    dict_id = IntegerField(
        label='字典ID',
        validators=[
            DataRequired(message='字典ID不能为空'),
            NumberRange(min=0, message='字典ID值不得小于0')
        ]
    )
    # 字典项备注
    note = StringField(
        label='字典项备注',
        validators=[
            Length(max=255, message='字典项备注长度不得超过255个字符')
        ]
    )
    # 字典项排序
    sort = IntegerField(
        label='字典项排序',
        validators=[
            DataRequired(message='字典项排序不能为空'),
            NumberRange(min=0, max=99999, message='字典项排序值在0~99999之间')
        ]
    )

    # 字典项名称重复性验证
    def validate_name(self, field):
        # 查询单条数据
        if not field.data and DictData.query.filter(DictData.name == field.data).first():
            raise ValidationError("字典项名称不能重复")
