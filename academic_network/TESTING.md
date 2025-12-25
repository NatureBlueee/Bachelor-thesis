# Academic Research Network - 测试与验证指南

> 版本: 1.0 | 日期: 2025-12-25
> 目的: 逐步验证系统各组件正常工作

---

## 第一步：环境检查

### 1.1 检查 Python 环境

```powershell
# 检查 Python 版本
python --version
# 应该显示 Python 3.10 或更高

# 检查 OpenAgents 是否安装
python -c "import openagents; print(f'OpenAgents v{openagents.__version__}')"
```

### 1.2 检查依赖

```powershell
# 安装依赖
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
pip install -r requirements.txt

# 验证 Mem0
python -c "from mem0 import Memory; print('Mem0 OK')"
```

### 1.3 设置 API Key

```powershell
# 设置 OpenAI API Key
$env:OPENAI_API_KEY = "your-openai-api-key-here"

# 验证
echo $env:OPENAI_API_KEY
```

---

## 第二步：启动网络

### 2.1 启动 OpenAgents 网络

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
python -m openagents network start network.yaml
```

**预期输出**：
```
[INFO] Starting OpenAgents network...
[INFO] Network 'AcademicResearchNetwork' started on port 8700
[INFO] Studio available at http://localhost:8700/studio/
```

### 2.2 验证网络

打开浏览器访问: http://localhost:8700/studio/

**应该看到**：
- OpenAgents Studio 界面
- 网络状态显示 "Connected"
- 暂时没有 Agent（因为还没启动）

---

## 第三步：启动 Agents

**在新的 PowerShell 窗口中执行每个命令**

### 3.1 启动 Facilitator

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:OPENAI_API_KEY = "your-key"
python -m openagents launch-agent agents/facilitator.yaml
```

### 3.2 启动 Literature Agent (Python 版本)

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:OPENAI_API_KEY = "your-key"
python agents/literature_agent.py
```

### 3.3 启动 Critical Thinker

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:OPENAI_API_KEY = "your-key"
python -m openagents launch-agent agents/critical_thinker.yaml
```

### 3.4 启动 PR Manager

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:OPENAI_API_KEY = "your-key"
python -m openagents launch-agent agents/pr_manager.yaml
```

### 3.5 验证 Agents

在 Studio 中应该能看到 4 个 Agent：
- `facilitator`
- `literature-agent`
- `critical-thinker`
- `pr-manager`

---

## 第四步：功能测试

### 4.1 测试频道消息

在 Studio 中：
1. 进入 `general` 频道
2. 发送消息："Hello, is anyone there?"
3. 观察是否有 Agent 响应

### 4.2 测试 Literature Agent

在 `literature` 频道中：
1. 发送消息："AI literacy"
2. Literature Agent 应该返回搜索结果

### 4.3 测试完整工作流

1. 在 Studio 中创建新 Project
2. 选择模板 "thesis_modification"
3. 输入目标："帮我找关于 AI 素养的文献"
4. 观察 Agent 协作过程

---

## 第五步：一键启动（验证通过后使用）

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis
.\start_academic_network.ps1
```

---

## 常见问题

### Q1: "openagents" 命令找不到

**解决**：
```powershell
# 使用 python -m 方式
python -m openagents network start network.yaml
```

### Q2: 网络启动后 Agent 连接失败

**检查**：
- 网络是否在 8700 端口运行
- Agent 的 connection 配置是否正确

### Q3: LLM 调用失败

**检查**：
- OPENAI_API_KEY 是否设置
- API Key 是否有效

### Q4: 中文显示乱码

**解决**：
```powershell
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

### Q5: Literature Agent 找不到文献

**检查**：
- `Reference/Cited/` 和 `Reference/Uncited/` 目录是否存在
- 目录中是否有 `.md` 文件

---

## 测试检查清单

- [ ] Python 环境正确 (3.10+)
- [ ] 依赖安装成功 (openagents, mem0ai)
- [ ] OPENAI_API_KEY 已设置
- [ ] 网络启动成功 (port 8700)
- [ ] Studio 可访问
- [ ] Facilitator 连接成功
- [ ] Literature Agent 连接成功
- [ ] Critical Thinker 连接成功
- [ ] PR Manager 连接成功
- [ ] 频道消息测试通过
- [ ] 文献搜索测试通过
- [ ] 完整工作流测试通过

---

## 成功标准

当以下条件全部满足时，系统验证通过：

1. **网络运行正常**：Studio 可访问，显示网络状态
2. **所有 Agent 在线**：4 个 Agent 都显示为 Connected
3. **消息传递正常**：频道中发送的消息能被 Agent 接收和响应
4. **文献搜索正常**：Literature Agent 能搜索本地文献库
5. **工作流执行正常**：多 Agent 协作流程能正常完成
