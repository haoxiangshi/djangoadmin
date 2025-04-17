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
from apps.constants.constants import GENDER_LIST, MEMBER_SOURCE_LIST
from apps.constants.message import PAGE_LIMIT
from apps.forms.member import MemberForm, MemberStatusForm
from apps.models.member import Member
from apps.models.member_level import MemberLevel
from extends import db
from utils import R, regular, md5
from utils.utils import getImageURL, saveImage, uid


# 查询会员分页数据
def MemberList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = Member.query.filter(Member.is_delete == 0)
    # 会员账号
    username = request.args.get('username')
    if username:
        query = query.filter(Member.username == username)
    # 注册来源：1-网站注册 2-客户端注册 3-小程序注册 4-手机站注册 5-后台添加
    source = request.args.get('source')
    if source:
        query = query.filter(Member.source == source)
    # 性别
    gender = request.args.get('gender')
    if gender:
        query = query.filter(Member.gender == gender)
    # 会员状态
    status = request.args.get('status')
    if status:
        query = query.filter(Member.status == status)
    # 排序
    query = query.order_by(Member.id.desc())
    # 记录总数
    count = query.count()
    # 分页查询
    member_list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(member_list) > 0:
        # 查看会员等级列表
        memberLevelList = MemberLevel.query.filter(MemberLevel.is_delete == 0).all()
        member_level_list = {}
        if memberLevelList:
            for member_level in memberLevelList:
                member_level_list[member_level.id] = member_level.name

        # 遍历会员数据源
        for item in member_list:
            # 对象转字典
            data = utils.load2dict(item)
            # 性别
            data['gender_name'] = GENDER_LIST.get(item.gender)
            # 头像
            data['avatar'] = getImageURL(item.avatar) if item.avatar else ""
            # 出生日期
            data['birthday'] = str(item.birthday.strftime('%Y-%m-%d')) if item.birthday else None
            # 会员等级描述
            data['member_level_name'] = member_level_list.get(item.member_level) if member_level_list else ""
            # 会员来源描述
            data['source_name'] = MEMBER_SOURCE_LIST.get(item.source)
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据ID查看会员详情
def MemberDetail(member_id):
    # 根据ID查询会员
    member = Member.query.filter(and_(Member.id == member_id, Member.is_delete == 0)).first()
    # 查询结果判空
    if not member:
        return None

    # 城市编码
    cityList = []
    # 省份编号
    cityList.append(member.province_code)
    # 城市编码
    cityList.append(member.city_code)
    # 县区编码
    cityList.append(member.district_code)

    # 对象转字典
    data = utils.load2dict(member)
    # 头像
    data['avatar'] = getImageURL(member.avatar) if member.avatar else ""
    # 出生日期
    data['birthday'] = str(member.birthday.strftime('%Y-%m-%d')) if member.birthday else None
    # 行政区划
    data['city'] = cityList

    # 返回结果
    return data


# 添加会员
def MemberAdd():
    # 表单验证
    form = MemberForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 图片处理
    avatar = form.avatar.data
    if avatar:
        form.avatar.data = saveImage(avatar, "member")

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

    # 表单数据赋值给对象
    member = Member(**form.data)
    member.create_user = uid()
    # 插入数据
    member.save()

    # 返回结果
    return R.ok(msg="添加成功")


# 更新会员
def MemberUpdate():
    form = MemberForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 记录ID判空
    member_id = form.data['id']
    if not member_id or int(member_id) <= 0:
        return R.failed("记录ID不能为空")

    # 根据ID查询记录
    user = Member.query.filter(and_(Member.id == member_id, Member.is_delete == 0)).first()
    # 查询结果判空
    if not user:
        return R.failed("记录不存在")

    # 图片处理
    avatar = form.avatar.data
    if avatar:
        form.avatar.data = saveImage(avatar, "member")

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

    # 更新数据
    result = Member.query.filter_by(id=member_id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 删除会员
def MemberDelete(member_id):
    # 记录ID为空判断
    if not member_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = member_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            member = Member.query.filter(and_(Member.id == int(vId), Member.is_delete == 0)).first()
            # 查询结果判空
            if not member:
                return R.failed("记录不存在")
            # 设置删除标识
            member.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 设置状态
def MemberStatus():
    # 表单验证
    form = MemberStatusForm(request.form)
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
    user = Member.query.filter(and_(Member.id == id, Member.is_delete == 0)).first()
    # 查询结果判空
    if not user:
        return R.failed("记录不存在")

    # 更新记录
    result = Member.query.filter_by(id=id).update({
        "status": status
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("设置失败")
    # 返回结果
    return R.ok(msg="设置成功")
