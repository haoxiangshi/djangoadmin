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
from apps.constants.constants import AD_SORT_PLATFORM_LIST
from apps.constants.message import PAGE_LIMIT
from apps.forms.ad_sort import AdSortForm
from apps.models.ad_sort import AdSort
from apps.models.item import Item
from apps.models.item_cate import ItemCate
from extends import db
from utils import R, regular
from utils.utils import uid


# 获取广告位分页数据
def AdSortList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = AdSort.query.filter(AdSort.is_delete == 0)
    # 名称
    name = request.args.get('name')
    if name:
        query = query.filter(AdSort.name.like('%' + name + '%'))
    # 投放平台：1PC站 2WAP站 3微信小程序 4APP应用
    platform = request.args.get('platform')
    if platform:
        query = query.filter(AdSort.platform == platform)
    # 栏目状态筛选
    status = request.args.get('status')
    if status:
        query = query.filter(AdSort.status == status)
    # 排序
    query = query.order_by(AdSort.sort.asc())
    # 记录总数
    count = query.count()
    # 分页查询
    list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(list) > 0:
        for v in list:
            # 对象转字典
            data = utils.load2dict(v)
            # 投放平台
            data['platform_name'] = AD_SORT_PLATFORM_LIST.get(v.platform)
            # 站点信息
            item_info = Item.query.filter(and_(Item.id == v.item_id, Item.is_delete == 0)).first()
            data['item_name'] = item_info.name if item_info else None
            # 栏目信息
            cate_info = ItemCate.query.filter(and_(ItemCate.id == v.cate_id, ItemCate.is_delete == 0)).first()
            data['cate_name'] = cate_info.name if cate_info else None
            # 创建时间
            data['create_time'] = str(v.create_time.strftime('%Y-%m-%d %H:%M:%S')) if v.create_time else None
            # 更新时间
            data['update_time'] = str(v.update_time.strftime('%Y-%m-%d %H:%M:%S')) if v.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据ID查询广告位详情
def AdSortDetail(adsort_id):
    # 根据ID查询广告位
    adsort = AdSort.query.filter(and_(AdSort.id == adsort_id, AdSort.is_delete == 0)).first()
    # 查询结果为空判断
    if not adsort:
        return None
    # 对象转字典
    data = utils.load2dict(adsort)
    # 返回结果
    return data


# 添加广告位
def AdSortAdd():
    # 表单验证
    form = AdSortForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 表单数据赋值给对象
    adsort = AdSort(**form.data)
    adsort.create_user = uid()
    # 插入数据
    adsort.save()
    # 返回结果
    return R.ok(msg="添加成功")


# 更新广告位
def AdSortUpdate():
    # 表单验证
    form = AdSortForm(request.form)
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
    adsort = AdSort.query.filter(and_(AdSort.id == id, AdSort.is_delete == 0)).first()
    # 查询结果判空
    if not adsort:
        return R.failed("记录不存在")
    result = AdSort.query.filter_by(id=id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 删除广告位
def AdSortDelete(adsort_id):
    # 记录ID为空判断
    if not adsort_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = adsort_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            adsort = AdSort.query.filter(and_(AdSort.id == int(vId), AdSort.is_delete == 0)).first()
            # 查询结果判空
            if not adsort:
                return R.failed("记录不存在")
            # 设置删除标识
            adsort.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 查询全部广告位列表
def GetAdSortList():
    # 查询全部广告位列表
    list = AdSort.query.filter(AdSort.is_delete == 0).all()
    # 实例化广告位对象列表
    sortList = []
    if list:
        for v in list:
            item = {
                'id': v.id,
                'description': v.description + "=>" + str(v.loc_id)
            }
            # 加入列表
            sortList.append(item)
    # 返回结果
    return sortList
