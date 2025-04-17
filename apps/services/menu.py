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
from sqlalchemy import and_, text

import utils
from apps.forms.menu import MenuForm
from apps.models.menu import Menu
from config.env import DB_PREFIX
from extends import db
from utils import R, regular
from utils.utils import uid


# 查询菜单列表
def MenuList():
    # 实例化查询对象
    query = Menu.query.filter(Menu.is_delete == 0)
    # 菜单名称
    name = request.args.get('name')
    if name:
        # 菜单名称模糊查询
        query = query.filter(Menu.name.like('%' + name + '%'))
    # 查询数据
    list = query.order_by(Menu.sort.asc()).all()

    # 实例化数组对象
    result = []
    # 遍历数据源
    if list:
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
    return R.ok(data=result)


# 根据ID查询菜单详情
def MenuDetail(menu_id):
    # 根据ID查询菜单
    menu = Menu.query.filter(and_(Menu.id == menu_id, Menu.is_delete == 0)).first()
    # 查询结果判空
    if not menu:
        return None

    # 查询菜单权限节点
    permission_list = Menu.query.filter(and_(Menu.parent_id == menu_id, Menu.type == 1, Menu.is_delete == 0)).all()
    # 选中的权限节点
    checked_list = []
    if permission_list:
        for v in permission_list:
            checked_list.append(v.sort)
    # 对象转字典
    data = utils.load2dict(menu)
    # 权限节点
    data['checked_list'] = checked_list
    # 返回结果
    return data


# 添加菜单
def MenuAdd():
    # 表单验证
    form = MenuForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 权限节点
    checked_list = form.checked_list.data
    # 从表单中移除角色信息
    del form.checked_list

    # 表单数据赋值给对象
    menu = Menu(**form.data)
    menu.create_user = uid()
    # 插入数据
    db.session.add(menu)
    db.session.commit()

    # 返回结果
    return R.ok(msg="添加成功")


# 更新菜单
def MenuUpdate():
    # 表单验证
    form = MenuForm(request.form)
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
    menu = Menu.query.filter(and_(Menu.id == id, Menu.is_delete == 0)).first()
    # 查询结果判空
    if not menu:
        return R.failed("记录不存在")

    # 权限节点
    checked_list = form.checked_list.data
    # 从表单中移除角色信息
    del form.checked_list

    # 更新数据源
    result = Menu.query.filter_by(id=id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")

    # 返回结果
    return R.ok(msg="更新成功")


# 删除菜单
def MenuDelete(menu_id):
    # 记录ID为空判断
    if not menu_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = menu_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            menu = Menu.query.filter(and_(Menu.id == int(vId), Menu.is_delete == 0)).first()
            # 查询结果判空
            if not menu:
                return R.failed("记录不存在")
            # 设置删除标识
            menu.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 获取用户权限节点
def GetPermissionsList(user_id):
    if user_id == 1:
        # 超级管理员
        list = Menu.query.filter(and_(Menu.is_delete == 0, Menu.type == 1)).all()
        permission_list = []
        if list:
            for item in list:
                permission_list.append(item.permission)
        # 返回结果
        return permission_list
    else:
        sql = 'SELECT m.* FROM ' + DB_PREFIX + 'menu AS m '
        sql += 'INNER JOIN ' + DB_PREFIX + 'role_menu AS rm ON m.id=rm.menu_id '
        sql += 'INNER JOIN ' + DB_PREFIX + 'user_role AS ur ON ur.role_id=rm.role_id '
        sql += 'WHERE ur.user_id={} AND (m.type=1 OR (m.type=0 AND m.permission!="")) AND m.`status`=1 AND m.is_delete=0'.format(
            user_id)
        list = db.session.execute(text(sql)).fetchall()
        permission_list = []
        if list:
            for item in list:
                permission_list.append(item.permission)
        # 返回结果
        return permission_list


# 根据用户ID查询菜单列表
def GetPermissionMenuList(user_id):
    if user_id == 1:
        # 超级管理员
        # 查询全部菜单列表
        list = Menu.query.filter(and_(Menu.is_delete == 0, Menu.status == 1, Menu.type == 0)).order_by(Menu.sort.asc())
        menu_list = GetTreeList(list)
        return menu_list
    else:
        # 其他用户
        sql = 'SELECT m.* FROM ' + DB_PREFIX + 'menu AS m '
        sql += 'INNER JOIN ' + DB_PREFIX + 'role_menu AS rm ON m.id=rm.menu_id '
        sql += 'INNER JOIN ' + DB_PREFIX + 'user_role AS ur ON ur.role_id=rm.role_id '
        sql += 'WHERE ur.user_id={} AND m.type=0 AND m.`status`=1 AND m.is_delete=0 '.format(user_id)
        sql += 'ORDER BY m.sort ASC;'
        list = db.session.execute(text(sql)).fetchall()
        menu_list = GetTreeList(list)
        return menu_list


# 根据数据源获取树状结构
def GetTreeList(list):
    # 实例化数组
    menu_list = []
    if list:
        for item in list:
            data = {
                'id': item.id,
                'title': item.title,
                'icon': item.icon,
                'path': item.path,
                'parent_id': item.parent_id,
                'type': item.type,
                'component': item.component,
                'permission': item.permission,
                'target': item.target,
                'hide': item.hide,
            }
            menu_list.append(data)
    # 处理数据源为树状结构
    result = get_tree(menu_list, 0)
    # 返回结果
    return result


# 获取树状结构
def get_tree(data, parent_id):
    result = []
    for item in data:
        if parent_id != item["parent_id"]:
            continue
        # 递归调用
        temp = get_tree(data, item["id"])
        if (len(temp) > 0):
            item["children"] = temp
        else:
            item["children"] = []
        # 加入数组
        result.append(item)
    # 返回结果
    return result
