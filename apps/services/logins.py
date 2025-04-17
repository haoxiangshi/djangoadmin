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

from apps.forms.login import LoginForm
from apps.models.user import User
from utils import regular, R, md5, redis

from utils.jwts import create_token


# 系统登录
def Login():
    # 表单验证
    form = LoginForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)
    # 登录账号
    username = form.username.data
    # 登录密码
    password = form.password.data
    # 验证码
    image_code = redis.get(form.idKey.data)
    # 验证码正确性校验
    if not image_code or image_code.lower() != form.captcha.data.lower():
        return R.failed("验证码不正确")

    # 根据用户名查询用户信息
    user = User.query.filter(and_(User.username == username, User.is_delete == 0)).first()
    if not user:
        return R.failed("用户不存在")

    # 密码MD5加密
    md5_pwd = md5.getPassword(password)

    # 比对密码是否相同
    if md5_pwd != user.password:
        return R.failed(msg="密码不正确")
    # 生成TOKEN
    access_token = create_token({"userId": user.id})
    # 返回结果
    return R.ok(msg="登录成功", data={"access_token": access_token})
