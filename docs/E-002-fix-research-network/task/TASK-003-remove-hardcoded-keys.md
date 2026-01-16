# TASK-003: 移除硬编码 API Key

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-003-remove-hardcoded-keys.md`
> 任务ID：TASK-003
> Beads 任务ID：`[TBD]`
> 任务标题：移除硬编码 API Key
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：1h
> 创建日期：2026-01-15
> 优先级：P0（安全问题）

---

## 1. 任务目标

* 做什么：移除 `start.sh` 和 `mods/memory_system.py` 中的硬编码 API Key
* 为什么做：安全风险，API Key 不应提交到代码仓库
* 涉及文件：
  - `research_network/start.sh`
  - `research_network/mods/memory_system.py`

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（安全修复）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **无依赖**：可以立即启动
* 下游任务：TASK-005（start.sh 路径修复可并行）

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：代码中不包含任何硬编码的 API Key
- [ ] AC2：改用环境变量或 .env 文件读取
- [ ] AC3：添加 .env.example 示例文件

## 4. 实施方案

* 改动点列表：
  - `research_network/start.sh`：移除 export API_KEY=xxx，改为检查环境变量
  - `research_network/mods/memory_system.py`：使用 os.getenv() 读取
  - 新增 `research_network/.env.example`：提供配置模板

## 5. 测试

- [ ] grep 检查无硬编码 key
- [ ] 环境变量读取测试

## 6. 风险与回滚

* 风险：现有用户需要手动配置环境变量
* 回滚：git revert
