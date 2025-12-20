$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"

Write-Host "🚀 Launching OpenAgents Network (UTF-8 Mode)..." -ForegroundColor Green

# Start the network with explicit Python execution and UTF-8 env var
& "$env:APPDATA\Python\Python313\Scripts\openagents.exe" network start ./academic_network
