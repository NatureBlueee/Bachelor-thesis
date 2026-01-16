# 多Agent协作学术研究系统设计文档

> 本文档详细描述基于 OpenAgents 框架的多Agent协作系统，用于学术论文写作的智能辅助。

## 目录

1. [系统概述](#1-系统概述)
2. [Agent架构设计](#2-agent架构设计)
3. [通信与协作模式](#3-通信与协作模式)
4. [记忆系统设计](#4-记忆系统设计)
5. [工具系统设计](#5-工具系统设计)
6. [工作流模板](#6-工作流模板)
7. [核心设计原则](#7-核心设计原则)
8. [框架对比分析](#8-框架对比分析)
9. [技术实现细节](#9-技术实现细节)

---

## 1. 系统概述

### 1.1 项目背景

将软件工程实践应用于学术写作：
- **版本控制**：所有论文修改通过 Git 追踪
- **Code Review**：每次修改需要经过审查
- **CI/CD**：自动化验证流程

核心理念：**每次论文修改都通过 Pull Request**

### 1.2 系统架构总览

```
┌─────────────────────────────────────────────────────────────────┐
│                 Academic Research Network                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  协调层 (Coordinator Layer)                                 │ │
│  │  └─ Academic Partner: 统一入口 + 批判性思考 + 任务委派       │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              ↓ 委派任务                          │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  专家层 (Expert Layer)                                      │ │
│  │  └─ Literature Agent: 文献搜索 + 深度阅读 + 引用建议         │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              ↓ 委派任务                          │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  管理层 (Manager Layer)                                     │ │
│  │  ├─ PR Manager: PR验证（10步检查清单）+ 生命周期管理         │ │
│  │  └─ Archivist: 精确文件操作 + 状态同步                      │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  记忆层 (Memory Layer)                                      │ │
│  │  └─ Mem0 向量数据库 + MEMORY.md 本地备份                    │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Agent架构设计

### 2.1 Agent划分标准

> **核心原则**："区分 Agent 的标准在于他们有没有必要共享同一个 context"

| Agent | 需要的上下文 | 职责边界 |
|-------|-------------|---------|
| Academic Partner | 完整对话历史 | 理解用户意图，协调全局 |
| Literature Agent | 任务上下文 | 专注文献处理 |
| PR Manager | 修改规格 | 专注验证流程 |
| Archivist | 文件操作指令 | 专注执行 |

### 2.2 各Agent详细设计

#### 2.2.1 Academic Partner（协调者）

```yaml
agent_id: "academic-partner"
type: CollaboratorAgent
model: glm-4.5

职责:
  - 统一用户入口
  - 批判性思考审查
  - 任务委派决策
  - 记忆系统管理

触发事件:
  - project.notification.message_received  # 用户消息
  - project.notification.started           # 项目启动
  - task.notification.completed            # 任务完成
  - task.notification.failed               # 任务失败

工具集:
  - send_project_message()    # 回复用户
  - delegate_task()           # 委派任务
  - add_memory_tool()         # 添加记忆
  - search_memory_tool()      # 搜索记忆
  - check_conflict_tool()     # 冲突检测
  - get_all_preferences_tool()
  - get_project_context_tool()

负面约束:
  ❌ 不凭空编造文献
  ❌ 不跳过文献支持直接给结论
  ❌ 不直接修改 Draft.md
```

#### 2.2.2 Literature Agent（文献专家）

```yaml
agent_id: "literature-agent"
type: WorkerAgent
model: glm-4.5

职责:
  - 文献搜索（Cited/Uncited）
  - 博士生式深度阅读
  - 引用建议（优先未引用文献）

任务类型:
  - search: 关键词搜索文献
  - deep_read: 深度阅读分析
  - suggest: 推荐可引用文献

工具集:
  - DocumentTools.search_literature()
  - DocumentTools.read_file()
  - DocumentTools.suggest_citations()

输出格式:
  search: { query, count, files, details }
  deep_read: { file, summary, key_findings, rq_relevance }
  suggest: { topic, suggestions[] }
```

#### 2.2.3 PR Manager（PR管理者）

```yaml
agent_id: "pr-manager"
type: WorkerAgent
model: glm-4.5

职责:
  - PR 创建验证
  - 10步检查清单执行
  - 生命周期状态管理

任务类型:
  - create_pr: 创建PR
  - validate_pr: 验证PR
  - merge_pr: 合并PR

10步验证清单:
  1. [ ] 修改位置明确
  2. [ ] 目标文件正确
  3. [ ] 验收标准清晰
  4. [ ] 引用格式正确 (GB/T 7714-2015)
  5. [ ] 文献支持充分
  6. [ ] 无术语冲突
  7. [ ] 与现有内容一致
  8. [ ] 无重复PR
  9. [ ] 状态标记正确
  10. [ ] 描述完整

状态流转:
  planning → discussing → approved → merged
```

#### 2.2.4 Archivist（档案管理者）

```yaml
agent_id: "archivist"
type: WorkerAgent
model: glm-4.5

职责:
  - 精确文件操作
  - PR结构创建
  - 状态同步

任务类型:
  - write_file: 写入文件
  - read_file: 读取文件
  - move_file: 移动文件
  - create_pr_structure: 创建PR目录结构

安全目录:
  ✅ Modifications/
  ✅ Notes/
  ✅ Reference/

受限目录:
  ❌ Target/
  ❌ .git/
  ❌ academic_network/
```

---

## 3. 通信与协作模式

### 3.1 任务委派模式

```
Academic Partner (协调者)
    │
    ├─→ delegate_task(literature-agent)
    │   ├─ task_type: search
    │   ├─ task_type: deep_read
    │   └─ task_type: suggest
    │
    ├─→ delegate_task(pr-manager)
    │   ├─ task_type: create_pr
    │   ├─ task_type: validate_pr
    │   └─ task_type: merge_pr
    │
    └─→ delegate_task(archivist)
        ├─ task_type: write_file
        ├─ task_type: read_file
        └─ task_type: move_file
```

### 3.2 事件驱动架构

```
用户消息
    ↓
project.notification.message_received
    ↓
Academic Partner 处理
    ↓
delegate_task() → task.notification.assigned
    ↓
Worker Agent 执行
    ↓
task.notification.completed / task.notification.failed
    ↓
Academic Partner 整合结果
    ↓
send_project_message() → 用户
```

### 3.3 结构化交接（Structured Handoff）

当需要修改论文时，Academic Partner 输出标准化的"修改规格"：

```markdown
## 修改规格 PR-XXXX

### 原文定位
- 文件：Target/Draft.md
- 位置：第X节，第Y段
- 原文摘录：「...原文内容...」

### 修改目标
[具体的修改描述]

### 验收标准 (AC)
1. [ ] 修改后的文本包含 XXX
2. [ ] 引用格式符合 GB/T 7714-2015
3. [ ] 不引入新的术语冲突

### 支持文献
- [作者(年份)] 文献标题 - 相关发现
```

---

## 4. 记忆系统设计

### 4.1 双层架构

```
┌─────────────────────────────────────────────────────────────┐
│                    AcademicMemory                            │
├─────────────────────────────────────────────────────────────┤
│  第一层：Mem0 向量数据库                                      │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ Provider: Qdrant (本地)                                  ││
│  │ Embeddings: Zhipu AI embedding-3 (2048维)               ││
│  │ LLM: glm-4-flash (OpenAI兼容API)                        ││
│  │ Collection: academic_memory_zhipu                        ││
│  │ 功能: 语义搜索、冲突检测                                  ││
│  └─────────────────────────────────────────────────────────┘│
├─────────────────────────────────────────────────────────────┤
│  第二层：MEMORY.md 本地备份                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 格式: Markdown + 时间戳                                  ││
│  │ 自动同步: 每次 add() 后触发                              ││
│  │ 故障转移: Mem0 失败时使用                                ││
│  │ 人类可读: 可直接编辑                                     ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### 4.2 记忆分类（6种）

| 分类 | 触发场景 | 示例 |
|------|---------|------|
| `preference` | "我喜欢...", "不要..." | "我喜欢简洁的写作风格" |
| `decision` | "我们采用...", "选择..." | "采用资源依赖理论作为主框架" |
| `insight` | 重要发现、认识 | "AI素养与向上影响存在正相关" |
| `constraint` | "必须...", "不能..." | "引用必须来自Reference/" |
| `correction` | 用户纠正AI理解 | "不是AI literacy，是AI fluency" |
| `inspiration` | 灵感、待探索想法 | "可以考虑加入调节变量" |

### 4.3 核心方法

```python
class AcademicMemory:
    async def add(self, content: str, category: str, metadata: dict = None):
        """添加记忆 → Mem0 + MEMORY.md 同步"""

    async def search(self, query: str, category: str = None, limit: int = 5):
        """搜索记忆 → Mem0优先，失败回退MEMORY.md"""

    async def check_conflict(self, content: str, category: str = None):
        """冲突检测 → 检查矛盾词对（要/不要, want/don't want）"""

    async def get_all_preferences(self):
        """获取所有偏好"""

    async def get_project_context(self):
        """获取项目上下文（决策+约束+洞察）"""
```

### 4.4 Agent间记忆共享

```python
# 单例模式确保所有Agent共享同一实例
_memory_instance = None

def get_memory(project_id: str = "thesis_project") -> AcademicMemory:
    global _memory_instance
    if _memory_instance is None:
        _memory_instance = AcademicMemory(project_id=project_id)
    return _memory_instance
```

---

## 5. 工具系统设计

### 5.1 DocumentTools（文档访问）

```python
class DocumentTools:
    def __init__(self, project_root: str):
        self.project_root = project_root

    async def search_literature(self, query: str,
                                search_cited: bool = True,
                                search_uncited: bool = True,
                                limit: int = 5) -> dict:
        """搜索文献，优先返回Uncited"""

    async def read_file(self, file_path: str) -> str:
        """读取文件内容"""

    async def read_draft_section(self, start_line: int, end_line: int) -> str:
        """读取Draft.md指定行"""

    async def suggest_citations(self, topic: str) -> list:
        """建议可引用文献（优先Uncited）"""

    async def check_missing_citations(self) -> list:
        """检查缺失引用"""

    async def convert_pdf(self, pdf_path: str) -> str:
        """PDF→Markdown转换（Datalab API）"""
```

### 5.2 MemoryTools（记忆访问）

```python
# 异步版本 (memory_tools.py)
async def add_memory_tool(content: str, category: str, metadata: dict = None)
async def search_memory_tool(query: str, category: str = None, limit: int = 5)
async def check_conflict_tool(content: str, category: str = None)
async def get_all_preferences_tool()
async def get_project_context_tool()

# 同步版本 (memory_tools_sync.py) - 用于YAML配置
def add_memory(content: str, category: str, metadata: dict = None)
def search_memory(query: str, category: str = None, limit: int = 5)
def check_conflict(content: str, category: str = None)
def get_preferences()
def get_project_context()
```

---

## 6. 工作流模板

### 6.1 论文修改流程 (thesis_modification)

```
┌─────────────────────────────────────────────────────────────┐
│                    论文修改工作流                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. 用户提交修改请求                                          │
│     ↓                                                        │
│  2. Academic Partner 分析请求                                │
│     ├─ 检查记忆系统（偏好、约束）                             │
│     ├─ 判断是否需要文献支持                                   │
│     └─ 决定委派策略                                          │
│     ↓                                                        │
│  3. 委派任务                                                 │
│     ├─→ Literature Agent: 搜索相关文献                       │
│     └─→ PR Manager: 准备验证                                 │
│     ↓                                                        │
│  4. 整合结果，输出修改规格                                    │
│     ↓                                                        │
│  5. PR Manager 执行10步验证                                  │
│     ↓                                                        │
│  6. Archivist 创建PR文件结构                                 │
│     ↓                                                        │
│  7. 用户审核 → 合并                                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 深度阅读流程 (deep_reading)

```
┌─────────────────────────────────────────────────────────────┐
│                    深度阅读工作流                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. 用户提供文献或主题                                        │
│     ↓                                                        │
│  2. Academic Partner 分析请求                                │
│     ↓                                                        │
│  3. 委派给 Literature Agent                                  │
│     ↓                                                        │
│  4. Literature Agent 执行博士生式阅读:                       │
│     ├─ 追踪 Reference List                                   │
│     ├─ 提取方法论细节                                        │
│     ├─ 建立与 RQ 的关联                                      │
│     └─ 记录相关引用                                          │
│     ↓                                                        │
│  5. Academic Partner 整合输出                                │
│     ├─ 结构化笔记                                            │
│     └─ 更新记忆系统（insight）                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 6.3 学术讨论流程 (academic_discussion)

```
┌─────────────────────────────────────────────────────────────┐
│                    学术讨论工作流                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. 用户提出问题                                             │
│     ↓                                                        │
│  2. Academic Partner 批判性分析                              │
│     ├─ 检查记忆系统                                          │
│     ├─ 质疑假设                                              │
│     └─ 评估论证强度                                          │
│     ↓                                                        │
│  3. 如需文献支持                                             │
│     └─→ 委派 Literature Agent 搜索                          │
│     ↓                                                        │
│  4. 形成回复                                                 │
│     ├─ 直接回答 + 文献支持                                   │
│     ├─ 或记录分歧点                                          │
│     └─ 更新记忆（decision/insight）                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. 核心设计原则

### 7.1 负面约束优先

> "告诉 Agent '不能做什么' 比 '应该做什么' 更重要"

```
❌ 不直接编辑 Draft.md（必须通过 PR）
❌ 不凭空编造文献（必须来自 Reference/）
❌ 不跳过批判性审查
❌ 不在没有文献支持的情况下给出结论
❌ 不覆盖已有的详细PR内容
```

### 7.2 文献即真理

- 所有论点必须有文献支持
- 优先使用未引用文献（Uncited/）
- 引用格式：GB/T 7714-2015（作者-年份制）
- 示例：`(Qin et al., 2018)`

### 7.3 PR驱动变更

- 所有 Draft.md 修改必须通过 PR
- 10步验证流程
- 完整历史记录
- 状态追踪：`planning → discussing → approved → merged`

### 7.4 批判性思考

Academic Partner 作为"严格但公正的同行评审者"：
- 质疑假设，挑战论证
- 目标是改进而非否定
- 审查框架：逻辑一致性 + 文献支持充分性 + 方法论强度

---

## 8. 框架对比分析

### 8.1 与 AutoGen 对比

| 维度 | OpenAgents (本系统) | AutoGen |
|------|---------------------|---------|
| 架构模式 | 分层委派 | 对话式协作 |
| Agent通信 | 事件驱动 + 任务委派 | 多轮对话 |
| 记忆系统 | 内置 Mem0 + 本地备份 | 需自行实现 |
| 适用场景 | 结构化工作流 | 开放式讨论 |
| 学习曲线 | 中等 | 较低 |
| 可视化 | Studio UI | 无内置 |

**AutoGen 特点**：
- 基于对话的多Agent协作
- Agent之间通过消息传递
- 适合需要多轮讨论的场景
- 代码优先，灵活性高

**本系统优势**：
- 任务委派模式更适合结构化流程
- 内置记忆系统，无需额外开发
- YAML配置，声明式定义Agent

### 8.2 与 CrewAI 对比

| 维度 | OpenAgents (本系统) | CrewAI |
|------|---------------------|--------|
| 角色定义 | YAML 配置 | Python 代码 |
| 任务编排 | 事件触发 | 顺序/并行 |
| 工具集成 | Mod 系统 | Tool 装饰器 |
| 记忆共享 | 双层架构 | 短期/长期记忆 |
| 灵活性 | 高（可扩展 Mod） | 中等 |

**CrewAI 特点**：
- 角色扮演式Agent定义
- 任务（Task）和流程（Process）分离
- 内置多种记忆类型
- Python代码定义，类型安全

**本系统优势**：
- YAML配置更易维护
- Mod系统扩展性更强
- 双层记忆提供故障转移

### 8.3 与 LangGraph 对比

| 维度 | OpenAgents (本系统) | LangGraph |
|------|---------------------|-----------|
| 核心抽象 | Agent + Mod | 状态图 |
| 流程控制 | 事件驱动 | 图节点 |
| 状态管理 | 记忆系统 | 图状态 |
| 可视化 | Studio UI | 需额外工具 |
| 复杂度 | 中等 | 较高 |

**LangGraph 特点**：
- 基于状态图的流程控制
- 精确的状态转换定义
- 支持循环和条件分支
- 与LangChain生态集成

**本系统优势**：
- 事件驱动更直观
- 不需要定义复杂的状态图
- Studio UI开箱即用

### 8.4 为什么选择 OpenAgents

1. **原生记忆系统**：Mem0 集成开箱即用，无需额外开发
2. **Studio UI**：可视化调试和监控，降低开发难度
3. **Mod 扩展性**：自定义模块无需修改核心代码
4. **YAML 配置**：声明式 Agent 定义，易于维护和版本控制
5. **学术场景适配**：任务委派模式适合结构化研究流程
6. **双层记忆**：Mem0 + MEMORY.md 提供可靠性和可读性

---

## 9. 技术实现细节

### 9.1 OpenAgents 框架集成

```yaml
# 依赖版本
openagents: ">=0.6.11"
mem0ai: ">=0.1.0"
openai: ">=1.0.0"
zhipuai: ">=2.0.0"
```

**Agent 基类**：
- `WorkerAgent`：执行具体任务的Agent
- `CollaboratorAgent`：协调多任务的Agent

**Mod 系统**：
- `openagents.mods.workspace.default`：默认工作空间
- `openagents.mods.workspace.messaging`：消息系统
- `openagents.mods.workspace.project`：项目管理
- `openagents.mods.coordination.task_delegation`：任务委派
- `mods.memory_system`：自定义记忆系统

### 9.2 传输协议配置

```yaml
transports:
  - type: "http"
    config:
      port: 8700
      host: "localhost"
      serve_studio: true
      serve_mcp: true
  - type: "grpc"
    config:
      port: 8600
      max_message_size: 104857600  # 100MB
      compression: "gzip"
```

### 9.3 目录结构

```
academic_network/
├── network.yaml              # 网络配置
├── requirements.txt          # Python 依赖
├── agents/
│   ├── academic_partner.yaml # 协调者 Agent
│   ├── literature_agent.yaml # 文献专家 Agent
│   ├── pr_manager.yaml       # PR 管理 Agent
│   └── archivist.yaml        # 档案管理 Agent
├── mods/
│   └── memory_system.py      # 记忆系统核心
├── tools/
│   ├── document_tools.py     # 文档工具
│   ├── memory_tools.py       # 记忆工具（异步）
│   └── memory_tools_sync.py  # 记忆工具（同步）
├── api/
│   ├── standalone_server.py  # FastAPI 上传服务
│   └── upload_handler.py     # PDF 上传处理
└── qdrant_data/              # 向量数据库存储
```

### 9.4 启动命令

```bash
# 安装依赖
pip install -r academic_network/requirements.txt

# 设置环境变量
export ZHIPU_API_KEY=<your-key>
export OPENAI_API_KEY=<your-key>  # 可选

# 启动网络
python -m openagents network start network.yaml

# 访问 Studio
open http://localhost:8700/studio/
```

---

## 附录：关键文件路径

| 文件 | 用途 |
|------|------|
| `academic_network/network.yaml` | 网络配置 |
| `academic_network/agents/academic_partner.yaml` | 协调者 Agent |
| `academic_network/agents/literature_agent.yaml` | 文献专家 Agent |
| `academic_network/agents/pr_manager.yaml` | PR 管理 Agent |
| `academic_network/agents/archivist.yaml` | 档案管理 Agent |
| `academic_network/mods/memory_system.py` | 记忆系统核心 |
| `academic_network/tools/document_tools.py` | 文档工具 |
| `academic_network/tools/memory_tools.py` | 记忆工具 |
| `MEMORY.md` | 记忆备份文件 |

---

*文档版本: 1.0*
*最后更新: 2026-01-06*
