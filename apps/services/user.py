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

import utils.dict
from apps.constants.constants import GENDER_LIST
from apps.constants.message import PAGE_LIMIT
from apps.forms.user import UserForm, UserStatusForm, UpdatePwdForm, UserInfoForm, ResetPwdForm
from apps.models.dept import Dept
from apps.models.level import Level
from apps.models.position import Position
from apps.models.user import User
from apps.models.user_role import UserRole
from apps.services import user_role
from extends import db
from utils import R, regular, md5
from utils.utils import getImageURL, uid, saveImage


# 查询用户分页数据
def UserList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = User.query.filter(User.is_delete == 0)
    # 用户姓名
    realname = request.args.get('realname')
    if realname:
        query = query.filter(User.realname.like('%' + realname + '%'))
    # 性别
    gender = request.args.get('gender')
    if gender:
        query = query.filter(User.gender == gender)
    # 用户状态
    status = request.args.get('status')
    if status:
        query = query.filter(User.status == status)
    # 排序
    query = query.order_by(User.id.asc())
    # 记录总数
    count = query.count()
    # 分页查询
    user_list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(user_list) > 0:
        # 查看部门列表
        dept_list = Dept.query.filter(Dept.is_delete == 0).all()
        deptList = {}
        if dept_list:
            for dept in dept_list:
                deptList[dept.id] = dept.name

        # 查看职级列表
        level_list = Level.query.filter(Level.is_delete == 0).all()
        levelList = {}
        if level_list:
            for level in level_list:
                levelList[level.id] = level.name

        # 查看用户列表
        position_list = Position.query.filter(Position.is_delete == 0).all()
        positionList = {}
        if position_list:
            for position in position_list:
                positionList[position.id] = position.name

        for item in user_list:
            # 获取用户角色列表
            roleList = user_role.getUserRoleList(item.id)
            # 城市
            city_list = []
            # 省份编码
            city_list.append(item.province_code)
            # 城市编码
            city_list.append(item.city_code)
            # 县区编码
            city_list.append(item.district_code)

            # 对象转字典
            data = utils.load2dict(item)
            # 性别
            data['gender_name'] = GENDER_LIST.get(item.gender)
            # 头像
            data['avatar'] = getImageURL(item.avatar) if item.avatar else ""
            # 出生日期
            data['birthday'] = str(item.birthday.strftime('%Y-%m-%d')) if item.birthday else None
            # 部门名称
            data['dept_name'] = deptList.get(item.dept_id) if deptList else None
            # 职级名称
            data['level_name'] = levelList.get(item.level_id) if levelList else None
            # 岗位名称
            data['position_name'] = positionList.get(item.position_id) if positionList else None
            # 角色列表
            data['roleList'] = roleList
            # 行政区划
            data['city'] = city_list
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据ID查询用户详情
def UserDetail(user_id):
    # 根据ID查询用户
    user = User.query.filter(and_(User.id == user_id, User.is_delete == 0)).first()
    # 查询结果判空
    if not user:
        return None

    # 获取用户角色数据
    roleList = UserRole.query.filter(UserRole.user_id == user.id).all()
    roles = []
    for role in roleList:
        roles.append(role.role_id)

    # 城市编码
    cityList = []
    # 省份编号
    cityList.append(user.province_code)
    # 城市编码
    cityList.append(user.city_code)
    # 县区编码
    cityList.append(user.district_code)

    # 对象转字典
    data = utils.load2dict(user)
    # 头像
    data['avatar'] = getImageURL(user.avatar) if user.avatar else ""
    # 出生日期
    data['birthday'] = str(user.birthday.strftime('%Y-%m-%d')) if user.birthday else None
    # 角色
    data['roles'] = roles
    # 行政区划
    data['city'] = cityList
    # 返回结果
    return data


# 添加用户
def UserAdd():
    # 表单验证
    form = UserForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 图片处理
    avatar = form.avatar.data
    if avatar:
        form.avatar.data = saveImage(avatar, "user")

    # 密码存在是MD5加密
    password = form.password.data
    if password:
        form.password.data = md5.getPassword(password)
    else:
        # 密码不填时保持原密码值不做更新梳理
        del form.password

    # 行政区划处理
    citys = form.city.data
    # 从表单中移除行政区划
    del form.city
    if citys:
        cityList = citys.split(',')
        if len(cityList) == 3:
            # 省份编码
            form.province_code.data = cityList[0]
            # 城市编码
            form.city_code.data = cityList[1]
            # 县区编码
            form.district_code.data = cityList[2]

    # 用户角色
    roles = form.roles.data
    # 从表单中移除角色信息
    del form.roles

    # 表单数据赋值给对象
    user = User(**form.data)
    user.create_user = uid()
    # 插入数据
    db.session.add(user)
    db.session.commit()

    # 创建用户角色数据
    addUserRole(user.id, roles)

    # 返回结果
    return R.ok(msg="添加成功")


