"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import camp as router_camp
from app.routers import season as router_season
from app.routers import teacher as router_teacher
from app.routers import course as router_course
from app.routers import material as router_material
from app.routers import student as router_student
from app.routers import accommodation as router_accommodation
from app.routers import dining as router_dining
from app.routers import outdoor as router_outdoor
from app.routers import schedule as router_schedule
from app.routers import observation as router_observation
from app.routers import safety as router_safety
from app.routers import firstaid as router_firstaid
from app.routers import transport as router_transport
from app.routers import feedback as router_feedback
from app.routers import evaluation as router_evaluation
from app.routers import photo as router_photo

ROUTERS = [router_camp, router_season, router_teacher, router_course, router_material, router_student, router_accommodation, router_dining, router_outdoor, router_schedule, router_observation, router_safety, router_firstaid, router_transport, router_feedback, router_evaluation, router_photo]
