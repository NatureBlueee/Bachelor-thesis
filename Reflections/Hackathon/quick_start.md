# OpenAgents Hackathon 快速启动指南

由于自动克隆遇到网络或环境问题，请按照以下步骤手动初始化环境。

## 1. 获取项目代码

请在终端（Terminal）中运行以下命令：

```bash
# 进入项目根目录
cd d:\Profolio\文章\Thesis\Graduate-thesis

# 克隆 OpenAgents 仓库
git clone https://github.com/openagents-org/openagents.git OpenAgents
```

## 2. 环境配置 (推荐使用 Conda)

如果还没有环境，建议创建一个新的 Python 3.12 环境：

```bash
# 创建环境
conda create -n openagents python=3.12 -y

# 激活环境
conda activate openagents
```

## 3. 安装依赖

```bash
# 安装 OpenAgents 包
pip install openagents

# 升级到最新版
pip install -U openagents
```

## 4. 运行 Hello World

一切准备就绪后，尝试运行第一个 Agent 网络：

```bash
# 初始化一个新的网络工作区
openagents init ./my_first_network

# 启动网络（在此终端运行，不要关闭）
openagents network start ./my_first_network
```

然后打开**第二个终端**，运行：

```bash
# 启动 OpenAgents Studio（可视化界面）
openagents studio -s
```

现在你应该能访问 http://localhost:8050 看到你的网络了！

## 5. 验证是否成功

如果你能在 Studio 里看到网络状态，说明环境验证通过。
接下来我们就可以把我们的 **6个 Agent** (Literature, Critical Thinker...) 部署进去了！
