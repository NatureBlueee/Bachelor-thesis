# TASK-007: 修复日志语言（拼音改中文/英文）

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-007-fix-log-language.md`
> 任务ID：TASK-007
> Beads 任务ID：`[TBD]`
> 任务标题：修复日志语言
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：0.5h
> 创建日期：2026-01-15
> 优先级：P2（改善质量）

---

## 1. 任务目标

* 做什么：将日志中的拼音改为中文或英文
* 为什么做：拼音日志可读性差，不利于调试
* 涉及文件：
  - `research_network/mods/*.py`
  - `research_network/tools/*.py`

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（代码质量改善）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **无依赖**：可以立即启动
* 下游任务：无

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：日志中不包含拼音
- [ ] AC2：日志使用统一的语言（中文或英文）

## 4. 实施方案

* 改动点列表：
  - 搜索所有 `logger.` 调用
  - 将拼音替换为中文或英文

## 5. 测试

- [ ] grep 检查无拼音日志
- [ ] 日志输出可读性检查

## 6. 风险与回滚

* 风险：低
* 回滚：git revert
