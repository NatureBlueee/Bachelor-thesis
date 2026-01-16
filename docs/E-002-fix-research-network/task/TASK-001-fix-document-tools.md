# TASK-001: 修复 DocumentTools 类引用

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-001-fix-document-tools.md`
> 任务ID：TASK-001
> Beads 任务ID：`[TBD]`
> 任务标题：修复 DocumentTools 类引用
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：0.5h
> 创建日期：2026-01-15
> 优先级：P0（阻塞运行）

---

## 1. 任务目标

* 做什么：修复 `mods/document_tools_sync.py` 中引用不存在的 `DocumentTools` 类的问题
* 为什么做：当前代码无法运行，`from tools.document_tools import DocumentTools` 会报 ImportError
* 不做什么：不重构整体架构，只修复引用问题

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（技术债修复）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **无依赖**：可以立即启动
* 下游任务：TASK-004（工具重复清理依赖此任务确认正确的工具实现）

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：`from mods.document_tools_sync import *` 不报 ImportError
- [ ] AC2：同步工具函数可正常调用

## 4. 实施方案

* 改动点列表：
  - `research_network/mods/document_tools_sync.py`
* 方案选择：
  - 方案A：创建缺失的 `DocumentTools` 类
  - 方案B：修改 import 路径指向正确的实现
  - 推荐方案B（复用现有代码）

## 5. 测试

- [ ] import 测试通过
- [ ] 基本功能调用测试

## 6. 风险与回滚

* 风险：低
* 回滚：git revert
