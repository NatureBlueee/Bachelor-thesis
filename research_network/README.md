# Academic Research Network

> OpenAgents Hackathon Demo - 学术研究多智能体协作系统

## 1. 项目概述

**项目名称**: Academic Research Network
**Network ID**: `academic-research-network`
**一句话介绍**: 基于 OpenAgents 框架的学术研究协作系统，通过多智能体协作帮助研究者进行文献管理、学术搜索和研究偏好记忆。

**目标用户**:
- 本科/研究生论文写作者
- 学术研究人员
- 需要文献管理和学术讨论支持的用户

## 2. 技术架构

**技术栈**:
- 后端: Python 3.9+ / Flask
- LLM: Claude (via OmniMaaS/Bedrock API)
- 向量存储: Qdrant (Mem0)
- 嵌入模型: Zhipu AI embedding-3
- 学术 API: CrossRef + OpenAlex

**架构设计**:

```
┌─────────────────────────────────────────────────────────────┐
│                    Web UI (Flask)                           │
│                  http://localhost:5001                      │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│              Academic Partner Agent                          │
│         (协调者 - 带工具调用的对话系统)                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────▼───────┐ ┌───▼───┐ ┌───────▼───────┐
│  Memory Mod   │ │ Tools │ │ Academic APIs │
│ (Mem0+MD双层) │ │       │ │ CrossRef/OA   │
└───────────────┘ └───────┘ └───────────────┘
```

**核心组件**:
- `demo_server.py` - Flask 服务器，处理 HTTP 请求和工具调用
- `mods/memory_tools_sync.py` - 双层记忆系统 (Mem0 向量 + MEMORY.md 文件)
- `tools/document_tools.py` - 本地文献搜索和读取
- `tools/academic_search.py` - 外部学术数据库搜索

## 3. 智能体设计

### Agent 角色

| Agent | 职责 | 工具 |
|-------|------|------|
| Academic Partner | 主协调者，处理用户对话，调用工具 | 全部 5 个工具 |
| Literature Agent | 文献专家 (待命状态) | search_literature, read_literature |

### 工具列表

| 工具名 | 功能 | 数据源 |
|--------|------|--------|
| `add_memory` | 记住用户偏好、决策、洞见 | Mem0 + MEMORY.md |
| `search_memory` | 语义搜索相关记忆 | Mem0 向量库 |
| `search_literature` | 搜索本地文献库 | Reference/ 目录 |
| `read_literature` | 读取文献内容 | 本地 Markdown 文件 |
| `search_academic` | 搜索学术数据库 | CrossRef + OpenAlex |

### Mod 使用

**Memory Mod (双层记忆系统)**:
- 第一层: Mem0 + Qdrant 向量存储，支持语义搜索
- 第二层: MEMORY.md 文件备份，人类可读
- 自动分类: preference / decision / insight / constraint

## 4. 协作场景与创新点

### 典型协作场景

**场景 1: 文献研究**
```
用户: 搜索关于 AI literacy 的文献
Agent: [调用 search_literature] → 返回本地文献库匹配结果
Agent: [调用 search_academic] → 补充外部学术数据库结果
```

**场景 2: 偏好记忆**
```
用户: 记住：我偏好使用资源依赖理论
Agent: [调用 add_memory] → 存储到 Mem0 + MEMORY.md
...后续对话...
用户: 我之前说过什么偏好？
Agent: [调用 search_memory] → 语义检索相关记忆
```

**场景 3: 学术讨论**
```
用户: 向上影响行为有哪些类型？
Agent: [调用 search_academic] → 获取最新研究
Agent: 基于文献进行批判性讨论
```

### 创新点

1. **双层记忆架构**: Mem0 向量搜索 + MEMORY.md 人类可读备份，兼顾效率和可解释性
2. **本地+云端文献融合**: 本地 Reference/ 文献库 + CrossRef/OpenAlex API
3. **批判性学术伙伴**: 不只是回答问题，而是质疑假设、挑战论证
4. **Bedrock API 兼容**: 解决了 `content=None` 导致的 API 错误

## 5. 实际应用价值

### 解决的问题

1. **文献管理碎片化**: 统一管理本地文献和在线搜索
2. **研究偏好遗忘**: 通过记忆系统保持长期研究上下文
3. **学术讨论缺乏批判性**: Agent 主动质疑和挑战，而非简单附和

### 可扩展性

- 可添加更多 Agent (如 Writing Agent, Review Agent)
- 可接入更多学术 API (Semantic Scholar, PubMed)
- 可扩展到团队协作场景

## 6. 开发、发布与使用说明

### 环境要求

- Python 3.9+
- pip 包管理器

### 安装步骤

```bash
# 1. 进入项目目录
cd research_network

# 2. 安装依赖
pip install flask flask-cors openai requests

# 3. 配置环境变量 (创建 .env 文件)
cat > .env << EOF
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.omnimaas.com/v1
OPENAI_MODEL=claude-sonnet-4-5-20250929
ZHIPUAI_API_KEY=your_zhipu_key  # 可选，用于 Mem0 嵌入
EOF

# 4. 启动服务器
export $(grep -v '^#' .env | xargs) && python3 demo_server.py
```

### 使用方式

1. 打开浏览器访问 http://localhost:5001
2. 在聊天框输入问题或使用快速测试按钮
3. 右侧面板显示 Agent 状态和工具调用日志

### API 端点

| 端点 | 方法 | 功能 |
|------|------|------|
| `/` | GET | Web UI |
| `/api/chat` | POST | 对话接口 |
| `/api/tools` | GET | 工具列表 |

## 7. 团队与分工

| 成员 | 角色 | 职责 |
|------|------|------|
| 张晨曦 | 项目负责人 / 开发者 | 系统设计、代码实现、文档编写 |

## 8. 遇到的挑战与解决方案

### 挑战 1: Bedrock API 兼容性

**问题**: OmniMaaS/Bedrock API 拒绝 `content=None` 的 assistant 消息
```
ValidationException: messages: text content blocks must be non-empty
```

**解决方案**: 确保 assistant 消息内容永不为空
```python
assistant_msg = {
    "role": "assistant",
    "content": msg.content or "Calling tools...",  # 关键修复
    "tool_calls": [...]
}
```

### 挑战 2: 工具返回空结果

**问题**: 某些工具返回空结果导致 API 错误

**解决方案**: 在 `call_tool` 函数中确保非空返回
```python
if not result:
    return {"status": "ok", "message": "No results found"}
```

### 挑战 3: Mem0 初始化失败

**问题**: 缺少 ZHIPUAI_API_KEY 时 Mem0 无法初始化

**解决方案**: 优雅降级到纯 MEMORY.md 模式，打印警告但不中断服务

## 9. 未来展望

### 短期计划

- [ ] 添加 Literature Agent 独立处理文献任务
- [ ] 支持 PDF 上传和自动解析
- [ ] 增加引用格式化工具

### 中期计划

- [ ] 多用户会话隔离
- [ ] 文献知识图谱构建
- [ ] 写作辅助 Agent

### 长期愿景

构建完整的学术研究协作平台，支持从文献阅读、笔记整理、论文写作到同行评审的全流程 AI 辅助。

---

**Demo 地址**: http://localhost:5001
**License**: MIT
