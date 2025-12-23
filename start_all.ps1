<# 
    OpenAgents 一键启动脚本
    运行方式: ./start_all.ps1
#>

$ErrorActionPreference = "Continue"
$openagents = "$env:APPDATA\Python\Python313\Scripts\openagents.exe"
$networkPath = ".\academic_network"

Write-Host "🚀 OpenAgents 一键启动" -ForegroundColor Green
Write-Host "========================" -ForegroundColor Gray

# 1. 启动网络（新窗口）
Write-Host "1️⃣  启动网络..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& '$openagents' network start $networkPath"
Start-Sleep -Seconds 5  # 等待网络初始化

# 2. 启动 Agents（每个一个新窗口）
$agents = @(
    "literature_agent.yaml",
    "critical_thinker.yaml",
    "pr_manager.yaml"
)

foreach ($agent in $agents) {
    $agentPath = "$networkPath\agents\$agent"
    if (Test-Path $agentPath) {
        Write-Host "2️⃣  启动 Agent: $agent" -ForegroundColor Cyan
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "& '$openagents' agent start '$agentPath'"
        Start-Sleep -Seconds 2
    } else {
        Write-Host "⚠️  未找到: $agent" -ForegroundColor Yellow
    }
}

# 3. 打开浏览器
Write-Host "3️⃣  打开 Studio..." -ForegroundColor Cyan
Start-Sleep -Seconds 3
Start-Process "http://localhost:8700/studio/"

Write-Host "`n✅ 全部启动完成！" -ForegroundColor Green
Write-Host "提示: 关闭时请手动关闭所有 PowerShell 窗口" -ForegroundColor Gray
