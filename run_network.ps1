$ErrorActionPreference = "Stop"

Write-Host "🚀 Launching OpenAgents Network..." -ForegroundColor Green

# 1. 尝试使用 openagents 命令
try {
    Write-Host "📦 Initializing academic_network..." -ForegroundColor Cyan
    # 优先尝试 python -m 这种稳健的方式
    python -m openagents init ./academic_network
    
    if (-not $?) {
        # 如果 python -m 失败，尝试直接命令（虽然这不太可能，如果 python -m 都失败了）
        openagents init ./academic_network
    }
}
catch {
    Write-Host "⚠️ Initialization failed or directory already exists." -ForegroundColor Yellow
}

# 2. 复制配置文件
if (Test-Path "Reflections/Hackathon/agents") {
    Write-Host "📋 Copying agent configurations..." -ForegroundColor Cyan
    Copy-Item "Reflections/Hackathon/agents/*.yaml" -Destination "academic_network/agents/" -Force
    Write-Host "✅ Agents configured." -ForegroundColor Green
}

# 3. 启动网络
Write-Host "`n🌐 Starting Network..." -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the network." -ForegroundColor Gray
python -m openagents network start ./academic_network
