# Agent 间通信与工具设计

> 创建时间: 2025-12-27
> 基于: OpenAgents Project Mod + Task Delegation Mod
> 目的: 设计 Agent 之间的通信机制、工具规范、PR Scope 实现

---

## 1. 通信架构总览

### 1.1 OpenAgents 能力映射

| 我们的概念 | OpenAgents 对应 | 说明 |
|-----------|----------------|------|
| PR Scope（任务边界） | Project Mod | 每个 PR 是一个 Project |
| PR 内的共享状态 | `project.global_state` | 修改规格、共识、进度 |
| Agent 私有笔记 | `project.agent_state` | Literature Agent 的阅读进度等 |
| 产出物 | `project.artifact` | PR 文件、阅读笔记等 |
| Agent 间委派 | Task Delegation Mod | 结构化的任务委派 |
| 用户入口 | Messaging Mod / Channel | 用户与 Academic Partner 对话 |

### 1.2 通信流图

```
┌──────────────────────────────────────────────────────────────────────────┐
│                              用户入口                                     │
│                          (Messaging Mod)                                  │
└────────────────────────────────┬─────────────────────────────────────────┘
                                 │ 用户消息
                                 ↓
┌──────────────────────────────────────────────────────────────────────────┐
│                         Academic Partner                                  │
│                                                                           │
│  接收用户消息 → 批判性思考 → 生成任务 → 委派给专家 Agent                   │
│                                                                           │
│  使用的 Mod:                                                              │
│  - Messaging Mod: 与用户对话                                              │
│  - Project Mod: 管理 PR Scope                                            │
│  - Task Delegation Mod: 委派任务给其他 Agent                              │
└────────────────────────────────┬─────────────────────────────────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ↓                      ↓                      ↓
    task.delegate          task.delegate          task.delegate
          │                      │                      │
          ↓                      ↓                      ↓
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Literature Agent│  │   PR Manager    │  │    Archivist    │
│                 │  │                 │  │                 │
│ task.complete   │  │ task.complete   │  │ task.complete   │
│ 返回阅读笔记     │  │ 返回验证结果     │  │ 返回执行确认     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## 2. PR Scope 设计（基于 Project Mod）

### 2.1 PR 作为 Project

每个 PR 创建时，对应创建一个 OpenAgents Project：

```yaml
# network.yaml 中的 Project 模板
project_templates:
  thesis_modification:
    name: "论文修改流程"
    description: "PR-driven 的论文修改工作流"
    agent_groups: ["coordinators", "experts", "managers"]
    context: |
      这是一个论文修改 PR。

      约束：
      - 所有修改必须有文献支持
      - 不直接修改 Draft.md，通过 Archivist 执行
      - 遵循 GB/T 7714-2015 引用格式
```

### 2.2 PR Scope 的状态设计

**Global State（共享状态）**：

| Key | 类型 | 说明 |
|-----|------|------|
| `pr_id` | string | PR-XXXX |
| `pr_title` | string | PR 标题 |
| `pr_status` | enum | draft / reviewing / merged |
| `modification_spec` | object | 修改规格（Academic Partner 输出） |
| `consensus` | array | 讨论共识列表 |
| `checklist` | object | 10 步 checklist 状态 |

**Agent State（私有状态）**：

| Agent | Key | 说明 |
|-------|-----|------|
| Literature Agent | `reading_progress` | 当前阅读进度 |
| Literature Agent | `temp_thoughts` | 临时想法 |
| PR Manager | `validation_notes` | 验证过程中的笔记 |
| Archivist | `pending_sync` | 待同步的文件列表 |

**Artifacts（产出物）**：

| Key | 说明 |
|-----|------|
| `pr_file` | PR-XXXX.md 的内容 |
| `reading_notes` | 文献阅读笔记 |
| `modification_result` | 修改结果 |

### 2.3 PR 生命周期事件

```
project.start (创建 PR)
    ↓
