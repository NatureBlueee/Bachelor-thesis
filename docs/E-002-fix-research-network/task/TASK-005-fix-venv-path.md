# TASK-005: 修复 start.sh 虚拟环境路径

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-005-fix-venv-path.md`
> 任务ID：TASK-005
> Beads 任务ID：`[TBD]`
> 任务标题：修复 start.sh 虚拟环境路径
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：0.5h
> 创建日期：2026-01-15
> 优先级：P1（影响稳定性）

---

## 1. 任务目标

* 做什么：修复 `start.sh` 中硬编码的虚拟环境路径
* 为什么做：当前路径硬编码为特定用户目录，其他用户无法使用
* 涉及文件：
  - `research_network/start.sh`

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（可用性修复）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **无依赖**：可以立即启动（与 TASK-003 可并行，都修改 start.sh 但不同部分）
* 下游任务：无

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：使用相对路径或自动检测虚拟环境
- [ ] AC2：在不同机器上可正常运行

## 4. 实施方案

* 改动点列表：
  - `research_network/start.sh`
* 方案：
  ```bash
  # 改为相对路径
  SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
  source "$SCRIPT_DIR/venv/bin/activate"
  ```

## 5. 测试

- [ ] 在不同目录下运行测试
- [ ] 虚拟环境激活测试

## 6. 风险与回滚

* 风险：低
* 回滚：git revert
