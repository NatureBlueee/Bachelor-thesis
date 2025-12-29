# 设置 UTF-8 编码，防止中文乱码和 GBK 错误
$env:PYTHONUTF8="1"

# 添加 Python Scripts 到 PATH (如果还没在的话)
if ($env:Path -notlike "*Python313\Scripts*") {
    $env:Path += ";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"
    Write-Host "✅ 已添加 Python Scripts 到环境变量" -ForegroundColor Green
}

# 提示如何使用
Write-Host "🚀 准备启动 OpenAgents 网络..." -ForegroundColor Cyan
Write-Host "提示: 如果遇到端口占用错误，请先运行: Stop-Process -Id (Get-NetTCPConnection -LocalPort 8700).OwningProcess -Force" -ForegroundColor Yellow

# 启动网络
openagents network start network.yaml
