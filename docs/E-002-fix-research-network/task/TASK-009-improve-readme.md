# TASK-009: 完善 README 环境配置说明

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-009-improve-readme.md`
> 任务ID：TASK-009
> Beads 任务ID：`[TBD]`
> 任务标题：完善 README 环境配置说明
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：0.5h
> 创建日期：2026-01-15
> 优先级：P2（改善质量）

---

## 1. 任务目标

* 做什么：完善 README 中的环境配置说明
* 为什么做：当前 README 缺少详细的环境配置步骤，新用户难以上手
* 涉及文件：
  - `research_network/README.md`

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（文档改善）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **接口依赖**：TASK-002（需要知道最终的依赖列表）
  - **接口依赖**：TASK-003（需要知道环境变量配置方式）
* 下游任务：无

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：README 包含完整的环境配置步骤
- [ ] AC2：README 包含所需环境变量列表
- [ ] AC3：新用户按 README 可成功运行项目

## 4. 实施方案

* 改动点列表：
  - `research_network/README.md`
* 添加内容：
  - 环境要求（Python 版本等）
  - 依赖安装步骤
  - 环境变量配置
  - 快速启动命令

## 5. 测试

- [ ] 按 README 步骤验证可运行

## 6. 风险与回滚

* 风险：低
* 回滚：git revert
