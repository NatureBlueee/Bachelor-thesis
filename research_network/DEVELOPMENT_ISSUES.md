# OpenAgents 开发问题记录

## 问题 1: pip 版本与源码版本不一致

**现象**: Agent 启动失败，提示 `CollaboratorAgent` 类不存在

**原因**:
- pip 安装的 OpenAgents 0.8.5 版本 API 与 GitHub 源码不同
- pip 版本只有 `SimpleOpenAIAgentRunner` 类
- 源码中的 `CollaboratorAgent`、`WorkerAgent` 等类未发布到 PyPI

**解决方案**: 使用 `SimpleOpenAIAgentRunner` 替代，调整 YAML 配置

---

## 问题 2: 源码安装失败

**现象**: 尝试 `pip install -e .` 安装源码时权限错误

**原因**: macOS 系统 Python 权限限制

**解决方案**: 使用 `--user` 标志或虚拟环境

---

## 问题 3: mcp 模块缺失

**现象**: 使用 PYTHONPATH 方式运行时报错 `No module named 'mcp'`

**原因**:
- OpenAgents 源码依赖 `mcp` 包
- 该包在 PyPI 上不存在或名称不同

**解决方案**: 暂未解决，改用 pip 版本

---

## 问题 4: CLI 命令参数格式错误

**现象**: `openagents launch-agent --config agents/xxx.yaml` 报错

**原因**: `config` 是位置参数，不是选项参数

**正确用法**:
```bash
python3 -m openagents.cli launch-agent agents/academic_partner.yaml
```

---

## 问题 5: YAML 配置格式要求

**现象**: Agent 启动时报错 "config section required"

**原因**: CLI 要求 YAML 必须包含 `config` 节

**解决方案**: 将 `agent_id` 等参数移入 `config` 部分

```yaml
# 错误格式
agent_id: academic_partner
type: openagents.agents...

# 正确格式
type: openagents.agents.simple_openai_agent.SimpleOpenAIAgentRunner
config:
  agent_id: academic_partner
  model_name: gpt-4
  instruction: "..."
```

---

## 问题 6: 缺少 OpenAI API Key

**现象**:
```
ERROR - The api_key client option must be set either by passing api_key
to the client or by setting the OPENAI_API_KEY environment variable
```

**解决方案**:
```bash
export OPENAI_API_KEY="sk-xxx"
```

---

## 问题 7: Network WebSocket 服务器未实际启动

**现象**: Agent 连接失败

**错误信息**:
```
2026-01-06 20:18:32,612 - openagents.core.connector - ERROR - Connection error: [Errno 61] Connect call failed ('127.0.0.1', 8765)
2026-01-06 20:18:32,612 - root - ERROR - Error running agent: Failed to start agent: Failed to connect to server
```

**调试过程**:
1. 启动网络后，日志显示成功：
   ```
   Network 'AcademicResearchNetwork' started successfully
   Transport: TransportType.WEBSOCKET
   Host: 127.0.0.1, Port: 8765
   ```
2. 但检查端口监听状态：
   ```bash
   lsof -i :8765  # 返回空，端口未被监听
   ```
3. 增加等待时间（从 3s 到 5s）后仍然失败

**原因分析**:
- `launch-network` 命令只创建 Python 配置对象，不启动实际的 WebSocket 服务器
- pip 版本 (0.5.1) 的 network launcher 是配置层，不是服务层
- 完整的网络服务可能需要源码版本或额外组件

**尝试的解决方案**:
1. ❌ 增加 sleep 等待时间 - 无效
2. ❌ 检查 Agent YAML 端口配置 - 端口正确但服务不存在
3. ✅ 创建独立运行脚本 `chat.py`，直接使用 OpenAI SDK 绕过网络层

---

## 问题 8: OpenAgents 版本号混乱

**现象**: 官方文档和 GitHub 说版本是 0.8.5，但实际安装后不同

**调试过程**:
```python
import openagents
print(openagents.__version__)  # 输出: 0.5.1

# 检查可用模块
import pkgutil
for importer, modname, ispkg in pkgutil.iter_modules(openagents.__path__):
    print(f'  - {modname}')
# 输出: cli, core, launchers, models, protocols, utils
```

**原因**: PyPI 发布版本落后于 GitHub 源码

**影响**:
- 文档中的 API 可能不存在于 pip 版本
- 示例代码可能无法运行
- 需要根据实际安装版本调整代码

---

## 问题 9: OmniMaaS API 集成

**背景**: 由于 OpenAI API 在国内访问受限，使用 OmniMaaS 作为代理服务

**配置方法**:
```python
from openai import OpenAI
client = OpenAI(
    api_key="your-omnimaas-key",
    base_url="https://api.omnimaas.com/v1"
)
```

