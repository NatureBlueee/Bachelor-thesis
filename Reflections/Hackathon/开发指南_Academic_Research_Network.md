# Academic Research Network - 开发指南

> 基于对 OpenAgents 深入分析后的完整开发路线图
> 版本: 1.0 | 更新日期: 2025-12-25

---

## 1. 核心架构理解

### OpenAgents 的本质
不是"聊天机器人框架"，而是 **Agent Network 基础设施**：

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Network (通信空间)                           │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                        Mods (能力模块)                         │  │
│  │   messaging   │   forum   │   project   │   wiki   │ default  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                               ▲                                     │
│          ┌────────────────────┼────────────────────┐               │
│          │                    │                    │               │
│     ┌────┴────┐         ┌────┴────┐         ┌────┴────┐           │
│     │  Agent  │         │  Agent  │         │  Agent  │           │
│     │ (YAML)  │         │(Python) │         │ (Human) │           │
│     └─────────┘         └─────────┘         └─────────┘           │
│                                                  ↑                  │
│                                              Studio                │
└─────────────────────────────────────────────────────────────────────┘
```

### 关键概念对照表

| 概念 | 在 OpenAgents 中 | 在我们项目中 |
|------|------------------|-------------|
| Network | 通信容器 | academic_network |
| Agent | 参与者（Python或YAML定义） | Literature, Critical Thinker... |
| Mod | 能力扩展模块 | messaging, project, 自定义Document Mod |
| Event | 一切交互的载体 | `task.delegate`, `task.complete`, 自定义事件 |
| Workspace | 协作空间抽象 | channels, files, forum |
| Studio | 人类界面 | 我们用来观察和参与的Web UI |

---

## 2. 我们要开发什么

### 目标架构（类比 Research Team Demo）

```
                    ┌─────────────────────┐
    用户请求        │   Facilitator       │
  "修改方法论" ────▶│  (协调者 Router)     │
                    └──────────┬──────────┘
                               │ event: task.delegate
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
     ┌────────────┐    ┌────────────┐    ┌────────────┐
     │ Literature │    │  Critical  │    │   Method   │
     │   Agent    │    │  Thinker   │    │   Expert   │
     └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
           │                 │                 │
           └─────────────────┼─────────────────┘
                             │ event: task.complete
                             ▼
                    ┌─────────────────────┐
                    │    PR Manager       │
                    │  (生成修改请求 PR)   │
                    └─────────────────────┘
```

### Agent 角色与职责

| Agent ID | 角色 | 触发事件 | 输出 |
|----------|------|---------|------|
| `facilitator` | 协调者 | `project.started`, `task.complete` | 分配任务给其他Agent |
| `literature-agent` | 文献专家 | `task.delegate` (查询文献) | 文献摘要、相关引用 |
| `critical-thinker` | 批判者 | `task.delegate` (审查论点) | 质疑点、逻辑漏洞 |
| `method-expert` | 方法顾问 | `task.delegate` (方法论问题) | 方法建议、设计评估 |
| `pr-manager` | 变更管理 | `consensus.reached` | 生成PR文件 |

---

## 3. 开发路径选择

### 方式一：YAML Agent（推荐起步）
**适合**：快速验证、配置驱动、无需复杂逻辑

```yaml
# academic_network/agents/literature_agent.yaml
type: "openagents.agents.collaborator_agent.CollaboratorAgent"
agent_id: "literature-agent"

config:
  model_name: "gpt-4o-mini"
  max_iterations: 5
  
  instruction: |
    你是学术研究团队的文献专家。
    
    你可以：
    - 根据研究问题推荐文献
    - 生成结构化摘要
    - 比较不同文献观点
    
    你不能：
    ❌ 凭空编造文献
    ❌ 评判文献学术价值
    ❌ 直接修改论文

  react_to_all_messages: false
  
  triggers:
    - event: "task.delegate"
      instruction: |
        收到文献查询任务。从 payload.query 获取查询内容。
        1. 分析查询，找出最相关的文献
        2. 生成结构化摘要
        3. send_event("task.complete", "facilitator", {results: "..."})
        4. finish()

mods:
  - name: "openagents.mods.workspace.project"
    enabled: true
  - name: "openagents.mods.workspace.default"
    enabled: true

connection:
  host: "localhost"
  port: 8700
  transport: "grpc"
```

### 方式二：Python Agent（可扩展）
**适合**：需要访问本地文件、复杂逻辑、外部API集成

```python
# academic_network/agents/literature_agent.py
from openagents.agents.worker_agent import WorkerAgent, on_event
from openagents.models.agent_config import AgentConfig
from openagents.models.event_context import EventContext
import os