project.global_state.set (设置修改规格)
    ↓
task.delegate (委派给专家)
    ↓
task.complete (专家完成任务)
    ↓
project.artifact.set (保存产出物)
    ↓
project.complete (合并 PR)
```

---

## 3. Agent 间任务委派（基于 Task Delegation Mod）

### 3.1 任务委派格式

**Academic Partner → Literature Agent**：

```python
await tasks.delegate_task(
    assignee_id="literature-agent",
    description="阅读文献并输出结构化笔记",
    payload={
        "task_type": "deep_read",
        "literature_path": "Reference/Cited/Schroth_2019.md",
        "focus_points": [
            "Gen Z 的特征描述",
            "与 Millennials 的区别"
        ],
        "research_framework": {
            "RQ1": "...",
            "RQ2": "...",
            "RQ3": "..."
        },
        "output_format": "structured_notes"
    },
    timeout_seconds=600  # 10 分钟
)
```

**Academic Partner → PR Manager**：

```python
await tasks.delegate_task(
    assignee_id="pr-manager",
    description="验证修改规格并执行合并 checklist",
    payload={
        "task_type": "merge_verification",
        "pr_id": "PR-0010",
        "modification_spec": {
            "original_text": "...",
            "target_text": "...",
            "acceptance_criteria": [...],
            "required_citations": [...]
        }
    },
    timeout_seconds=300
)
```

**PR Manager → Archivist**：

```python
await tasks.delegate_task(
    assignee_id="archivist",
    description="执行文件修改并同步状态",
    payload={
        "task_type": "file_operation",
        "operations": [
            {
                "type": "UPDATE",
                "file": "Draft.md",
                "line_range": [45, 52],
                "new_content": "..."
            }
        ],
        "sync_required": [
            "_CONTEXT.md",
            "PR/PR-0010.md"
        ]
    },
    timeout_seconds=120
)
```

### 3.2 任务完成格式

**Literature Agent 返回**：

```python
await tasks.complete_task(
    task_id=task_id,
    result={
        "status": "success",
        "reading_notes": {
            "core_arguments": [...],
            "methodology": {...},
            "relevance": {...},
            "quotable_passages": [...]
        },
        "temp_thoughts": [...],
        "critical_points": [...]
    }
)
```

**PR Manager 返回**：

```python
# 成功
await tasks.complete_task(
    task_id=task_id,
    result={
        "status": "verified",
        "checklist": {
            "1_read_pr": "pass",
            "2_read_original": "pass",
            ...
            "10_update_status": "pass"
        },
        "archivist_task_id": "..."
    }
)

# 需要回推
await tasks.complete_task(
    task_id=task_id,
    result={
        "status": "blocked",
        "open_issues": [
            {
                "type": "OPEN",
                "description": "修改规格不完整",
                "missing": "原文引用",
                "requires": "Academic Partner 补充"
            }
        ]
    }
)
```

### 3.3 升级规则实现

当 Agent 遇到无法处理的情况时，通过 `fail_task` 回推：

```python
await tasks.fail_task(
    task_id=task_id,
    error_message="[OPEN] 规格不完整",
    details={
        "type": "ESCALATION",
        "reason": "修改规格缺少原文引用",
        "required_action": "Academic Partner 需要提供 Draft.md 中的精确位置",
        "blocked_items": ["checklist_item_2"]
    }
)
```

---

## 4. 工具设计规范

### 4.1 工具设计原则（来自 Anthropic）

> "Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts."

**关键原则**：
1. 每个工具有独特的目的和清晰的描述
2. 在提示词中嵌入显式的工具选择启发式
3. 工具设计要"防错"（减少误用可能性）

### 4.2 Academic Partner 的工具

```yaml
tools:
  # PR 管理
  - name: create_pr
    description: |
      创建一个新的 PR。
      使用时机：用户请求修改论文内容时
      不要使用：只是讨论、没有明确修改意图时
    parameters:
      title: PR 标题
      scope: 修改范围（哪个章节）
      reason: 为什么要修改

  - name: get_pr_status
    description: 获取指定 PR 的当前状态

  # 任务委派
  - name: delegate_literature_task
    description: |
      委派文献阅读任务给 Literature Agent。
      使用时机：需要深度阅读文献、查找引用支持时
      不要使用：只需要简单查询文献是否存在时
    parameters:
      literature_path: 文献路径
      focus_points: 关注点列表
      output_format: structured_notes | quotable_only

  - name: delegate_merge_task
    description: |
      委派合并验证任务给 PR Manager。
      前提条件：必须先生成完整的修改规格
      使用时机：用户确认可以合并时
    parameters:
      pr_id: PR ID
      modification_spec: 结构化的修改规格

  # 记忆管理
  - name: add_memory
    description: |
      将重要信息添加到 Mem0。
      使用时机：用户表达了重要偏好或做出了关键决策
      不要使用：日常对话、临时性讨论
    parameters:
      content: 要记住的内容
      category: preference | decision | insight