**环境变量方式**:
```bash
export OPENAI_API_KEY="your-omnimaas-key"
export OPENAI_BASE_URL="https://api.omnimaas.com/v1"
```

**测试验证**:
```python
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "你好"}],
    max_tokens=10
)
print(resp.choices[0].message.content)  # 输出: OK
```

**注意事项**:
- OmniMaaS 支持 OpenAI SDK 兼容接口
- 模型名称与 OpenAI 官方一致
- API Key 格式: `sk-xxx`

---

## 问题 10: SimpleOpenAIAgentRunner.react() 方法签名复杂

**现象**: 尝试直接调用 Agent 的 react 方法失败

**错误信息**:
```
TypeError: react() missing 2 required positional arguments: 'incoming_thread_id' and 'incoming_message'
```

**调试过程**:
```python
import inspect
print(inspect.signature(SimpleOpenAIAgentRunner.react))
# 输出: (self, message_threads: Dict[str, MessageThread], incoming_thread_id: str, incoming_message: BaseMessage)
```

**原因**: Agent 设计为在网络环境中运行，react 方法需要完整的消息线程上下文

**解决方案**: 不直接使用 Agent 类，改用 OpenAI SDK 直接调用 LLM

---

## 经验总结

1. **版本差异**: 开源项目的 pip 版本可能落后于源码，需先检查 API 兼容性
2. **文档滞后**: 官方文档可能与实际代码不同步，以代码为准
3. **CLI 参数**: 使用 `--help` 确认命令格式
4. **环境变量**: LLM 相关项目通常需要 API Key 环境变量
5. **网络层验证**: 日志显示"成功"不代表服务真正运行，需用 `lsof -i :端口` 验证
6. **API 代理**: 国内环境可使用 OmniMaaS 等兼容 OpenAI SDK 的代理服务
7. **降级方案**: 当框架功能不可用时，直接使用底层 SDK 是有效的替代方案

---

## 最终解决方案

由于 OpenAgents pip 版本 (0.5.1) 的网络层只是配置层，无法实际启动 WebSocket 服务器，最终采用独立脚本方案：

**文件**: `chat.py`

**运行方式**:
```bash
python3 chat.py
```

**功能**: 直接使用 OpenAI SDK 调用 OmniMaaS API，实现学术研究对话助手核心功能

---

## 文档与实际差距分析

### 预期 vs 现实

**预期流程**（按文档应该是这样）：
```bash
pip install openagents          # 安装
openagents init ./my_network    # 初始化
openagents network start        # 启动网络
openagents agent start xxx.yaml # 启动 Agent
# 完成，可以使用
```

**实际情况**：按照文档操作，每一步都遇到问题。

### 文档问题

| 文档声明 | 实际情况 | 影响 |
|---------|---------|------|
| 版本 0.8.5 | pip 安装后是 0.5.1 | API 不一致，示例代码无法运行 |
| `CollaboratorAgent`、`WorkerAgent` 类 | pip 版本只有 `SimpleOpenAIAgentRunner` | 需要重写配置文件 |
| `launch-network` 启动 WebSocket 服务 | 只创建配置对象，不启动服务 | Agent 无法连接 |
| Studio UI 在 localhost:8050 | 未验证，网络层不工作 | 无法使用可视化界面 |

### Demo 可用性

**未测试**：由于 pip 版本与源码版本差异，官方 demo 需要从 GitHub 克隆源码才能运行。

**预期问题**：
1. Demo 可能依赖源码中未发布到 PyPI 的模块
2. Demo 可能需要 `mcp` 等未公开的依赖包
3. Demo 的 YAML 配置格式可能与 pip 版本不兼容

### 根本原因

OpenAgents 项目处于活跃开发阶段：
- PyPI 发布版本 (0.5.1) 严重落后于 GitHub 源码
- 文档描述的是源码功能，不是 pip 版本功能
- 缺少版本兼容性说明

### 建议

1. **使用源码安装**：`pip install git+https://github.com/bestagents/openagents.git`
2. **或等待 PyPI 更新**：等官方发布新版本
3. **或使用替代方案**：直接用 OpenAI SDK 实现核心功能（本项目采用）

---

## 关于本次开发的反思

### 理论上应该如何

如果文档准确，开发流程应该是：
1. 阅读官方文档
2. 参考官方 Demo
3. 按文档步骤执行
4. 系统正常运行

**OpenAgents 文档声称部署很简单**：几条命令即可启动多 Agent 网络。

### 实际发生了什么

| 步骤 | 预期 | 实际 |
|------|------|------|
| `pip install openagents` | 安装 0.8.5 | 安装了 0.5.1 |
| 使用文档中的类 | 正常导入 | 类不存在 |
| `launch-network` | 启动 WebSocket 服务 | 只创建配置对象 |
| Agent 连接网络 | 正常连接 | 连接失败 |

