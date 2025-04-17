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


from flask import request
from sqlalchemy import and_

import utils
from apps.constants.message import PAGE_LIMIT
from apps.forms.member_level import MemberLevelForm
from apps.models.member_level import MemberLevel
from extends import db
from utils import R, regular
from utils.utils import uid


# 查询会员登记分页数据
def MemberLevelList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = MemberLevel.query.filter(MemberLevel.is_delete == 0)
    # 会员等级名称
    name = request.args.get('name')
    if name:
        query = query.filter(MemberLevel.name.like('%' + name + '%'))
    # 排序
    query = query.order_by(MemberLevel.sort.asc())
    # 记录总数
    count = query.count()
    # 分页查询
    list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(list) > 0:
        for item in list:
            # 对象转字典
            data = utils.load2dict(item)
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据会员等级ID查询详情
def MemberLevelDetail(member_level_id):
    # 根据ID查询会员等级
    member_level = MemberLevel.query.filter(and_(MemberLevel.id == member_level_id, MemberLevel.is_delete == 0)).first()
    # 查询结果判空
    if not member_level:
        return None
    # 对象转字典
    data = utils.load2dict(member_level)
    # 返回结果
    return data


# 添加会员等级
def MemberLevelAdd():
    # 表单验证
    form = MemberLevelForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 表单数据赋值给对象
    member_level = MemberLevel(**form.data)
    member_level.create_user = uid()
    # 插入数据
    member_level.save()
    # 返回结果
    return R.ok(msg="添加成功")


# 更新会员等级
def MemberLevelUpdate():
    # 表单验证
    form = MemberLevelForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 记录ID判空
    id = form.data['id']
    if not id or int(id) <= 0:
        return R.failed("记录ID不能为空")

    # 根据ID查询记录
    member_level = MemberLevel.query.filter(and_(MemberLevel.id == id, MemberLevel.is_delete == 0)).first()
    # 查询结果判空
    if not member_level:
        return R.failed("记录不存在")
    result = MemberLevel.query.filter_by(id=id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 删除会员等级
def MemberLevelDelete(member_level_id):
    # 记录ID为空判断
    if not member_level_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = member_level_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            member_level = MemberLevel.query.filter(
                and_(MemberLevel.id == int(vId), MemberLevel.is_delete == 0)).first()
            # 查询结果判空
            if not member_level:
                return R.failed("职级不存在")
            # 设置删除标识
            member_level.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 获取会员等级列表
def GetMemberLevelList():
    list = MemberLevel.query.filter(MemberLevel.is_delete == 0).order_by(MemberLevel.sort.asc()).all()
    # 实例化对象
    result = []
    # 遍历数据源
    for v in list:
        # 对象转字典
        item = utils.load2dict(v)
        # 加入列表
        result.append(item)
    # 返回结果
    return result
