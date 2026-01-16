# E-002 fix-research-network 执行计划

> 创建时间：2026-01-15 11:47
> Epic：E-002
> 目标：修复 research_network 项目的技术问题

---

## 1. 任务总览

| TASK ID | Beads ID | 标题 | 优先级 | 状态 | 预估 | 依赖 |
|---------|----------|------|--------|------|------|------|
| TASK-001 | Bachelor-thesis-xmc | 修复 DocumentTools 类引用 | P0 | ✅ 已完成 | 0.5h | 无 |
| TASK-002 | Bachelor-thesis-o4t | 补全 requirements.txt 依赖 | P0 | ✅ 已完成 | 0.5h | 无 |
| TASK-003 | Bachelor-thesis-8o8 | 移除硬编码 API Key | P0 | ✅ 已完成 | 1h | 无 |
| TASK-004 | Bachelor-thesis-tnn | 清理重复的工具文件 | P1 | ✅ 已完成 | 1h | TASK-001 |
| TASK-005 | Bachelor-thesis-hua | 修复 start.sh 虚拟环境路径 | P1 | ✅ 已完成 | 0.5h | 无 |
| TASK-006 | Bachelor-thesis-w2f | 修复 Agent YAML 工具路径 | P1 | ✅ 已完成 | 1h | TASK-004 |
| TASK-007 | Bachelor-thesis-dh1 | 修复日志语言 | P2 | ✅ 已完成 | 0.5h | 无 |
| TASK-008 | Bachelor-thesis-05s | 修复文档路径引用 | P2 | ✅ 已完成 | 0.5h | 无 |
| TASK-009 | Bachelor-thesis-xwx | 完善 README 环境配置说明 | P2 | ✅ 已完成 | 0.5h | TASK-002, TASK-003 |

---

## 2. 依赖关系图

```
                    ┌─────────────────────────────────────────┐
                    │           P0 - 阻塞运行                  │
                    └─────────────────────────────────────────┘

    ┌──────────┐         ┌──────────┐         ┌──────────┐
    │ TASK-001 │         │ TASK-002 │         │ TASK-003 │
    │ Document │         │ require- │         │ API Key  │
    │  Tools   │         │ ments.txt│         │  移除    │
    └────┬─────┘         └────┬─────┘         └────┬─────┘
         │                    │                    │
         ▼                    │                    │
                    ┌─────────────────────────────────────────┐
                    │           P1 - 影响稳定性                │
                    └─────────────────────────────────────────┘

    ┌──────────┐         ┌──────────┐
    │ TASK-004 │         │ TASK-005 │
    │ 清理重复 │         │ venv路径 │
    │  工具    │         │  修复    │
    └────┬─────┘         └──────────┘
         │
         ▼
    ┌──────────┐
    │ TASK-006 │
    │ YAML路径 │
    │  修复    │
    └──────────┘

                    ┌─────────────────────────────────────────┐
                    │           P2 - 改善质量                  │
                    └─────────────────────────────────────────┘

    ┌──────────┐         ┌──────────┐         ┌──────────┐
    │ TASK-007 │         │ TASK-008 │         │ TASK-009 │◄──┐
    │ 日志语言 │         │ 文档路径 │         │ README   │   │
    │  修复    │         │  修复    │         │  完善    │   │
    └──────────┘         └──────────┘         └──────────┘   │
                                                    ▲        │
                                                    │        │
                                              TASK-002  TASK-003
```

---

## 3. 推荐执行顺序

### 第一批（立即可并行，无依赖）

```bash
# 可同时启动 6 个任务
bd update Bachelor-thesis-xmc -s doing  # TASK-001
bd update Bachelor-thesis-o4t -s doing  # TASK-002
bd update Bachelor-thesis-8o8 -s doing  # TASK-003
bd update Bachelor-thesis-hua -s doing  # TASK-005
bd update Bachelor-thesis-dh1 -s doing  # TASK-007
bd update Bachelor-thesis-05s -s doing  # TASK-008
```

### 第二批（等 TASK-001 完成）

```bash
bd update Bachelor-thesis-tnn -s doing  # TASK-004（依赖 TASK-001）
```

### 第三批（等 TASK-004 完成）

```bash
bd update Bachelor-thesis-w2f -s doing  # TASK-006（依赖 TASK-004）
```

### 第四批（等 TASK-002 和 TASK-003 完成）

```bash
bd update Bachelor-thesis-xwx -s doing  # TASK-009（依赖 TASK-002, TASK-003）
```

---

## 4. beads 依赖设置命令（已执行）

```bash
# 语法：bd dep add <被阻塞任务> <阻塞它的任务>

# TASK-004 依赖 TASK-001
bd dep add Bachelor-thesis-tnn Bachelor-thesis-xmc

# TASK-006 依赖 TASK-004
bd dep add Bachelor-thesis-w2f Bachelor-thesis-tnn

# TASK-009 依赖 TASK-002
bd dep add Bachelor-thesis-xwx Bachelor-thesis-o4t

# TASK-009 依赖 TASK-003
bd dep add Bachelor-thesis-xwx Bachelor-thesis-8o8
```

---

## 5. 验证命令

```bash
# 查看可立即开始的任务
bd ready

# 查看所有 E-002 任务
bd list | grep E-002

# 查看特定任务的依赖
bd dep list Bachelor-thesis-xwx
```

---

## 6. 关键路径分析

**最长路径**：TASK-001 -> TASK-004 -> TASK-006
- 预估总时间：0.5h + 1h + 1h = 2.5h

**并行优化后**：
- 第一批（6 任务并行）：~1h（取最长的 TASK-003）
- 第二批（TASK-004）：1h
- 第三批（TASK-006）：1h
- 第四批（TASK-009）：0.5h（可与第三批并行）

**总预估时间**：~3h（串行）或 ~2.5h（最大并行）
