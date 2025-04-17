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
from apps.constants.constants import LINK_TYPE_LIST, LINK_PLATFORM_LIST, LINK_FORM_LIST
from apps.constants.message import PAGE_LIMIT
from apps.forms.link import LinkForm, LinkStatusForm
from apps.models.link import Link
from extends import db
from utils import R, regular
from utils.utils import getImageURL, saveImage, uid


# 查看友链分页数据
def LinkList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = Link.query.filter(Link.is_delete == 0)
    # 友链名称
    name = request.args.get('name')
    if name:
        query = query.filter(Link.name.like('%' + name + '%'))
    # 友链类型：1-友情链接 2-合作伙伴
    type = request.args.get('type')
    if type:
        query = query.filter(Link.type == type)
    # 投放平台：1PC站 2WAP站 3微信小程序 4APP应用
    platform = request.args.get('platform')
    if platform:
        query = query.filter(Link.platform == platform)
    # 友链形式：1文字链接 2图片链接
    form = request.args.get('form')
    if form:
        query = query.filter(Link.form == form)
    # 状态筛选
    status = request.args.get('status')
    if status:
        query = query.filter(Link.status == status)
    # 排序
    query = query.order_by(Link.sort.desc())
    # 记录总数
    count = query.count()
    # 分页查询
    link_list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(link_list) > 0:
        for item in link_list:
            # 对象转字典
            data = utils.load2dict(item)
            # 友链类型
            data['type_name'] = LINK_TYPE_LIST.get(item.type)
            # 投放平台
            data['platform_name'] = LINK_PLATFORM_LIST.get(item.platform)
            # 友链形式
            data['form_name'] = LINK_FORM_LIST.get(item.form)
            # 友链图片
            data['image'] = getImageURL(item.image) if item.image else None
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据ID查看友链详情
def LinkDetail(link_id):
    # 根据ID查询友链
    link = Link.query.filter(and_(Link.id == link_id, Link.is_delete == 0)).first()
    # 查询结果为空判断
    if not link:
        return None
    # 对象转字典
    data = utils.load2dict(link)
    # 友链图片
    data['image'] = getImageURL(link.image) if link.image else None
    # 返回结果
    return data


# 添加友链
def LinkAdd():
    # 表单验证
    form = LinkForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 友链图片
    image = form.image.data
    if image:
        form.image.data = saveImage(image, "link")

    # 表单数据赋值给对象
    link = Link(**form.data)
    link.create_user = uid()
    # 插入数据
    link.save()
    # 返回结果
    return R.ok(msg="添加成功")


# 更新友链
def LinkUpdate():
    # 表单验证
    form = LinkForm(request.form)
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
    link = Link.query.filter(and_(Link.id == id, Link.is_delete == 0)).first()
    # 查询结果判空
    if not link:
        return R.failed("记录不存在")

    # 友链图片
    image = form.image.data
    if image:
        form.image.data = saveImage(image, "link")

    # 更新数据
    result = Link.query.filter_by(id=id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 删除友链
def LinkDelete(link_id):
    # 记录ID为空判断
    if not link_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = link_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            link = Link.query.filter(and_(Link.id == int(vId), Link.is_delete == 0)).first()
            # 查询结果判空
            if not link:
                return R.failed("记录不存在")
            # 设置删除标识
            link.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 设置状态
def LinkStatus():
    # 表单验证
    form = LinkStatusForm(request.form)
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
    link = Link.query.filter(and_(Link.id == id, Link.is_delete == 0)).first()
    # 查询结果判空
    if not link:
        return R.failed("记录不存在")

    # 更新记录
    result = link.query.filter_by(id=id).update({
        "status": status
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("设置失败")
    # 返回结果
    return R.ok(msg="设置成功")
