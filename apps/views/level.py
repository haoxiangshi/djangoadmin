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


from apps.middleware.check_permission import check_permission
from apps.services import level
from apps.views import level_blue

from config.env import FLASK_DEMO
from utils import R


# 查询职级分页数据
@check_permission("sys:level:list")
@level_blue.route('/list', methods=["GET"])
def list():
    # 调用查询职级分页数据服务方法
    result = level.LevelList()
    # 返回结果
    return result


# 查询职级详情
@level_blue.route('/detail/<int:id>', methods=["GET"])
@check_permission("sys:level:detail")
def detail(id):
    # 调用查询职级详情服务方法
    data = level.LevelDetail(id)
    # 返回结果
    return R.ok(data=data)


# 添加职级
@level_blue.route('/add', methods=["POST"])
@check_permission("sys:level:add")
def add():
    if FLASK_DEMO:
        return R.failed("演示环境，暂无操作权限")
    # 调用添加职级服务
    result = level.LevelAdd()
    # 返回结果
    return result


# 更新职级
@level_blue.route('/update', methods=["PUT"])
@check_permission("sys:level:update")
def update():
    if FLASK_DEMO:
        return R.failed("演示环境，暂无操作权限")
    # 调用更新职级服务方法
    result = level.LevelUpdate()
    # 返回结果
    return result


# 删除职级
@level_blue.route('/delete/<string:id>', methods=["DELETE"])
@check_permission("sys:level:delete")
def delete(id):
    if FLASK_DEMO:
        return R.failed("演示环境，暂无操作权限")
    # 调用删除职级服务方法
    result = level.LevelDelete(id)
    # 返回结果
    return result


# 设置职级状态
@level_blue.route('/status', methods=["PUT"])
@check_permission("sys:level:status")
def status():
    if FLASK_DEMO:
        return R.failed("演示环境，暂无操作权限")
    # 调用设置职级状态服务方法
    result = level.LevelStatus()
    # 返回结果
    return result


# 导入Excel
@level_blue.route('/import', methods=["POST"])
@check_permission("sys:level:import")
def imports():
    # 预留的接口
    if FLASK_DEMO:
        return R.failed("演示环境，暂无操作权限")
    # 调用导入Excel方法
    result = level.LevelImport()
    # 返回结果
    return result


# 导出Excel
@level_blue.route('/export', methods=["POST"])
@check_permission("sys:level:export")
def export():
    # 预留的接口
    if FLASK_DEMO:
        return R.failed("演示环境，暂无操作权限")
    # 调用导出Excel方法
    result = level.LevelExport()
    # 返回结果
    return result


# 获取职级数据列表
@level_blue.route('/getLevelList', methods=["GET"])
def getLevelList():
    # 调用查询职级数据
    result = level.getLevelList()
    # 返回结果
    return R.ok(data=result)
