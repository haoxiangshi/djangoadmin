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
from apps.forms.role import RoleForm, RoleStatusForm
from apps.models.role import Role
from extends import db
from utils import R, regular
from utils.utils import uid


# 查询角色分页数据
def RoleList():
    # 页码
    page = int(request.args.get('page', 1))
    # 每页数
    limit = int(request.args.get('limit', PAGE_LIMIT))
    # 分页查询
    query = Role.query.filter(Role.is_delete == 0)
    # 角色名称
    name = request.args.get('name')
    if name:
        query = query.filter(Role.name.like('%' + name + '%'))
    # 排序
    query = query.order_by(Role.sort.asc())
    # 记录总数
    count = query.count()
    # 查询分页数据
    role_list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化返回对象
    result = []
    # 遍历数据源
    if len(role_list) > 0:
        for item in role_list:
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


# 根据角色ID查询详情
def RoleDetail(role_id):
    # 根据ID查询角色
    role = Role.query.filter(and_(Role.id == role_id, Role.is_delete == 0)).first()
    # 查询结果判空
    if not role:
        return None
    # 对象转字典
    data = utils.load2dict(role)
    # 返回结果
    return data


# 添加角色
def RoleAdd():
    # 表单验证
    form = RoleForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 表单数据赋值给对象
    role = Role(**form.data)
    role.create_user = uid()
    # 插入数据
    role.save()
    # 返回结果
    return R.ok(msg="添加成功")


# 更新角色
def RoleUpdate():
    # 表单验证
    form = RoleForm(request.form)
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
    role = Role.query.filter(and_(Role.id == id, Role.is_delete == 0)).first()
    # 查询结果判空
    if not role:
        return R.failed("记录不存在")
    result = Role.query.filter_by(id=id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 删除角色
def RoleDelete(role_id):
    # 记录ID为空判断
    if not role_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = role_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            role = Role.query.filter(and_(Role.id == int(vId), Role.is_delete == 0)).first()
            # 查询结果判空
            if not role:
                return R.failed("记录不存在")
            # 设置删除标识
            role.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 设置状态
def RoleStatus():
    # 表单验证
    form = RoleStatusForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)
    # 记录ID
    id = int(form.data['id'])
    # 状态值
    status = int(form.data['status'])
    # 根据ID查询记录
    role = Role.query.filter(and_(Role.id == id, Role.is_delete == 0)).first()
    # 查询结果判空
    if not role:
        return R.failed("记录不存在")

    # 更新记录
    result = Role.query.filter_by(id=id).update({
        "status": status
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("设置失败")
    # 返回结果
    return R.ok(msg="设置成功")


# 获取角色列表
def getRoleList():
    # 查询角色列表
    list = Role.query.filter(and_(Role.is_delete == 0, Role.status == 1)).order_by(Role.sort.asc()).all()
    # 实例化角色列表
    role_list = []
    # 遍历数据源
    if list:
        for v in list:
            # 对象转字典
            item = utils.load2dict(v)
            # 加入数组
            role_list.append(item)
    # 返回结果
    return role_list
