# 项目计划 PROJ-E-001-v1

> * EPIC_ID：E-001
> * EPIC_DIR：`E-001-fix-multi-agent`
> * 文档状态：ACTIVE
> * 版本：v1
> * 创建人：Proj Agent
> * 创建日期：2025-01-14

---

## 0. 关联信息

* biz-overview：`/docs/_project/biz-overview.md`
* PRD：`../prd/PRD-E-001-v0.md`
* Story：`../story/STORY-001-deep-read.md`
* Tech：`../tech/TECH-E-001-v1.md`

---

## 1. 项目概述

### 1.1 名称与目标

* **Epic 名称**：修复多 Agent 协作系统
* **业务目标**：在黑客松演示多 Agent 协作完成文献深度阅读
* **核心问题**：对话"聊两句就没了"，无法完成多轮协作

### 1.2 成功指标

| 指标 | 目标值 | 当前值 |
|------|--------|--------|
| 多轮对话 | 3+ 轮不中断 | 2 轮后中断 |
| 任务委派可见 | 100% | 0% |
| 结构化笔记输出 | 包含 4 个必要字段 | 无 |

---

## 2. 范围说明

### 2.1 本期纳入

| Story ID | 描述 | 优先级 |
|----------|------|--------|
| STORY-001 | 文献深度阅读与结构化笔记 | Must |

### 2.2 本期不纳入

* PR 创建/合并流程
* 记忆系统（Mem0）
* 自动文献检索（外部 API）

---

## 3. Story → Slice → Task 对齐表

| STORY_ID | SLICE_ID | TASK_ID | 描述 | 本期纳入 | 验收责任人 |
|----------|----------|---------|------|----------|------------|
| STORY-001 | NO_SLICE | TASK-001 | 验证系统启动和基本对话 | ✅ | 用户 |
| STORY-001 | NO_SLICE | TASK-002 | 验证任务委派流程 | ✅ | 用户 |
| STORY-001 | NO_SLICE | TASK-003 | 验证深度阅读输出 | ✅ | 用户 |

> 说明：本 Epic 为修复性质，已完成代码修改，TASK 均为验证任务，无需 SLICE 拆分。

---

## 4. 执行进度表

| TASK_ID | 描述 | 状态 | Owner | 预估 | 阻塞点 |
|---------|------|------|-------|------|--------|
| TASK-001 | 验证系统启动和基本对话 | TODO | 用户 | 10min | 无 |
| TASK-002 | 验证任务委派流程 | TODO | 用户 | 10min | TASK-001 |
| TASK-003 | 验证深度阅读输出 | TODO | 用户 | 15min | TASK-002 |

---

## 5. 资源配置

| 角色 | 人数 | 投入时间 | 备注 |
|------|------|----------|------|
| 用户 | 1 | 35min | 验证测试 |
| AI Agent | - | - | 已完成代码修复 |

---

## 6. 时间计划

* **目标完成日期**：2025-01-14（当天）
* **总预估时间**：35 分钟

| 阶段 | 内容 | 预估 |
|------|------|------|
| 启动验证 | TASK-001 | 10min |
| 委派验证 | TASK-002 | 10min |
| 输出验证 | TASK-003 | 15min |

---

## 7. 任务拆解与优先级

### P0（必须完成）

| TASK_ID | 描述 | 对应 AC |
|---------|------|---------|
| TASK-001 | 验证系统启动和基本对话 | AC1, AC2 |
| TASK-002 | 验证任务委派流程 | AC3 |
| TASK-003 | 验证深度阅读输出 | AC4 |

### P1（本期不纳入）

无

### P2（本期不纳入）

无

---

## 8. 里程碑与完成定义

### M1：系统可运行（验证 TASK-001）

**完成定义**：
- [ ] `openagents start network.yaml` 启动成功
- [ ] 打开 http://localhost:8700/studio 看到 UI
- [ ] 发送消息能收到 academic-partner 回复
- [ ] 连续对话 3+ 轮不中断

### M2：任务委派可见（验证 TASK-002）

**完成定义**：
- [ ] 请求"搜索 AI literacy 相关文献"
- [ ] 能看到委派给 literature-agent 的过程
- [ ] literature-agent 能调用 search_literature 工具
- [ ] 结果能返回给 academic-partner

### M3：深度阅读输出（验证 TASK-003）

**完成定义**：
- [ ] 请求深度阅读某文献
- [ ] 输出包含"基本信息"
- [ ] 输出包含"方法论"
- [ ] 输出包含"关键发现"
- [ ] 输出包含"RQ关联"

---

## 9. Gate 检查点

### Gate A（进入实现前）- ✅ 已通过

- [x] PRD-E-001-v0.md 存在
- [x] STORY-001-deep-read.md 存在
- [x] TECH-E-001-v1.md 存在
- [ ] UI 证据：OpenAgents Studio UI（待验证）

### Gate B（P0 进入 DONE 前）

- [ ] 对应 AC 的测试用例与结果
- [ ] 至少一次"真数据真流程"的端到端验证
- [ ] 回滚方案：恢复原 academic_partner.yaml

### Gate C（方向偏差时）

* 触发条件：发现"不是想要的"或关键分叉决策改变
* 必须动作：PRD/TECH/PROJ 升版本并记录变更点

---

## 10. 风险与预案

| 风险 | 概率 | 影响 | 预案 |
|------|------|------|------|
| LLM 响应超时 | 中 | 高 | 增加 agent_timeout 配置 |
| 文献内容过长 | 中 | 中 | read_literature 已限制 3000 字符预览 |
| OpenAgents 框架 bug | 低 | 高 | 回退到已知稳定版本 |

---

## 11. 验证命令

```bash
# 启动系统
cd /Users/nature/个人项目/Bachelor-thesis/academic_network
openagents start network.yaml

# 访问 Studio UI
open http://localhost:8700/studio
```

---

## 12. 变更记录

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| v1 | 2025-01-14 | Proj Agent | 初版 |