class LiteratureAgent(WorkerAgent):
    default_agent_id = "literature-agent"
    
    async def on_startup(self):
        """Agent 启动时调用"""
        ws = self.workspace()
        await ws.channel("general").post("📚 Literature Agent 上线")
    
    @on_event("task.delegate")
    async def handle_task(self, context: EventContext):
        """处理文献查询任务"""
        payload = context.incoming_event.payload
        query = payload.get("query", "")
        
        # 访问本地文献库
        results = await self.search_local_references(query)
        
        # 使用LLM生成摘要
        summary = await self.run_agent(
            context=context,
            instruction=f"为以下查询生成文献摘要: {query}\n找到的文献: {results}"
        )
        
        # 发送完成事件
        ws = self.workspace()
        await ws.send_event(
            event_name="task.complete",
            destination_id="facilitator",
            payload={"task_id": payload.get("task_id"), "results": summary}
        )
    
    async def search_local_references(self, query: str) -> str:
        """搜索本地 Reference/ 文件夹"""
        ref_path = "d:/Profolio/文章/Thesis/Graduate-thesis/Reference/PDF-MD/output_api"
        results = []
        
        for filename in os.listdir(ref_path):
            if filename.endswith(".md"):
                filepath = os.path.join(ref_path, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    if query.lower() in content.lower():
                        results.append(filename)
        
        return "\n".join(results[:5])  # 返回前5个

if __name__ == "__main__":
    agent = LiteratureAgent(agent_config=AgentConfig(
        model_name="gpt-4o-mini",
        instruction="你是文献专家，帮助研究者找到相关文献。"
    ))
    agent.start(network_host="localhost", network_port=8700)
    agent.wait_for_stop()
```

---

## 4. Network 配置

```yaml
# academic_network/network.yaml
network:
  name: "AcademicResearchNetwork"
  mode: "centralized"
  node_id: "academic-network-1"

  transports:
    - type: "http"
      config:
        port: 8700
        serve_studio: true
        serve_mcp: true
    - type: "grpc"
      config:
        port: 8600

  agent_groups:
    coordinators:
      description: "协调者 (Facilitator)"
      password_hash: "xxx"  # 需要生成
      metadata:
        permissions: ["create_projects", "delegate_tasks"]
        agents: ["facilitator"]
    
    experts:
      description: "专家 Agents"
      password_hash: "xxx"
      metadata:
        permissions: ["execute_tasks", "report_results"]
        agents: ["literature-agent", "critical-thinker", "method-expert"]
    
    managers:
      description: "变更管理"
      metadata:
        agents: ["pr-manager"]

  mods:
    - name: "openagents.mods.workspace.default"
      enabled: true
      config:
        custom_events_enabled: true
    
    - name: "openagents.mods.workspace.messaging"
      enabled: true
      config:
        default_channels:
          - name: "general"
            description: "综合讨论"
          - name: "literature"
            description: "文献讨论"
          - name: "methodology"
            description: "方法论讨论"
    
    - name: "openagents.mods.workspace.project"
      enabled: true
      config:
        project_templates:
          thesis_modification:
            name: "论文修改流程"
            description: "多专家协作的论文修改"
            agent_groups: ["coordinators", "experts", "managers"]
            context: |
              论文修改工作流：
              1. Facilitator 接收修改请求
              2. 分配任务给相关专家
              3. 专家返回分析结果
              4. Facilitator 整合形成共识
              5. PR Manager 生成变更单

network_profile:
  discoverable: false
  name: "Academic Research Network"
  description: "多Agent协作的学术研究助手"
```

---

## 5. 开发步骤

### Phase 1: 最小可行验证 (MVP)
目标：让 2 个 Agent 能对话

1. [ ] 修改 `academic_network/network.yaml`
2. [ ] 创建 `facilitator.yaml` (YAML Agent)
3. [ ] 创建 `literature_agent.yaml` (YAML Agent)
4. [ ] 启动 Network → 启动两个 Agent → 在 Studio 测试

验证标准：
- 在 Studio 创建 Project
- Facilitator 收到 `project.started` 事件
- Facilitator 发送 `task.delegate` 给 Literature Agent
- Literature Agent 返回 `task.complete`

### Phase 2: 增加对抗性
目标：Critical Thinker 能质疑 Literature Agent 的输出

1. [ ] 创建 `critical_thinker.yaml`
2. [ ] 修改 Facilitator 的触发器，在收到 Literature 结果后转给 Critical Thinker
3. [ ] 测试对抗性对话

### Phase 3: 集成本地文件
目标：Agent 能读取 Reference/ 和 PR/ 文件

1. [ ] 将 Literature Agent 改为 Python Agent
2. [ ] 实现 `search_local_references()` 方法
3. [ ] 实现 PR Manager 的 `create_pr()` 方法

### Phase 4: 完整流程
目标：完成从"用户请求"到"生成PR"的全流程

1. [ ] 串联所有 Agent
2. [ ] 录制演示视频
3. [ ] 准备 GitHub 提交

---

## 6. 常用 API 速查

### Workspace API
```python
ws = self.workspace()

# 频道操作
await ws.channel("general").post("消息内容")
await ws.channel("general").reply(message_id, "回复内容")

# 直接消息
await ws.agent("other-agent").send("私信内容")

# 自定义事件
await ws.send_event(
    event_name="task.delegate",
    destination_id="literature-agent",
    payload={"query": "研究问题"}
)
```

### 事件装饰器
```python
from openagents.agents.worker_agent import on_event

@on_event("task.delegate")
async def handle_task(self, context: EventContext):
    payload = context.incoming_event.payload
    source = context.source_id
```

### LLM 调用
```python
await self.run_agent(
    context=context,
    instruction="你的提示词"
)
```

---

## 7. 关键文件位置

```
Graduate-thesis/
├── academic_network/           # OpenAgents Network 根目录
│   ├── network.yaml           # 网络配置
│   ├── agents/                # Agent 定义
│   │   ├── facilitator.yaml
│   │   ├── literature_agent.yaml (或.py)
│   │   ├── critical_thinker.yaml
│   │   └── pr_manager.yaml
│   └── tools/                 # 自定义工具
│       └── file_access.py
├── Reference/                  # 文献库（Agent 需要访问）
├── PR/                        # PR 文件（Agent 需要写入）
└── start_all.ps1              # 一键启动脚本
```

---

## 8. 下一步行动

**立即可做**：
1. 用你现有的 `start_all.ps1` 启动环境
2. 修改 `academic_network/network.yaml` 加入 project mod
3. 创建 `facilitator.yaml` 作为 Router
4. 在 Studio 中创建一个 Project 测试

**需要我帮忙**：
- 生成完整的 YAML Agent 配置
- 编写 Python Agent 模板
- 调试事件流
