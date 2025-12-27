# Academic Research Network - 架构重设计

## 核心问题

当前设计混淆了三个概念：
- **Workflow（工作流）**：多个 Agent 协作完成一个任务的流程
- **Agent（角色）**：有特定能力和判断力的独立实体
- **Tool（工具）**：Agent 可以调用的具体操作

---

## 从本地系统分析

### 你现有的 9 个工作流

| 工作流 | 本质 | 涉及什么 |
|-------|------|---------|
| `/start` | 状态检查 | 读取文件、输出状态 |
| `/create-pr` | 变更管理 | 写文件、更新索引 |
| `/merge-pr` | 变更管理 + 验证 | 10步检查、写文件、更新多个文件 |
| `/deep-read` | 文献分析 | 读文献、批判评估、输出笔记 |
| `/add-paper` | 文献管理 | PDF转换、写文件、更新索引 |
| `/ask-academic-ai` | 外部查询 | 构造提问、请求 Consensus |
| `/analyze-answer` | 分析整理 | 评估回答、提取引用 |
| `/reflect` | 记忆管理 | 评估对话、更新 MEMORY.md |
| `/sync` | 状态同步 | 检查一致性、更新多个文件 |

### 关键洞见

1. **本地系统只有一个 AI 角色**（你现在用的 Antigravity）
2. **工作流是 AI 的"行为模式"**，不是不同的 AI
3. **真正需要的"能力"**：
   - 理解用户意图
   - 搜索和阅读文献
   - 批判性评估
   - 管理文件（PR、索引等）
   - 记忆和反思

---

## 重新设计：什么才是真正的 Agent？

### Agent 的定义标准

一个独立的 Agent 应该满足：
1. **有独特的专业判断**（不是简单执行命令）
2. **需要持续运行**（响应多个请求）
3. **有自己的"人格"或"立场"**

### 我的建议：只需要 2 个核心 Agent

| Agent | 角色 | 为什么单独存在 |
|-------|------|--------------|
| **Academic Partner** | 主协调者 + 批判伙伴 | 需要理解全局、做判断、协调其他能力 |
| **Literature Specialist** | 文献专家 | 需要专门处理文献搜索、阅读、引用检查 |

**为什么不需要更多 Agent？**

| 原本设想 | 为什么不需要 |
|---------|-------------|
| PR Manager | PR操作是**工具**，不是角色。Academic Partner 调用 `create_pr` 和 `merge_pr` 工具即可 |
| Critical Thinker | 批判性思考是 Academic Partner 的**核心能力**，不需要分离 |
| Method Expert | 方法论建议可以通过 Literature Specialist 提供文献支持 |

---

## 新架构

```
         用户
          ↓
 ┌────────────────────────────────────────────────────┐
 │              Academic Partner (主 Agent)            │
 │                                                     │
 │  能力：                                              │
 │  - 理解用户意图，判断需要什么                         │
 │  - 批判性思考和质疑                                  │
 │  - 协调 Literature Specialist                       │
 │  - 管理对话记忆                                      │
 │                                                     │
 │  工具：                        调用：                │
 │  - create_pr()                                      │
 │  - merge_pr()                 ↓                     │
 │  - update_memory()    ┌───────────────────┐         │
 │  - sync_context()     │ Literature        │         │
 │                       │ Specialist        │         │
 │                       │                   │         │
 │                       │ 工具：            │         │
 │                       │ - search_lit()    │         │
 │                       │ - deep_read()     │         │
 │                       │ - check_citation()│         │
 │                       │ - convert_pdf()   │         │
 │                       └───────────────────┘         │
 └────────────────────────────────────────────────────┘
          ↓
       回复用户
```

---

## 工作流 = Agent 的内部逻辑

用户不需要选择工作流，Academic Partner 自动判断：

| 用户说 | Academic Partner 判断 | 执行的工作流 |
|-------|---------------------|-------------|
| "帮我找关于 Gen Z 的文献" | 文献查询 → 调用 Literature Specialist |
| "我想修改 Introduction" | 论文修改 → 调用 `create_pr` 工具 |
| "合并 PR-0009" | 变更合并 → 调用 `merge_pr` 工具 |
| "这个论点有问题吗？" | 批判审查 → 自己思考 + 可能查文献 |
| "深度阅读 DeRue 2010" | 文献阅读 → 调用 Literature Specialist |

---

## 工具定义

### Academic Partner 的工具

```python
# PR 管理工具
def create_pr(title, original, modified, reason, citations):
    """创建 PR 文件并更新索引"""
    
def merge_pr(pr_id):
    """执行 10 步合并流程"""

# 记忆管理工具
def update_memory(content, category):
    """更新 MEMORY.md"""
    
def check_memory_conflict(statement):
    """检查是否与已有偏好冲突"""

# 状态管理工具
def sync_context():
    """同步 _CONTEXT.md"""

def get_project_status():
    """获取当前项目状态"""
```

### Literature Specialist 的工具

```python
# 文献搜索
def search_literature(query, source="all"):
    """搜索 Reference/Cited 和 Uncited"""

# 文献阅读
def read_file(path):
    """读取文献内容"""

def deep_read(path, focus_on):
    """深度阅读，输出结构化笔记"""

# 引用检查
def check_citations(text):
    """检查文本中的引用是否在 References 中"""

def suggest_citations(topic):
    """为某话题建议可引用文献"""

# PDF 转换
def convert_pdf(path):
    """调用 Datalab API 转换 PDF"""
```

---

## 与 OpenAgents 的映射

| 概念 | OpenAgents 实现 |
|-----|----------------|
| Academic Partner | WorkerAgent (YAML 或 Python) |
| Literature Specialist | WorkerAgent (Python，需要本地文件访问) |
| 用户入口 | Studio 的 **Direct Message** 或 **Channel**，不是 Project |
| 工具 | Agent 的 tools 配置 |
| 工作流 | Agent 的 instruction 中描述，不需要 project_templates |

---

## 下一步

1. **简化 network.yaml**：移除复杂的 agent_groups 和 project_templates
2. **创建 Academic Partner**：整合 Facilitator + Critical Thinker
3. **优化 Literature Specialist**：添加完整的工具集
4. **使用 Messaging 模式**：用户通过 Channel 或 DM 与 Agent 交互

---

## 问题征询

1. 你觉得这个简化后的架构合理吗？
2. 除了 Literature 相关，还有什么能力需要**独立 Agent**？
3. 对于 OpenAgents 的 Project 模式，你还想保留吗？（可以用于特定的复杂任务）