### 问题归因

**不是开发能力问题，而是文档与实际不符**：
- 文档描述的是 GitHub 源码功能
- pip 安装的是落后版本
- 没有版本兼容性说明
- Demo 未验证是否可在 pip 版本运行

### 待验证事项

1. **官方 Demo 是否可用**：克隆源码后，Demo 能否正常运行？
2. **源码安装是否可行**：`pip install git+...` 能否解决依赖问题（如 `mcp` 模块）？
3. **Studio UI 是否存在**：网络层正常后，Studio 是否可访问？

### 结论

当框架文档与实际代码不一致时，应：
1. 先验证最小可行示例（官方 Demo）
2. 确认 pip 版本与文档版本一致
3. 如不一致，考虑源码安装或替代方案

---

## 问题 11: 解决方案 - 使用 Python 3.12 虚拟环境

**问题**: pip 版本 (0.5.1) 功能不完整，源码需要 Python 3.10+

**解决步骤**:
```bash
# 1. 安装 Python 3.12
/opt/homebrew/bin/brew install python@3.12

# 2. 创建虚拟环境
/opt/homebrew/bin/python3.12 -m venv ~/openagents_venv

# 3. 安装 mcp 依赖
~/openagents_venv/bin/pip install mcp

# 4. 从源码安装 OpenAgents
cd /Users/nature/个人项目/Bachelor-thesis/openagents_repo
~/openagents_venv/bin/pip install -e ".[dev]"
```

**验证结果**:
```
Version: 0.8.5.post2
WorkerAgent: <class 'openagents.agents.worker_agent.WorkerAgent'>
CollaboratorAgent: <class 'openagents.agents.collaborator_agent.CollaboratorAgent'>
✅ All imports successful!
```

**Demo 测试成功**:
- Network 启动：HTTP:8700, gRPC:8600 ✅
- Agent 连接：通过 gRPC 连接成功 ✅
- Mod 加载：messaging mod 正常工作 ✅
- 工具注册：7 个工具可用 ✅

**关键命令**:
```bash
# 启动网络
~/openagents_venv/bin/openagents network start network.yaml

# 启动 Agent
export OPENAI_API_KEY="your-key"
export OPENAI_BASE_URL="https://api.omnimaas.com/v1"
~/openagents_venv/bin/openagents agent start agents/xxx.yaml
```

---

## 问题 12: Protobuf 版本冲突 (mem0ai vs grpcio-tools)

**现象**: 网络启动失败，报错 `Detected mismatched Protobuf Gencode/Runtime major versions`

**错误信息**:
```
Unexpected error: Detected mismatched Protobuf Gencode/Runtime major versions
when loading agent_service.proto: gencode 6.31.1 runtime 5.29.5
```

**原因分析**:
- OpenAgents 源码中的 `agent_service_pb2.py` 是用 protobuf 6.31.1 生成的
- `mem0ai` 依赖要求 `protobuf>=5.29.0,<6.0.0`
- `grpcio-tools>=1.70.0` 要求 `protobuf>=6.31.1`
- 两者版本要求互斥

**解决方案**:

1. 安装兼容版本的 grpcio-tools：
```bash
pip install "grpcio-tools>=1.50.0,<1.70.0" "protobuf>=5.29.0,<6.0.0" --force-reinstall
```

2. 重新生成 protobuf 文件（使用 protobuf 5.x）：
```bash
cd openagents_repo/src/openagents/proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. agent_service.proto
```

3. 修复生成文件的导入路径（`agent_service_pb2_grpc.py` 第 6 行）：
```python
# 原来
import agent_service_pb2 as agent__service__pb2
# 改为
from openagents.proto import agent_service_pb2 as agent__service__pb2
```

**验证结果**:
```
✅ OpenAgents network is online
🎨 Studio: http://localhost:8700/studio/
🤖 Agent 'academic-partner' is running!
🤖 Agent 'literature-agent' is running!
```

**兼容版本组合**:
| 包 | 版本 |
|---|---|
| protobuf | 5.29.5 |
| grpcio | 1.76.0 |
| grpcio-tools | 1.69.0 |
| mem0ai | 1.0.1 |

---

## 问题 13: HTTP 传输替代 gRPC

**背景**: 为避免 protobuf 版本冲突，改用 HTTP 传输

**配置修改** (`network.yaml`):
```yaml
transports:
  - type: http
    config:
      port: 8700
      serve_studio: true
      serve_mcp: true
manifest_transport: http
recommended_transport: http  # 原来是 grpc
```

**Agent 配置修改**:
```yaml
connection:
  host: "localhost"
  port: 8700
  transport: "http"  # 原来是 grpc
```

**结果**: HTTP 传输正常工作，无需 gRPC
