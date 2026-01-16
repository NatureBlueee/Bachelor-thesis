# Academic Research Network

基于 OpenAgents 框架的学术研究多Agent协作系统。

## 环境要求

- Python 3.10+
- pip3

## 快速开始

### 1. 安装依赖

```bash
pip3 install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 并填入真实的 API Key：

```bash
cp .env.example .env
```

必需的环境变量：

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `OPENAI_API_KEY` | OpenAI 兼容 API Key | `sk-xxx` |
| `OPENAI_BASE_URL` | API 端点 | `https://api.omnimaas.com/v1/messages` |
| `OPENAI_MODEL` | 模型名称 | `claude-sonnet-4-5-20250929` |
| `ZHIPUAI_API_KEY` | 智谱 AI Key（用于 Mem0 embeddings） | `xxx` |

### 3. 启动网络

```bash
# 方式1: 使用启动脚本（推荐）
./start.sh

# 方式2: 手动启动
python3 -m openagents.cli launch-network network.yaml
```

### 4. 启动 Agents

```bash
python3 -m openagents.cli launch-agent agents/academic_partner.yaml
python3 -m openagents.cli launch-agent agents/literature_agent.yaml
```

### 5. 访问 Studio

打开浏览器访问: http://localhost:8700

## Agent 架构

```
┌─────────────────────────────────────────────────────────────┐
│  协调层: Academic Partner                                    │
│  - 统一用户入口                                              │
│  - 批判性思考                                                │
│  - 任务委派                                                  │
├─────────────────────────────────────────────────────────────┤
│  专家层: Literature Agent                                    │
│  - 文献搜索                                                  │
│  - 深度阅读                                                  │
│  - 引用建议                                                  │
└─────────────────────────────────────────────────────────────┘
```

## 目录结构

```
research_network/
├── network.yaml              # 网络配置
├── requirements.txt          # Python 依赖
├── start.sh                  # 启动脚本
├── agents/
│   ├── academic_partner.yaml # 协调者（记忆工具）
│   └── literature_agent.yaml # 文献专家（文献+学术搜索工具）
├── mods/
│   └── memory_system.py      # Mem0 + MEMORY.md 双层记忆
├── tools/
│   ├── memory_tools.py       # 记忆工具
│   ├── document_tools.py     # 本地文献工具
│   └── academic_search.py    # 学术搜索 API
└── qdrant_data/              # 向量数据库存储
```

## 工具说明

### Academic Partner 工具
| 工具 | 功能 |
|------|------|
| `add_memory` | 添加记忆（偏好/决策/洞见/约束/纠正） |
| `search_memory` | 语义搜索相关记忆 |

### Literature Agent 工具
| 工具 | 功能 |
|------|------|
| `search_literature` | 搜索本地 Reference/ 文献库 |
| `read_file` | 读取文献内容 |
| `list_literature` | 列出所有文献 |
| `search_academic` | 搜索 CrossRef + OpenAlex 学术数据库 |

## 工作流

1. **论文修改流程**: PR-driven 的论文修改
2. **深度阅读流程**: 博士生式深度阅读
3. **学术讨论流程**: 探索性学术问题讨论
