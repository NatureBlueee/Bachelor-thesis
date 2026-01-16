# TASK-004: 清理重复的工具文件

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-004-cleanup-duplicate-tools.md`
> 任务ID：TASK-004
> Beads 任务ID：`[TBD]`
> 任务标题：清理重复的工具文件
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：1h
> 创建日期：2026-01-15
> 优先级：P1（影响稳定性）

---

## 1. 任务目标

* 做什么：合并 `tools/memory_tools.py` 与 `mods/memory_tools_sync.py` 的重复功能
* 为什么做：两个文件功能重复，维护成本高，容易出现不一致
* 涉及文件：
  - `research_network/tools/memory_tools.py`
  - `research_network/mods/memory_tools_sync.py`

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（技术债清理）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **硬依赖**：TASK-001（需要先确认正确的工具实现模式）
* 下游任务：TASK-006（Agent YAML 路径修复依赖此任务）

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：只保留一份 memory_tools 实现
- [ ] AC2：所有调用方更新为使用统一的实现
- [ ] AC3：功能测试通过

## 4. 实施方案

* 方案：保留 `mods/memory_tools_sync.py`（同步版本），删除 `tools/memory_tools.py`
* 改动点列表：
  - 删除 `tools/memory_tools.py`
  - 更新所有 import 引用

## 5. 测试

- [ ] 功能回归测试
- [ ] import 路径测试

## 6. 风险与回滚

* 风险：可能遗漏调用方
* 回滚：git revert
