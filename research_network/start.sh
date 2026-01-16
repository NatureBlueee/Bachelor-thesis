#!/bin/bash
# Academic Research Network 启动脚本
# 使用 Python 3.12 虚拟环境

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# 自动检测虚拟环境路径（优先级：本地 venv > 用户目录 venv）
if [ -d "$SCRIPT_DIR/venv/bin" ]; then
    VENV="$SCRIPT_DIR/venv/bin"
elif [ -d "$HOME/openagents_venv/bin" ]; then
    VENV="$HOME/openagents_venv/bin"
else
    echo "❌ Error: No virtual environment found."
    echo "   Expected: $SCRIPT_DIR/venv/ or ~/openagents_venv/"
    exit 1
fi

# OmniMaaS API 配置 (从环境变量或 .env 文件读取)
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  Warning: OPENAI_API_KEY not set. Please set it in environment or .env file."
fi
export OPENAI_BASE_URL="${OPENAI_BASE_URL:-https://api.omnimaas.com/v1}"

echo "🚀 Starting Academic Research Network..."
echo "📦 Using venv: $VENV"

# 启动网络
$VENV/openagents network start network.yaml &
NETWORK_PID=$!

sleep 5

echo "📡 Network started (PID: $NETWORK_PID)"
echo "🌐 Studio UI: http://localhost:8700/studio/"

# 启动 Agents
echo "🤖 Starting agents..."

$VENV/openagents agent start agents/academic_partner.yaml &
sleep 2

$VENV/openagents agent start agents/literature_agent.yaml &
sleep 2

echo "✅ All agents started!"
echo "Press Ctrl+C to stop all services"

wait
