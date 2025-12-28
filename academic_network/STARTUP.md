# Academic Research Network 启动指南

## 环境准备

每次打开新终端，需要先设置环境变量并切换目录：

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:Path += ";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"
```

---

## 快速启动

### 方法 1：一键脚本（推荐）

双击运行：
```
academic_network/start_network.bat
```

### 方法 2：手动启动

**步骤 1：启动网络（窗口1）**
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:Path += ";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"
openagents network start network.yaml
```

**步骤 2：启动 Agent（每个 Agent 一个新窗口）**

每个窗口都要先执行：
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:Path += ";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"
```

然后启动对应 Agent：

| Agent | 启动命令 |
|-------|---------|
| Academic Partner | `openagents agent start agents/academic_partner.yaml` |
| Literature Agent | `openagents agent start agents/literature_agent.yaml` |
| PR Manager | `openagents agent start agents/pr_manager.yaml` |
| Archivist | `openagents agent start agents/archivist.yaml` |

**最小启动**：只需启动 `academic_partner.yaml` 即可进行基本对话。

**步骤 3：打开 Studio**
```
http://localhost:8700/studio/
```

---

## 完整启动命令（复制即用）

### 窗口1 - 网络
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network; $env:PYTHONUTF8="1"; $env:Path+=";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"; openagents network start network.yaml
```

### 窗口2 - Academic Partner
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network; $env:PYTHONUTF8="1"; $env:Path+=";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"; openagents agent start agents/academic_partner.yaml
```

### 窗口3 - Literature Agent
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network; $env:PYTHONUTF8="1"; $env:Path+=";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"; openagents agent start agents/literature_agent.yaml
```

### 窗口4 - PR Manager
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network; $env:PYTHONUTF8="1"; $env:Path+=";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"; openagents agent start agents/pr_manager.yaml
```

### 窗口5 - Archivist
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network; $env:PYTHONUTF8="1"; $env:Path+=";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"; openagents agent start agents/archivist.yaml
```

---

## Agent 架构

```
用户 ──> Academic Partner (入口)
              │
              ├──> Literature Agent (文献专家)
              ├──> PR Manager (变更管理)
              └──> Archivist (档案管理)
```

| Agent | 职责 |
|-------|------|
| **Academic Partner** | 统一入口，批判性思考，任务委派 |
| **Literature Agent** | 文献搜索、深度阅读、引用建议 |
| **PR Manager** | PR 创建、验证、合并 |
| **Archivist** | 文件操作执行 |

---

## 备用命令

如果 `openagents` 命令找不到：

```powershell
python -m openagents.cli network start network.yaml
python -m openagents.cli agent start agents/academic_partner.yaml
```

---

## API 配置

| 配置项 | 值 |
|-------|-----|
| Provider | 智谱 (Zhipu) |
| Model | `glm-4.5-flash` |
| API Base | `https://open.bigmodel.cn/api/paas/v4` |

---

## 启动日志

日志文件：`academic_network/startup.log`
