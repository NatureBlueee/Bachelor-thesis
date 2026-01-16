# Academic Network 架构文档

> 此文档记录系统架构、文件位置、已知问题，供开发时参考。

## 系统概览

```
用户 <---> Academic Partner (协调者/批判者)
                |
                ├── Literature Agent (文献专家)
                ├── PR Manager (变更管理)
                └── Archivist (档案管理)
```

## 文件结构

```
academic_network/
├── network.yaml              # 网络配置 (端口、mods、模板)
├── start_all.sh              # 一键启动脚本
├── ARCHITECTURE.md           # 本文档
│
├── agents/                   # Agent 配置
│   ├── academic_partner.yaml # 协调者 (有 LLM + 记忆工具)
│   ├── literature_agent.yaml # 文献专家 (有 LLM，需要文献工具)
│   ├── literature_agent.py   # 文献专家 Python 版 (有文献工具，无法启动)
│   ├── pr_manager.yaml       # PR 管理
│   └── archivist.yaml        # 档案管理
│
├── tools/                    # 自定义工具
│   ├── document_tools.py     # 文献搜索 (异步版)
│   ├── document_tools_sync.py# 文献搜索 (同步版，供 YAML Agent)
│   ├── memory_tools.py       # 记忆工具 (异步版)
│   └── memory_tools_sync.py  # 记忆工具 (同步版)
│
├── mods/                     # 自定义 Mods
│   └── memory_system.py      # Mem0 记忆系统 (加载失败)
│
└── 日志位置
    /tmp/network.log
    /tmp/academic_partner.log
    /tmp/literature_agent.log
    /tmp/pr_manager.log
    /tmp/archivist.log
```

## Agent 职责

| Agent | 类型 | 职责 | 工具 |
|-------|------|------|------|
| academic-partner | CollaboratorAgent | 与用户对话，批判性思考，委派任务 | add_memory, search_memory, delegate_task |
| literature-agent | WorkerAgent | 搜索文献，深度阅读，建议引用 | **需要**: search_literature, read_literature |
| pr-manager | WorkerAgent | 创建/验证 PR | 文件操作 |
| archivist | WorkerAgent | 执行文件修改 | 文件操作 |

## 已知问题

### 1. Literature Agent 无法搜索真实文献
- **现象**: 返回 LLM 编造的假文献
- **原因**: YAML 版本没有配置 document_tools
- **解决**: ✅ 已在 literature_agent.yaml 添加 tools 配置
- **验证**: 日志显示 "Loaded 3 custom tools from agent config"

### 2. Python 版 Literature Agent 无法启动
- **现象**: "Failed to connect to server"
- **原因**: 可能是 gRPC 连接问题，旧注册信息未清理
- **临时方案**: 使用 YAML 版本

### 3. Memory System Mod 加载失败
- **现象**: "No module named 'mods.memory_system'"
- **原因**: 路径问题
- **影响**: 不影响核心功能，记忆通过 tools 实现

## Agent 人设设计原则

### 问题
当前 Agent 太"听话"，不会追问用户真正需求。

### 改进方向
1. **批判性思考**: 不是用户说什么就做什么，要先理解为什么
2. **主动追问**: 遇到模糊需求时，先问清楚再行动
3. **挖掘意图**: "你想搜索文献" → "你想解决什么问题？需要什么类型的文献？"

### 人设关键词
- Academic Partner: 批判性学术伙伴，会挑战假设，追问动机
- Literature Agent: 博士生式阅读，不只是搜索，要理解研究关联

## 启动命令

```bash
cd academic_network
./start_all.sh
```

## 访问地址

- Studio UI: http://localhost:8700/studio
- Health API: http://localhost:8700/api/health

## 待办事项

- [ ] 给 literature_agent.yaml 添加 document_tools
- [ ] 改进 academic_partner 人设，增加追问能力
- [ ] 修复 Python 版 literature_agent.py 启动问题
- [ ] 修复 memory_system mod 加载问题