# 更新用户
def UserUpdate():
    # 表单验证
    form = UserForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 记录ID判空
    user_id = form.data['id']
    if not user_id or int(user_id) <= 0:
        return R.failed("记录ID不能为空")

    # 根据ID查询记录
    user = User.query.filter(and_(User.id == user_id, User.is_delete == 0)).first()
    # 查询结果判空
    if not user:
        return R.failed("记录不存在")

    # 图片处理
    avatar = form.avatar.data
    if avatar:
        form.avatar.data = saveImage(avatar, "user")

    # 密码存在是MD5加密
    password = form.password.data
    if password:
        form.password.data = md5.getPassword(password)
    else:
        # 密码不填时保持原密码值不做更新梳理
        del form.password

    # 行政区划处理
    citys = form.city.data
    # 从表单中移除行政区划
    del form.city
    if citys:
        cityList = citys.split(',')
        if len(cityList) == 3:
            # 省份编码
            form.province_code.data = cityList[0]
            # 城市编码
            form.city_code.data = cityList[1]
            # 县区编码
            form.district_code.data = cityList[2]

    # 用户角色
    roles = form.roles.data
    # 从表单中移除角色信息
    del form.roles

    # 更新数据
    result = User.query.filter_by(id=user_id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")

    # 创建用户角色数据
    addUserRole(user_id, roles)
    # 返回结果
    return R.ok(msg="更新成功")


# 创建用户角色信息
def addUserRole(user_id, roles):
    # 删除用户角色关系数据
    UserRole.query.filter(UserRole.user_id == user_id).delete()
    # 创建新的用户角色关系
    if roles:
        roleIdList = roles.split(',')
        for roleId in roleIdList:
            # 为空直接跳过
            if not roleId:
                continue
            user_role = UserRole(
                user_id=user_id,
                role_id=roleId
            )
            user_role.save()


# 删除用户
def UserDelete(user_id):
    # 记录ID为空判断
    if not user_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = user_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            user = User.query.filter(and_(User.id == int(vId), User.is_delete == 0)).first()
            # 查询结果判空
            if not user:
                return R.failed("记录不存在")
            # 设置删除标识
            user.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 设置状态
def UserStatus():
    # 表单验证
    form = UserStatusForm(request.form)
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
    user = User.query.filter(and_(User.id == id, User.is_delete == 0)).first()
    # 查询结果判空
    if not user:
        return R.failed("记录不存在")

    # 更新记录
    result = User.query.filter_by(id=id).update({
        "status": status
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("设置失败")
    # 返回结果
    return R.ok(msg="设置成功")


# 更新用户信息
def UserInfo():
    # 表单验证
    form = UserInfoForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 用户ID
    user_id = uid()
    # 根据ID查询记录
    user = User.query.filter(and_(User.id == user_id, User.is_delete == 0)).first()
    # 查询结果判空
    if not user:
        return R.failed("记录不存在")

    # 更新记录
    result = User.query.filter_by(id=user_id).update({
        'realname': form.realname.data,
        'nickname': form.nickname.data,
        'gender': form.gender.data,
        'mobile': form.mobile.data,
        'email': form.email.data,
        'address': form.address.data,
        'intro': form.intro.data
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 更新密码
def UpdatePwd():
    # 表单验证
    form = UpdatePwdForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 用户ID
    user_id = uid()

    # 根据ID查询用户
    user = User.query.filter(and_(User.is_delete == 0, User.id == user_id)).first()
    if not user:
        return R.failed("用户不存在")

    # 密码MD5加密
    oldPassword = md5.getPassword(form.oldPassword.data)
    # 判断原始密码是否正确
    if oldPassword != user.password:
        return R.failed("原始密码不正确")

    # 加密新密码
    password = md5.getPassword(form.newPassword.data)
    result = User.query.filter_by(id=user_id).update({
        "password": password
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 重置密码
def UserResetPwd():
    # 表单验证
    form = ResetPwdForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 用户ID
    user_id = form.id.data

    # 根据ID查询用户
    user = User.query.filter(and_(User.is_delete == 0, User.id == user_id)).first()
    if not user:
        return R.failed("用户不存在")

    ## 加密新密码
    password = md5.getPassword("123456")
    result = User.query.filter_by(id=user_id).update({
        "password": password
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("重置密码失败")
    # 返回结果
    return R.ok(msg="重置密码成功")
