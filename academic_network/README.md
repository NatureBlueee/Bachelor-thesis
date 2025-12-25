# Academic Research Network

基于 OpenAgents 的学术研究多Agent协作系统。

## 快速开始

### 1. 安装依赖

```powershell
cd academic_network
pip install -r requirements.txt
```

### 2. 设置环境变量

```powershell
$env:OPENAI_API_KEY = "your-openai-api-key"
```

### 3. 启动网络

```powershell
# 一键启动
.\start_academic_network.ps1

# 或者手动启动
cd academic_network
python -m openagents network start network.yaml
```

### 4. 访问 Studio

打开浏览器访问: http://localhost:8700/studio/

## Agent 架构

```
┌─────────────────────────────────────────────────────────────┐
│                   Academic Research Network                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐│
│  │Facilitator│  │Literature │  │  Critical │  │    PR     ││
│  │(协调者)   │  │  Agent    │  │  Thinker  │  │  Manager  ││
│  │           │  │(文献专家) │  │ (批判者)  │  │(变更管理) ││
│  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘│
│        │              │              │              │       │
│        └──────────────┴──────────────┴──────────────┘       │
│                          ↕                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    Mem0 记忆系统                         ││
│  │   • 自动捕捉偏好和洞见                                   ││
│  │   • 冲突检测和确认                                       ││
│  │   • 同步到 MEMORY.md                                     ││
│  └─────────────────────────────────────────────────────────┘│
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 核心特性

### 1. 负面约束设计
告诉 Agent "不能做什么" 比 "应该做什么" 更重要：
- ❌ 不直接编辑 Draft.md（必须通过 PR）
- ❌ 不凭空编造文献（必须来自 Reference/）
- ❌ 不跳过批判性审查

### 2. PR 驱动变更
所有论文修改通过 Pull Request：
- 10 步验证流程
- 强制引用检查
- 完整历史记录

### 3. 智能记忆系统
基于 Mem0 的记忆层：
- 自动提取用户偏好和洞见
- 检测偏好冲突并主动确认
- 每次讨论产出可追溯的结果

### 4. 文献工具链
- PDF → Markdown 转换 (Datalab API)
- 优先搜索未引用文献
- 自动引用检查

## 目录结构

```
academic_network/
├── network.yaml          # 网络配置
├── requirements.txt      # Python 依赖
├── agents/               # Agent 定义
│   ├── facilitator.yaml
│   ├── literature_agent.yaml
│   ├── critical_thinker.yaml
│   └── pr_manager.yaml
├── mods/                 # 自定义模块
│   └── memory_system.py
└── tools/                # 工具集
    └── document_tools.py
```

## 工作流模板

| 模板 | 用途 |
|------|------|
| thesis_modification | 论文修改流程 |
| deep_reading | 深度阅读文献 |
| academic_discussion | 学术问题讨论 |

## 与现有系统的集成

本系统与现有的论文协作系统完全兼容：
- 使用相同的 `Reference/` 文献库
- 使用相同的 `PR/` 系统
- 使用相同的 `MEMORY.md`
- 支持现有的 9 个工作流

## 下一步

- [ ] 测试 Agent 基础协作
- [ ] 验证 Mem0 记忆功能
- [ ] 录制演示视频
- [ ] 准备 Hackathon 提交
