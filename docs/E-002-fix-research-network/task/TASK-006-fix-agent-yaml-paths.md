# TASK-006: 修复 Agent YAML 工具路径

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-006-fix-agent-yaml-paths.md`
> 任务ID：TASK-006
> Beads 任务ID：`[TBD]`
> 任务标题：修复 Agent YAML 工具路径
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：1h
> 创建日期：2026-01-15
> 优先级：P1（影响稳定性）

---

## 1. 任务目标

* 做什么：检查并修复 Agent YAML 文件中的工具路径引用
* 为什么做：工具路径可能不一致，导致 Agent 无法正确加载工具
* 涉及文件：
  - `research_network/agents/*.yaml`

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（配置修复）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **硬依赖**：TASK-004（需要先确定最终的工具文件位置）
* 下游任务：无

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：所有 Agent YAML 中的工具路径指向正确的实现文件
- [ ] AC2：Agent 启动时工具加载无报错

## 4. 实施方案

* 改动点列表：
  - `research_network/agents/*.yaml` 中的 `tools.implementation` 字段
* 检查项：
  - 路径格式是否正确（module.function）
  - 目标函数是否存在

## 5. 测试

- [ ] Agent 启动测试
- [ ] 工具调用测试

## 6. 风险与回滚

* 风险：低
* 回滚：git revert
