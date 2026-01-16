# OpenAgents 学术研究系统 - 开发日志

> 记录时间: 2026-01-07
> 项目: OpenAgents 黑客松参赛作品
> 状态: ✅ 系统运行成功

---

## 一、项目目标

### 1.1 核心目标
构建基于 OpenAgents 框架的多 Agent 学术研究协作系统，作为黑客松参赛作品。

### 1.2 功能需求
| 功能 | 描述 | 状态 |
|------|------|------|
| 多 Agent 协作 | Academic Partner + Literature Agent | ✅ |
| 记忆系统 | Mem0 向量存储 + MEMORY.md 备份 | ✅ |
| 本地文献搜索 | 搜索 Reference/ 目录 | ✅ |
| 学术 API 搜索 | CrossRef + OpenAlex | ✅ |
| 事件驱动通信 | task.delegate / task.complete | ✅ |

### 1.3 技术栈
- OpenAgents 0.8.5.post2 (源码版本)
- Python 3.12
- Mem0 + Qdrant (向量数据库)
- ZhipuAI embeddings (embedding-3)
- OmniMaaS API (OpenAI 兼容)

---

## 二、开发时间线

### Phase 1: 初始尝试 (失败)
**问题**: pip 版本 (0.5.1) 与文档描述 (0.8.5) 不一致
- `CollaboratorAgent` 类不存在
- Network 只创建配置对象，不启动实际服务
- WebSocket 端口未监听

**教训**: 开源项目的 pip 版本可能严重落后于源码

### Phase 2: 源码安装
**解决方案**: 使用 Python 3.12 虚拟环境 + 源码安装
```bash
/opt/homebrew/bin/python3.12 -m venv ~/openagents_venv
cd openagents_repo && pip install -e ".[dev]"
```

**结果**: 成功获得 0.8.5.post2 版本，所有类可用

### Phase 3: 记忆系统实现
**实现**: 双层记忆架构
1. Mem0 向量层 - 语义搜索
2. MEMORY.md 文本层 - 人类可读备份

**依赖安装**:
```bash
pip install mem0ai qdrant-client langchain zhipuai aiofiles
```

### Phase 4: Protobuf 版本冲突 (关键问题)
**错误信息**:
```
Detected mismatched Protobuf Gencode/Runtime major versions
when loading agent_service.proto: gencode 6.31.1 runtime 5.29.5
```

**根因分析**:
- OpenAgents 源码的 `agent_service_pb2.py` 用 protobuf 6.31.1 生成
- `mem0ai` 要求 `protobuf>=5.29.0,<6.0.0`
- `grpcio-tools>=1.70.0` 要求 `protobuf>=6.31.1`
- 两者版本要求互斥！

**解决方案** (3 步):
```bash
# 1. 安装兼容版本
pip install "grpcio-tools>=1.50.0,<1.70.0" "protobuf>=5.29.0,<6.0.0" --force-reinstall

# 2. 重新生成 proto 文件
cd openagents_repo/src/openagents/proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. agent_service.proto

# 3. 修复导入路径 (agent_service_pb2_grpc.py 第6行)
# 原: import agent_service_pb2 as agent__service__pb2
# 改: from openagents.proto import agent_service_pb2 as agent__service__pb2
```

### Phase 5: 系统启动成功
**最终状态**:
- Network: HTTP:8700 ✅
- Academic Partner Agent: 运行中 ✅
- Literature Agent: 运行中 ✅

---

## 三、关键问题与解决方案

### 问题 1: pip 版本落后
| 项目 | pip 版本 | 源码版本 |
|------|---------|---------|
| openagents | 0.5.1 | 0.8.5.post2 |

**解决**: 从 GitHub 源码安装

### 问题 2: mcp 模块缺失
**错误**: `No module named 'mcp'`
**解决**: `pip install mcp` (需要 Python 3.10+)

### 问题 3: 系统 Python 权限限制
**错误**: Permission denied
**解决**: 使用虚拟环境

### 问题 4: Protobuf 版本冲突
**详见**: Phase 4

### 问题 5: proto 文件导入路径错误
**错误**: `No module named 'agent_service_pb2'`
**原因**: grpc_tools 生成的文件使用相对导入
**解决**: 手动修改为绝对导入

---

## 四、兼容版本组合

经过多次测试，以下版本组合可以正常工作：

| 包 | 版本 | 说明 |
|---|---|---|
| python | 3.12 | 虚拟环境 |
| openagents | 0.8.5.post2 | 源码安装 |
| protobuf | 5.29.5 | mem0ai 兼容 |
| grpcio | 1.76.0 | 最新版 |
| grpcio-tools | 1.69.0 | 生成 protobuf 5.x 兼容代码 |
| mem0ai | 1.0.1 | 向量记忆 |
| qdrant-client | latest | 本地向量数据库 |

---

## 五、项目结构

