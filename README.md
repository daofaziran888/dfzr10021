# 生态研学营地运营综合管理平台

面向自然生态研学营地的营期策划、师资调配、物资筹备、学员接待、户外活动执行与安全应急的一体化管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 营地档案 | `camp` | 研学营地 | 营地编号、营地名称、所在区域 |
| 营期策划 | `season` | 研学营期 | 营期编号、营期主题、目标人群 |
| 师资调配 | `teacher` | 研学导师 | 导师编号、姓名、专业领域 |
| 课程设计 | `course` | 研学课程 | 课程编号、课程名称、课程类型 |
| 物资筹备 | `material` | 研学物资 | 物资编号、物资名称、物资类别 |
| 学员接待 | `student` | 参营学员 | 学员编号、姓名、年龄 |
| 住宿安排 | `accommodation` | 住宿单元 | 房间编号、房间类型、所在区域 |
| 餐饮管理 | `dining` | 供餐计划 | 计划编号、供餐日期、餐次类型 |
| 户外活动 | `outdoor` | 户外路线 | 路线编号、路线名称、路线类型 |
| 日程执行 | `schedule` | 每日日程 | 日程编号、所属营期、日程日期 |
| 自然观察 | `observation` | 观察记录 | 记录编号、观察地点、观察日期 |
| 安全应急 | `safety` | 安全预案 | 预案编号、预案类型、适用场景 |
| 医疗救护 | `firstaid` | 救护记录 | 记录编号、伤患姓名、伤情描述 |
| 交通调度 | `transport` | 车辆安排 | 安排编号、车辆牌号、车辆类型 |
| 家长反馈 | `feedback` | 反馈记录 | 反馈编号、反馈人、关联学员 |
| 营期评价 | `evaluation` | 评价记录 | 评价编号、所属营期、评价维度 |
| 影像记录 | `photo` | 活动影像 | 影像编号、所属营期、拍摄日期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
