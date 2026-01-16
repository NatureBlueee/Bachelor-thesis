# 技术方案 TECH-E-001-v1

> * EPIC_ID：E-001
> * EPIC_DIR：`E-001-fix-multi-agent`
> * 文档状态：FINAL
> * 版本：v1
> * 创建人：Tech Agent
> * 创建日期：2025-01-14

---

## 0. 关联信息

* PRD：`../prd/PRD-E-001-v0.md`
* Story：`../story/STORY-001-deep-read.md`
* biz-overview：`/docs/_project/biz-overview.md`

---

## 1. 目标与范围对齐

引用 PRD-E-001-v0：
- 多轮对话不中断（3+ 轮）
- Agent 间任务委派可见
- 输出结构化文献笔记

---

## 2. 现状与约束（代码验证）

### 2.1 相关代码现状

| 组件 | 文件路径 | 状态 |
|------|----------|------|
| academic-partner | `agents/academic_partner.yaml` | [VERIFIED] 已修复 |
| literature-agent | `agents/literature_agent.yaml` | [VERIFIED] 工具已配置 |
| document_tools_sync | `tools/document_tools_sync.py:19-58` | [VERIFIED] 同步包装器存在 |
| document_tools | `tools/document_tools.py:50-105` | [VERIFIED] 异步实现存在 |
| network.yaml | `network.yaml:1-172` | [VERIFIED] 网络配置正确 |

### 2.2 已修复问题

| 问题 | 修复内容 | 文件:行号 |
|------|----------|-----------|
| `finish()` 不存在 | 删除 `finish()` 调用 | `academic_partner.yaml:45,56` |
| `max_iterations` 太小 | 5 → 15 | `academic_partner.yaml:14` |

### 2.3 复用清单

| 可复用能力 | 来源 |
|------------|------|
| `search_literature()` | `document_tools_sync.py:19-32` |
| `suggest_citations()` | `document_tools_sync.py:34-42` |
| `read_literature()` | `document_tools_sync.py:44-58` |
| `task_delegation` mod | OpenAgents 内置 |

### 2.4 硬约束

- YAML Agent 只能调用同步函数（`document_tools_sync.py` 已用 `asyncio.run()` 包装）
- OpenAgents 框架版本：0.8.5
- LLM：glm-4.5（智谱 AI）

---

## 3. 方案总览

### 3.1 一句话方案

修复 `academic_partner.yaml` 中的配置错误，使多 Agent 协作流程能正常运行。

### 3.2 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                    OpenAgents Studio UI                      │
│                   http://localhost:8700/studio               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     network.yaml                             │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │ HTTP :8700      │  │ gRPC :8600      │                   │
│  │ (Studio UI)     │  │ (Agent 通信)    │                   │
│  └─────────────────┘  └─────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ academic-     │    │ literature-   │    │ pr-manager    │
│ partner       │    │ agent         │    │ archivist     │
│ (Collaborator)│    │ (Worker)      │    │ (Worker)      │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │
        │  delegate_task()    │
        ├────────────────────►│
        │                     │
        │  complete_task()    │
        │◄────────────────────┤
```

### 3.3 数据流

```
用户消息
    │
    ▼
project.notification.message_received
    │
    ▼
academic-partner 分析
    │
    ├─ 简单问题 → send_project_message() → 用户
    │
    └─ 文献任务 → delegate_task()
                      │
                      ▼
              task.notification.assigned
                      │
                      ▼
              literature-agent 执行
                      │
                      ▼
              complete_task()
                      │
                      ▼
              task.notification.completed
                      │
                      ▼
              academic-partner 整合
                      │
                      ▼
              send_project_message() → 用户
```

---

## 4. 详细设计

### 4.1 事件契约

#### 委派任务 payload（academic-partner → literature-agent）

```json
{
  "task_type": "deep_read",
  "file_path": "Reference/Cited/xxx.md",
  "context": "用户研究主题描述"
}
```

#### 返回结果 payload（literature-agent → academic-partner）

```json
{
  "task_type": "deep_read",
  "results": "结构化笔记内容",
  "citations": ["追踪文献列表"],
  "notes": "## 文献笔记：[标题]\n..."
}
```

### 4.2 工具调用链

```
literature-agent
    │
    ├─ search_literature(query)
    │      └─ document_tools_sync.py:19
    │             └─ asyncio.run(doc_tools.search_literature())
    │                    └─ document_tools.py:50
    │
    └─ read_literature(file_name)
           └─ document_tools_sync.py:44
                  └─ asyncio.run(doc_tools.read_file())
                         └─ document_tools.py:116
```

---

## 5. 验证方法

### 5.1 启动命令

```bash
cd /Users/nature/个人项目/Bachelor-thesis/academic_network
openagents start network.yaml
```

### 5.2 验证步骤

| 步骤 | 操作 | 预期结果 |
|------|------|----------|
| 1 | 打开 http://localhost:8700/studio | 看到 Studio UI |
| 2 | 发送 "你好" | 收到 academic-partner 回复 |
| 3 | 继续对话 3+ 轮 | 不中断 |
| 4 | 发送 "帮我搜索 AI literacy 相关文献" | 看到委派给 literature-agent |
| 5 | 等待结果 | 收到文献列表 |

---

## 6. TASK 拆解建议

基于 STORY-001，建议以下 TASK：

| TASK ID | 描述 | 优先级 | 对应 AC |
|---------|------|--------|---------|
| TASK-001 | 验证系统启动和基本对话 | P0 | AC1, AC2 |
| TASK-002 | 验证任务委派流程 | P0 | AC3 |
| TASK-003 | 验证深度阅读输出 | P0 | AC4 |

### TASK-001：验证系统启动和基本对话

**验收标准**：
- [ ] 系统能正常启动
- [ ] 发送消息能收到回复
- [ ] 连续对话 3+ 轮不中断

### TASK-002：验证任务委派流程

**验收标准**：
- [ ] 请求文献搜索时，能看到委派给 literature-agent
- [ ] literature-agent 能正确调用 search_literature 工具
- [ ] 结果能返回给 academic-partner

### TASK-003：验证深度阅读输出

**验收标准**：
- [ ] 请求深度阅读时，输出包含"基本信息"
- [ ] 输出包含"方法论"
- [ ] 输出包含"关键发现"
- [ ] 输出包含"RQ关联"

---

## 7. 风险与预案

| 风险 | 概率 | 影响 | 预案 |
|------|------|------|------|
| LLM 响应超时 | 中 | 高 | 增加 agent_timeout 配置 |
| 文献内容过长 | 中 | 中 | read_literature 已限制 3000 字符预览 |

---

## 8. 变更记录

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| v1 | 2025-01-14 | Tech Agent | 初版 |