```

### 4.3 Literature Agent 的工具

```yaml
tools:
  - name: read_literature
    description: 读取指定文献的内容
    parameters:
      path: 文献路径
      section: 可选，指定章节

  - name: search_in_literature
    description: 在文献中搜索特定内容
    parameters:
      path: 文献路径
      query: 搜索关键词

  - name: save_reading_note
    description: |
      保存阅读笔记到 Agent State。
      用于保存临时想法和阅读进度
    parameters:
      note_type: temp_thought | progress | critical_point
      content: 笔记内容

  - name: report_progress
    description: 向委派者报告阅读进度
    parameters:
      message: 进度描述
      data: 可选，结构化数据
```

### 4.4 PR Manager 的工具

```yaml
tools:
  - name: validate_spec
    description: |
      验证修改规格的完整性。
      必须首先调用此工具，然后再执行 checklist。
    parameters:
      spec: 修改规格对象
    returns:
      complete: boolean
      missing_items: 缺失项列表

  - name: execute_checklist
    description: |
      执行 10 步合并 checklist。
      前提：validate_spec 返回 complete=true
    parameters:
      pr_id: PR ID
      spec: 已验证的修改规格

  - name: delegate_archivist_task
    description: 委派文件操作给 Archivist
    parameters:
      operations: 操作列表
      sync_required: 需要同步的文件列表

  - name: escalate_issue
    description: |
      回推问题给 Academic Partner。
      使用时机：规格不完整、引用缺失、发现冲突
    parameters:
      issue_type: OPEN | BLOCKED
      description: 问题描述
      requires: 需要谁来处理
```

### 4.5 Archivist 的工具

```yaml
tools:
  - name: read_file
    description: 读取指定文件内容
    parameters:
      path: 文件路径

  - name: update_file
    description: |
      更新文件内容。精确替换，不重述。
    parameters:
      path: 文件路径
      line_range: 行号范围
      new_content: 新内容（必须是精确文本）

  - name: create_file
    description: 创建新文件
    parameters:
      path: 文件路径
      content: 文件内容

  - name: sync_index
    description: 同步索引文件
    parameters:
      index_file: 索引文件路径
      entries: 要更新的条目

  - name: confirm_operation
    description: 确认操作完成
    parameters:
      operation_id: 操作 ID
      status: success | error
      details: 详情
```

---

## 5. 通知与事件处理

### 5.1 Academic Partner 需要监听的事件

```python
# 用户消息
@agent.on_event("messaging.message.received")
async def handle_user_message(event):
    # 处理用户输入
    pass

# 任务完成通知
@agent.on_event("task.notification.completed")
async def handle_task_completed(event):
    task_id = event.payload["task_id"]
    result = event.payload["result"]
    # 处理专家返回的结果
    pass

