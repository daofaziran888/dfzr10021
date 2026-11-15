"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class CampEntry(BaseModel):
    """研学营地明细结构。"""

    field_0: str | None = None  # 营地编号
    field_1: str | None = None  # 营地名称
    field_2: str | None = None  # 所在区域
    field_3: str | None = None  # 占地面积
    field_4: str | None = None  # 容纳人数
    field_5: str | None = None  # 海拔高度
    field_6: str | None = None  # 运营状态
    field_7: str | None = None  # 营地特色

class SeasonEntry(BaseModel):
    """研学营期明细结构。"""

    field_0: str | None = None  # 营期编号
    field_1: str | None = None  # 营期主题
    field_2: str | None = None  # 目标人群
    field_3: str | None = None  # 计划人数
    field_4: str | None = None  # 开营日期
    field_5: str | None = None  # 结营日期
    field_6: str | None = None  # 策划人员
    field_7: str | None = None  # 营期状态

class TeacherEntry(BaseModel):
    """研学导师明细结构。"""

    field_0: str | None = None  # 导师编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 专业领域
    field_3: str | None = None  # 资质证书
    field_4: str | None = None  # 从业年限
    field_5: str | None = None  # 擅长课程
    field_6: str | None = None  # 可调配时段
    field_7: str | None = None  # 调配状态

class CourseEntry(BaseModel):
    """研学课程明细结构。"""

    field_0: str | None = None  # 课程编号
    field_1: str | None = None  # 课程名称
    field_2: str | None = None  # 课程类型
    field_3: str | None = None  # 适用年龄
    field_4: str | None = None  # 课程时长
    field_5: str | None = None  # 所需物资
    field_6: str | None = None  # 户外比例
    field_7: str | None = None  # 课程状态

class MaterialEntry(BaseModel):
    """研学物资明细结构。"""

    field_0: str | None = None  # 物资编号
    field_1: str | None = None  # 物资名称
    field_2: str | None = None  # 物资类别
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 当前数量
    field_5: str | None = None  # 安全余量
    field_6: str | None = None  # 存放地点
    field_7: str | None = None  # 物资状态

class StudentEntry(BaseModel):
    """参营学员明细结构。"""

    field_0: str | None = None  # 学员编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 年龄
    field_3: str | None = None  # 所属学校
    field_4: str | None = None  # 报名营期
    field_5: str | None = None  # 紧急联系人
    field_6: str | None = None  # 特殊备注
    field_7: str | None = None  # 接待状态

class AccommodationEntry(BaseModel):
    """住宿单元明细结构。"""

    field_0: str | None = None  # 房间编号
    field_1: str | None = None  # 房间类型
    field_2: str | None = None  # 所在区域
    field_3: str | None = None  # 容纳人数
    field_4: str | None = None  # 当前入住
    field_5: str | None = None  # 设施配置
    field_6: str | None = None  # 清洁记录
    field_7: str | None = None  # 房间状态

class DiningEntry(BaseModel):
    """供餐计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 供餐日期
    field_2: str | None = None  # 餐次类型
    field_3: str | None = None  # 用餐人数
    field_4: str | None = None  # 菜单名称
    field_5: str | None = None  # 主厨人员
    field_6: str | None = None  # 食材清单
    field_7: str | None = None  # 供餐状态

class OutdoorEntry(BaseModel):
    """户外路线明细结构。"""

    field_0: str | None = None  # 路线编号
    field_1: str | None = None  # 路线名称
    field_2: str | None = None  # 路线类型
    field_3: str | None = None  # 全程距离
    field_4: str | None = None  # 预计耗时
    field_5: str | None = None  # 难度等级
    field_6: str | None = None  # 必需装备
    field_7: str | None = None  # 路线状态

class ScheduleEntry(BaseModel):
    """每日日程明细结构。"""

    field_0: str | None = None  # 日程编号
    field_1: str | None = None  # 所属营期
    field_2: str | None = None  # 日程日期
    field_3: str | None = None  # 上午安排
    field_4: str | None = None  # 下午安排
    field_5: str | None = None  # 晚间安排
    field_6: str | None = None  # 执行人
    field_7: str | None = None  # 日程状态

class ObservationEntry(BaseModel):
    """观察记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 观察地点
    field_2: str | None = None  # 观察日期
    field_3: str | None = None  # 物种名称
    field_4: str | None = None  # 观察数量
    field_5: str | None = None  # 行为描述
    field_6: str | None = None  # 记录人员
    field_7: str | None = None  # 记录状态

class SafetyEntry(BaseModel):
    """安全预案明细结构。"""

    field_0: str | None = None  # 预案编号
    field_1: str | None = None  # 预案类型
    field_2: str | None = None  # 适用场景
    field_3: str | None = None  # 响应级别
    field_4: str | None = None  # 责任人
    field_5: str | None = None  # 演练日期
    field_6: str | None = None  # 修订日期
    field_7: str | None = None  # 预案状态

class FirstaidEntry(BaseModel):
    """救护记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 伤患姓名
    field_2: str | None = None  # 伤情描述
    field_3: str | None = None  # 处理措施
    field_4: str | None = None  # 处理人员
    field_5: str | None = None  # 发生时间
    field_6: str | None = None  # 是否送医
    field_7: str | None = None  # 处理状态

class TransportEntry(BaseModel):
    """车辆安排明细结构。"""

    field_0: str | None = None  # 安排编号
    field_1: str | None = None  # 车辆牌号
    field_2: str | None = None  # 车辆类型
    field_3: str | None = None  # 驾驶员
    field_4: str | None = None  # 出发地点
    field_5: str | None = None  # 到达地点
    field_6: str | None = None  # 出发时间
    field_7: str | None = None  # 乘车人数

class FeedbackEntry(BaseModel):
    """反馈记录明细结构。"""

    field_0: str | None = None  # 反馈编号
    field_1: str | None = None  # 反馈人
    field_2: str | None = None  # 关联学员
    field_3: str | None = None  # 反馈类型
    field_4: str | None = None  # 反馈内容
    field_5: str | None = None  # 处理人
    field_6: str | None = None  # 处理日期
    field_7: str | None = None  # 反馈状态

class EvaluationEntry(BaseModel):
    """评价记录明细结构。"""

    field_0: str | None = None  # 评价编号
    field_1: str | None = None  # 所属营期
    field_2: str | None = None  # 评价维度
    field_3: str | None = None  # 评价得分
    field_4: str | None = None  # 评价人
    field_5: str | None = None  # 评价日期
    field_6: str | None = None  # 改进建议
    field_7: str | None = None  # 评价状态

class PhotoEntry(BaseModel):
    """活动影像明细结构。"""

    field_0: str | None = None  # 影像编号
    field_1: str | None = None  # 所属营期
    field_2: str | None = None  # 拍摄日期
    field_3: str | None = None  # 拍摄地点
    field_4: str | None = None  # 影像类型
    field_5: str | None = None  # 拍摄人员
    field_6: str | None = None  # 存储路径
    field_7: str | None = None  # 影像状态
