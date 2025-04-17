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
from apps.constants.constants import NOTICE_SOURCE_LIST
from apps.constants.message import PAGE_LIMIT
from apps.forms.notice import NoticeForm
from apps.models.notice import Notice
from config.env import FLASK_IMAGE_URL
from extends import db
from utils import R, regular
from utils.utils import uid, saveEditContent


# 查询通知公告分页数据
def NoticeList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = Notice.query.filter(Notice.is_delete == 0)
    # 通知公告标题
    title = request.args.get('title')
    if title:
        query = query.filter(Notice.title.like('%' + title + '%'))
    # 通知来源：1官方平台 2开源中国 3CSDN官方 4新浪微博
    source = request.args.get('source')
    if source:
        query = query.filter(Notice.source == source)
    # 通知状态：1-正常 2-停用
    status = request.args.get('status')
    if status:
        query = query.filter(Notice.status == status)
    # 排序
    query = query.order_by(Notice.id.desc())
    # 记录总数
    count = query.count()
    # 分页查询
    notice_list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(notice_list) > 0:
        for item in notice_list:
            # 对象转字典
            data = utils.load2dict(item)
            # 通知来源描述
            data['source_name'] = NOTICE_SOURCE_LIST.get(item.source)
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据通知ID查询详情
def NoticeDetail(notice_id):
    # 根据ID查询通知公告
    notice = Notice.query.filter(and_(Notice.id == notice_id, Notice.is_delete == 0)).first()
    # 查询结果判空
    if not notice:
        return None
    # 对象转字典
    data = utils.load2dict(notice)
    # 富文本内容
    content = notice.content.replace("[IMG_URL]", FLASK_IMAGE_URL)
    data['content'] = content
    # 通知来源
    data['source_name'] = NOTICE_SOURCE_LIST.get(notice.source)
    # 返回结果
    return data


# 添加通知公告
def NoticeAdd():
    # 表单验证
    form = NoticeForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 通知标题
    title = form.title.data
    # 通知内容
    content = form.content.data
    # 处理富文本内容
    form.content.data = saveEditContent(content, title, "notice")

    # 表单数据赋值给对象
    notice = Notice(**form.data)
    notice.create_user = uid()
    # 插入数据
    notice.save()
    # 返回结果
    return R.ok(msg="添加成功")


# 更新通知公告
def NoticeUpdate():
    # 表单验证
    form = NoticeForm(request.form)
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
    notice = Notice.query.filter(and_(Notice.id == id, Notice.is_delete == 0)).first()
    # 查询结果判空
    if not notice:
        return R.failed("记录不存在")

    # 通知标题
    title = form.title.data
    # 通知内容
    content = form.content.data
    # 处理富文本内容
    form.content.data = saveEditContent(content, title, "notice")
    # 更新记录
    result = Notice.query.filter_by(id=id).update(form.data)
    # 提交数据
    db.session.commit()
    if not result:
        return R.failed("更新失败")
    # 返回结果
    return R.ok(msg="更新成功")


# 删除通知公告
def NoticeDelete(notice_id):
    # 记录ID为空判断
    if not notice_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = notice_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            user = Notice.query.filter(and_(Notice.id == int(vId), Notice.is_delete == 0)).first()
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