# 任务失败/回推通知
@agent.on_event("task.notification.failed")
async def handle_task_failed(event):
    # 处理升级问题
    pass
```

### 5.2 专家 Agent 需要监听的事件

```python
# 任务分派通知
@agent.on_event("task.notification.assigned")
async def handle_task_assigned(event):
    task_id = event.payload["task_id"]
    description = event.payload["description"]
    payload = event.payload["payload"]
    # 开始执行任务
    pass
```

---

## 6. 实现计划

### 6.1 Phase 1: 基础架构

1. **配置 network.yaml**
   - 添加 Project Mod 配置（thesis_modification 模板）
   - 添加 Task Delegation Mod
   - 配置 Agent Groups

2. **实现 Academic Partner**
   - 基础对话能力
   - PR 创建/管理工具
   - 任务委派工具

### 6.2 Phase 2: 专家 Agent

1. **Literature Agent**
   - 文献读取工具
   - 结构化笔记输出
   - 阅读进度报告

2. **PR Manager**
   - 规格验证工具
   - Checklist 执行
   - 升级规则实现

3. **Archivist**
   - 文件操作工具
   - 索引同步
   - 状态确认

### 6.3 Phase 3: 集成测试

1. 端到端流程测试
2. 升级规则测试
3. 超时处理测试
4. 错误恢复测试

---

## 7. 关键设计决策

### 7.1 为什么用 Task Delegation 而不是直接 Event？

**优势**：
- 自动超时处理
- 状态跟踪
- 进度报告
- 访问控制

**替代方案**：直接使用 `send_event` + 自定义事件

**决策**：使用 Task Delegation Mod，因为它已经实现了我们需要的所有功能。

### 7.2 为什么 PR = Project？

**优势**：
- 自然的任务边界
- 内置的状态管理（global_state, agent_state）
- 内置的产出物管理（artifacts）
- 权限控制

**替代方案**：自定义 Mod

**决策**：复用 Project Mod，减少开发工作量。

### 7.3 工具数量的平衡

**原则**：
- 每个 Agent 有 4-6 个核心工具
- 工具描述包含"使用时机"和"不要使用"
- 工具之间有清晰的边界

---

## 附录：完整的 network.yaml 示例

```yaml
network:
  name: "AcademicResearchNetwork"
  mode: "centralized"

  mods:
    # 默认工作空间
    - name: "openagents.mods.workspace.default"
      enabled: true

    # 消息传递（用户入口）
    - name: "openagents.mods.workspace.messaging"
      enabled: true

    # 项目管理（PR Scope）
    - name: "openagents.mods.workspace.project"
      enabled: true
      config:
        max_concurrent_projects: 10
        project_templates:
          thesis_modification:
            name: "论文修改流程"
            description: "PR-driven 的论文修改工作流"
            agent_groups: ["coordinators", "experts", "managers"]
            context: |
              这是一个论文修改 PR。

              约束：
              - 所有修改必须有文献支持
              - 不直接修改 Draft.md，通过 Archivist 执行
              - 遵循 GB/T 7714-2015 引用格式
              - 使用 [OPEN] 标记未解决问题

          literature_review:
            name: "文献阅读任务"
            description: "深度阅读文献并输出结构化笔记"
            agent_groups: ["experts"]
            context: |
              这是一个文献阅读任务。

              要求：
              - 输出结构化阅读笔记
              - 每个要点有原文引用
              - 记录临时想法
              - 与研究框架关联

    # 任务委派
    - name: "openagents.mods.coordination.task_delegation"
      enabled: true
      config:
        default_timeout: 600  # 10 分钟

  agent_groups:
    coordinators:
      description: "协调者 - 与用户对话，分派任务"
      agents:
        - "academic-partner"

    experts:
      description: "专家 - 执行具体任务"
      agents:
        - "literature-agent"
        - "pr-manager"

    managers:
      description: "管理者 - 文件操作"
      agents:
        - "archivist"
```
