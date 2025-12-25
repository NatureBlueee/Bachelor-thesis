# Academic Research Network - 启动脚本
# 一键启动 OpenAgents 网络、所有 Agent 和 Studio

param(
    [switch]$SkipNetwork,
    [switch]$SkipAgents,
    [switch]$SkipStudio
)

# 设置 UTF-8 编码
$env:PYTHONUTF8 = "1"
$OutputEncoding = [System.Text.Encoding]::UTF8

# 颜色输出
function Write-Color($Text, $Color = "White") {
    Write-Host $Text -ForegroundColor $Color
}

# 项目路径
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$NETWORK_DIR = Join-Path $SCRIPT_DIR "academic_network"

Write-Color "========================================" "Cyan"
Write-Color "  Academic Research Network 启动器" "Cyan"
Write-Color "========================================" "Cyan"
Write-Color ""

# 检查环境变量
if (-not $env:OPENAI_API_KEY) {
    Write-Color "[!] 警告: OPENAI_API_KEY 未设置" "Yellow"
    Write-Color "    请设置: `$env:OPENAI_API_KEY = 'your-key'" "Yellow"
    Write-Color ""
}

# 检查目录
if (-not (Test-Path $NETWORK_DIR)) {
    Write-Color "[!] 错误: 找不到 academic_network 目录" "Red"
    exit 1
}

Write-Color "[*] 项目目录: $NETWORK_DIR" "Gray"
Write-Color ""

# 步骤 1: 启动网络
if (-not $SkipNetwork) {
    Write-Color "[1/5] 启动 OpenAgents 网络..." "Green"
    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "Set-Location '$NETWORK_DIR'; `$env:PYTHONUTF8='1'; Write-Host '=== OpenAgents Network ===' -ForegroundColor Cyan; python -m openagents network start network.yaml"
    ) -WindowStyle Normal
    Start-Sleep -Seconds 5
}
else {
    Write-Color "[1/5] 跳过网络启动" "Gray"
}

if (-not $SkipAgents) {
    # 步骤 2: 启动 Facilitator
    Write-Color "[2/5] 启动 Facilitator Agent..." "Green"
    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "Set-Location '$NETWORK_DIR'; `$env:PYTHONUTF8='1'; Write-Host '=== Facilitator Agent ===' -ForegroundColor Yellow; python -m openagents launch-agent agents/facilitator.yaml"
    ) -WindowStyle Normal
    Start-Sleep -Seconds 2

    # 步骤 3: 启动 Literature Agent (Python 版本)
    Write-Color "[3/5] 启动 Literature Agent (Python)..." "Green"
    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "Set-Location '$NETWORK_DIR'; `$env:PYTHONUTF8='1'; Write-Host '=== Literature Agent ===' -ForegroundColor Green; python agents/literature_agent.py"
    ) -WindowStyle Normal
    Start-Sleep -Seconds 2

    # 步骤 4: 启动 Critical Thinker 和 PR Manager
    Write-Color "[4/5] 启动 Critical Thinker & PR Manager..." "Green"
    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "Set-Location '$NETWORK_DIR'; `$env:PYTHONUTF8='1'; Write-Host '=== Critical Thinker ===' -ForegroundColor Magenta; python -m openagents launch-agent agents/critical_thinker.yaml"
    ) -WindowStyle Normal
    
    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "Set-Location '$NETWORK_DIR'; `$env:PYTHONUTF8='1'; Write-Host '=== PR Manager ===' -ForegroundColor Blue; python -m openagents launch-agent agents/pr_manager.yaml"
    ) -WindowStyle Normal
    Start-Sleep -Seconds 2
}
else {
    Write-Color "[2-4/5] 跳过 Agent 启动" "Gray"
}

# 步骤 5: 打开 Studio
if (-not $SkipStudio) {
    Write-Color "[5/5] 打开 OpenAgents Studio..." "Green"
    Start-Sleep -Seconds 1
    Start-Process "http://localhost:8700/studio/"
}
else {
    Write-Color "[5/5] 跳过 Studio" "Gray"
}

Write-Color ""
Write-Color "========================================" "Cyan"
Write-Color "  Academic Research Network 启动完成" "Green"
Write-Color "========================================" "Cyan"
Write-Color ""
Write-Color "  Studio: http://localhost:8700/studio/" "Yellow"
Write-Color ""
Write-Color "  运行中的 Agent:" "Yellow"
Write-Color "    - facilitator (协调者)" "White"
Write-Color "    - literature-agent (文献专家, Python)" "White"
Write-Color "    - critical-thinker (批判者)" "White"
Write-Color "    - pr-manager (变更管理)" "White"
Write-Color ""
Write-Color "  提示: 在 Studio 中创建 Project 开始使用" "Gray"
Write-Color ""
