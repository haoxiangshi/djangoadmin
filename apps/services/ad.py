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
from apps.constants.constants import AD_TYPE_LIST
from apps.constants.message import PAGE_LIMIT
from apps.forms.ad import AdForm, AdStatusForm
from apps.models.ad import Ad
from apps.models.ad_sort import AdSort
from config.env import FLASK_IMAGE_URL
from extends import db
from utils import R, regular
from utils.utils import getImageURL, saveImage, uid, saveEditContent


# 查询广告分页数据
def AdList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = Ad.query.filter(Ad.is_delete == 0)
    # 广告标题
    title = request.args.get('title')
    if title:
        query = query.filter(Ad.title.like('%' + title + '%'))
    # 广告类型：1-图片 2-文字 3-视频 4-推荐
    type = request.args.get('type')
    if type:
        query = query.filter(Ad.type == type)
    # 广告状态
    status = request.args.get('status')
    if status:
        query = query.filter(Ad.status == status)
    # 排序
    query = query.order_by(Ad.sort.desc())
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
            # 广告类型
            data['type_name'] = AD_TYPE_LIST.get(item.type)
            # 广告封面
            data['cover'] = getImageURL(item.cover) if item.cover else None
            # 查询广告位信息
            ad_sort = AdSort.query.filter(and_(AdSort.id == item.sort_id, AdSort.is_delete == 0)).first()
            # 广告位描述
            data['sort_desc'] = ad_sort.name + "=>" + str(ad_sort.loc_id) if ad_sort else None
            # 开始时间
            data['start_time'] = str(item.start_time.strftime('%Y-%m-%d %H:%M:%S')) if item.start_time else None
            # 结束时间
            data['end_time'] = str(item.end_time.strftime('%Y-%m-%d %H:%M:%S')) if item.end_time else None
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据广告ID查询详情
def AdDetail(ad_id):
    # 根据广告ID查询信息
    ad = Ad.query.filter(and_(Ad.id == ad_id, Ad.is_delete == 0)).first()
    # 查询结果为空判断
    if not ad:
        return None
    # 对象转字典
    data = utils.load2dict(ad)
    # 广告类型描述
    data['type_name'] = AD_TYPE_LIST.get(ad.type)
    # 广告封面
    data['cover'] = getImageURL(ad.cover) if ad.cover else ""
    # 开始时间
    data['start_time'] = str(ad.start_time.strftime('%Y-%m-%d %H:%M:%S')) if ad.start_time else None
    # 结束时间
    data['end_time'] = str(ad.end_time.strftime('%Y-%m-%d %H:%M:%S')) if ad.end_time else None
    # 返回结果
    return data


# 添加广告
def AdAdd():
    # 表单验证
    form = AdForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 广告封面
    cover = form.cover.data
    if form.type.data == 1 and cover:
        cover = saveImage(cover, "ad")
    else:
        cover = None
    # 参数赋值
    form.cover.data = cover

    # 表单数据赋值给对象
    ad = Ad(**form.data)
    ad.create_user = uid()
    # 插入数据
    ad.save()
    # 返回结果
    return R.ok(msg="添加成功")


# 更新广告
def AdUpdate():
    # 表单验证
    form = AdForm(request.form)
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
    ad = Ad.query.filter(and_(Ad.id == id, Ad.is_delete == 0)).first()
    # 查询结果判空
    if not ad:
        return R.failed("记录不存在")

    # 广告封面
    cover = form.cover.data
    if form.type.data == 1 and cover:
        cover = saveImage(cover, "ad")
    else:
        cover = None
    # 参数赋值
    form.cover.data = cover
    # 更新记录
    result = Ad.query.filter_by(id=id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 删除广告
def AdDelete(ad_id):
    # 记录ID为空判断
    if not ad_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = ad_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            ad = Ad.query.filter(and_(Ad.id == int(vId), Ad.is_delete == 0)).first()
            # 查询结果判空
            if not ad:
                return R.failed("记录不存在")
            # 设置删除标识
            ad.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 设置状态
def AdStatus():
    # 表单验证
    form = AdStatusForm(request.form)
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
    ad = Ad.query.filter(and_(Ad.id == id, Ad.is_delete == 0)).first()
    # 查询结果判空
    if not ad:
        return R.failed("记录不存在")

    # 更新记录
    result = Ad.query.filter_by(id=id).update({
        "status": status
    })
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("设置失败")
    # 返回结果
    return R.ok(msg="设置成功")
