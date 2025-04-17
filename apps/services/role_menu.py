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

from apps.forms.role_menu import RoleMenuForm
from apps.models.menu import Menu
from apps.models.role_menu import RoleMenu
from utils import regular, R


# 根据角色ID查询菜单列表
def getRoleMenuList(role_id):
    # 获取全部菜单列表
    menuList = Menu.query.filter(and_(Menu.is_delete == 0, Menu.status == 1)).order_by(Menu.sort.asc()).all()
    if len(menuList) == 0:
        return None
    # 根据角色ID查询角色菜单关系数据
    role_menu = RoleMenu.query.filter(RoleMenu.role_id == role_id).all()
    # 菜单ID集合
    idList = []
    # 遍历角色菜单数据源
    if role_menu:
        for v in role_menu:
            # 加入数组
            idList.append(v.menu_id)

    # 实例化菜单列表
    list = []
    # 遍历菜单数据
    for menu in menuList:
        # 菜单ID
        menu_id = menu.id
        data = {
            'id': menu_id,
            'title': menu.title,
            'open': True,
            'parentId': menu.parent_id,
        }
        if menu_id in idList:
            data['checked'] = True
        # 加入数组
        list.append(data)
    # 返回结果
    return list


# 保存角色菜单数据
def save():
    # 表单验证
    form = RoleMenuForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 角色ID
    role_id = form.role_id.data
    # 菜单ID
    menuIds = form.menu_id.data

    # 删除当前角色ID相关菜单权限
    RoleMenu.query.filter(RoleMenu.role_id == role_id).delete()

    # 处理菜单数据
    if menuIds != "":
        menuIdList = menuIds.split(',')
        # 遍历菜单ID数据源
        if len(menuIdList) > 0:
            for menu_id in menuIdList:
                if menu_id == "":
                    continue
                # 创建角色菜单数据
                role_menu = RoleMenu(
                    role_id=role_id,
                    menu_id=menu_id
                )
                role_menu.save()
    # 返回结果
    return R.ok()
