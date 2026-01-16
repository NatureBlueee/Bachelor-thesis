# TASK-008: 修复文档路径引用

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-008-fix-doc-paths.md`
> 任务ID：TASK-008
> Beads 任务ID：`[TBD]`
> 任务标题：修复文档路径引用
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：0.5h
> 创建日期：2026-01-15
> 优先级：P2（改善质量）

---

## 1. 任务目标

* 做什么：修复 `MULTI_AGENT_DESIGN.md` 中仍指向 `academic_network/` 的路径引用
* 为什么做：项目已重命名为 `research_network/`，文档路径需要同步更新
* 涉及文件：
  - `research_network/MULTI_AGENT_DESIGN.md`

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（文档修复）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **无依赖**：可以立即启动
* 下游任务：无

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：文档中所有路径引用指向 `research_network/`
- [ ] AC2：无 `academic_network/` 的残留引用

## 4. 实施方案

* 改动点列表：
  - `research_network/MULTI_AGENT_DESIGN.md`
* 方案：全局替换 `academic_network/` 为 `research_network/`

## 5. 测试

- [ ] grep 检查无旧路径引用

## 6. 风险与回滚

* 风险：低
* 回滚：git revert
