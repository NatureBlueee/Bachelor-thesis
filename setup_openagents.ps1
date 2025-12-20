$ErrorActionPreference = "Stop"

Write-Host "🚀 Starting OpenAgents Setup..." -ForegroundColor Green

# 1. Clone the repository
if (-not (Test-Path "OpenAgents")) {
    Write-Host "📦 Cloning OpenAgents repository..." -ForegroundColor Cyan
    git clone https://github.com/openagents-org/openagents.git OpenAgents
} else {
    Write-Host "✅ OpenAgents directory already exists." -ForegroundColor Yellow
}

# 2. Check for Conda and Create Environment
if (Get-Command "conda" -ErrorAction SilentlyContinue) {
    Write-Host "🐍 Creating Conda environment 'openagents'..." -ForegroundColor Cyan
    try {
        conda create -n openagents python=3.12 -y
        Write-Host "✅ Conda environment created." -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Conda environment might already exist or failed. Please check manually." -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠️  Conda not found. Skipping environment creation. Please ensure you have Python 3.12+ installed." -ForegroundColor Yellow
}

# 3. Instruction for activation and installation
Write-Host "`n🎉 Setup script finished! Next steps:" -ForegroundColor Green
Write-Host "1. Activate the environment:" -ForegroundColor Cyan
Write-Host "   conda activate openagents"
Write-Host "2. Install the package:" -ForegroundColor Cyan
Write-Host "   pip install openagents"
Write-Host "3. Initialize and Start:" -ForegroundColor Cyan
Write-Host "   openagents init ./my_first_network"
Write-Host "   openagents network start ./my_first_network"