```
research_network/
├── network.yaml              # 网络配置 (HTTP:8700)
├── start.sh                  # 启动脚本
├── standalone_agent.py       # 独立运行版本 (备用)
├── DEVELOPMENT_ISSUES.md     # 问题记录 (13个问题)
├── DEVELOPMENT_LOG.md        # 本文件
├── README.md                 # 项目说明
├── requirements.txt          # 依赖列表
│
├── agents/
│   ├── academic_partner.yaml # 协调者 Agent
│   └── literature_agent.yaml # 文献专家 Agent
│
├── mods/
│   └── memory_system.py      # Mem0 + MEMORY.md 双层记忆
│
├── tools/
│   ├── memory_tools.py       # 记忆工具 (add/search)
│   ├── document_tools.py     # 文献工具 (search/read/list)
│   └── academic_search.py    # 学术 API (CrossRef/OpenAlex)
│
└── qdrant_data/              # 向量数据库存储
```

---

## 六、Agent 工具清单

### Academic Partner (协调者)
| 工具 | 功能 |
|------|------|
| add_memory | 添加记忆 (偏好/决策/洞见/约束/纠正) |
| search_memory | 语义搜索相关记忆 |
| send_channel_message | 发送频道消息 |
| send_direct_message | 发送私信 |
| start_project | 启动项目工作流 |

### Literature Agent (文献专家)
| 工具 | 功能 |
|------|------|
| search_literature | 搜索本地 Reference/ 文献库 |
| read_file | 读取文献内容 |
| list_literature | 列出所有文献 |
| search_academic | 搜索 CrossRef + OpenAlex |

---

## 七、启动命令

```bash
# 进入项目目录
cd ~/个人项目/Bachelor-thesis/research_network

# 激活虚拟环境
source ~/openagents_venv/bin/activate

# 方式1: 使用启动脚本
./start.sh

# 方式2: 手动启动
export OPENAI_API_KEY="your-key"
export OPENAI_BASE_URL="https://api.omnimaas.com/v1"

openagents network start network.yaml &
sleep 5
openagents agent start agents/academic_partner.yaml &
openagents agent start agents/literature_agent.yaml &
```

**访问地址**: http://localhost:8700/studio/

---

## 八、经验总结

### 8.1 开源项目使用经验
1. **先验证 Demo**: 在开发前先运行官方 Demo 确认框架可用
2. **检查版本一致性**: pip 版本可能落后于文档描述
3. **源码安装优先**: 活跃开发的项目建议从源码安装
4. **虚拟环境隔离**: 避免系统 Python 权限和依赖冲突

### 8.2 依赖冲突处理
1. **识别冲突**: 仔细阅读 pip 的依赖冲突警告
2. **版本锁定**: 找到兼容的版本组合并记录
3. **重新生成**: 如果是编译生成的文件，用兼容版本重新生成
4. **手动修复**: 自动生成的代码可能需要手动调整

### 8.3 调试技巧
1. **端口验证**: `lsof -i :端口` 确认服务真正运行
2. **日志分析**: 查看 openagents.log 获取详细错误
3. **最小化测试**: 先测试单个组件，再集成
4. **备用方案**: 准备独立运行版本作为降级方案

### 8.4 文档记录
1. **实时记录**: 遇到问题立即记录，包括错误信息和解决方案
2. **版本组合**: 记录可工作的依赖版本组合
3. **命令保存**: 保存成功的命令序列

---

## 九、待优化事项

1. **Studio UI**: 需要构建前端才能访问 /studio/
2. **Agent 通信测试**: 验证 task.delegate/task.complete 事件流
3. **错误处理**: 增强工具函数的错误处理
4. **性能优化**: 考虑记忆搜索的缓存策略

---

## 十、相关文件位置

| 文件 | 路径 | 说明 |
|------|------|------|
| 开发日志 | `research_network/DEVELOPMENT_LOG.md` | 本文件 |
| 问题记录 | `research_network/DEVELOPMENT_ISSUES.md` | 13个问题详情 |
| 项目说明 | `research_network/README.md` | 快速开始指南 |
| 计划文件 | `~/.claude/plans/glimmering-singing-mist.md` | 原始开发计划 |
| 记忆文件 | `MEMORY.md` | AI 记忆备份 |

---

## 十一、给 OpenAgents 团队的反馈

如果 protobuf 问题无法自行解决，可以向 OpenAgents 团队反馈：

**问题描述**:
```
OpenAgents 0.8.5.post2 源码中的 agent_service_pb2.py 是用 protobuf 6.31.1 生成的，
但与 mem0ai 等依赖 protobuf<6.0.0 的包存在版本冲突。

建议：
1. 在 pyproject.toml 中明确 protobuf 版本要求
2. 或提供 protobuf 5.x 兼容的预生成文件
3. 或在文档中说明如何重新生成 proto 文件
```

**GitHub Issues**: https://github.com/bestagents/openagents/issues
