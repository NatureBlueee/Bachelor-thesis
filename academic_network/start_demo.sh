#!/bin/bash
# 黑客松演示一键启动脚本

cd "$(dirname "$0")"

# 激活虚拟环境
[ -d "venv" ] && source venv/bin/activate
[ -d ".venv" ] && source .venv/bin/activate

echo "🚀 启动 Academic Research Network 演示..."

# 停止现有进程
pkill -f "openagents" 2>/dev/null
sleep 2

# 启动 Network
echo "📡 启动 Network..."
python -m openagents.cli network start network.yaml > /tmp/network.log 2>&1 &
sleep 5

# 检查 Network
if ! curl -s http://localhost:8700/api/health > /dev/null; then
    echo "❌ Network 启动失败，查看 /tmp/network.log"
    exit 1
fi
echo "✅ Network 就绪"

# 启动核心 Agent
echo "🤖 启动 Agent..."
python -m openagents.cli agent start agents/literature_agent.yaml --network-host localhost --network-port 8700 > /tmp/literature_agent.log 2>&1 &
sleep 2
python -m openagents.cli agent start agents/academic_partner.yaml --network-host localhost --network-port 8700 > /tmp/academic_partner.log 2>&1 &
sleep 3

# 验证
echo ""
curl -s http://localhost:8700/api/health | python3 -c "
import sys,json
d=json.load(sys.stdin)
agents=list(d['data']['agents'].keys())
print(f'✅ 已注册 {len(agents)} 个 Agent: {agents}')
"

echo ""
echo "=========================================="
echo "  🎉 演示环境就绪!"
echo "=========================================="
echo "  前端: file://$(pwd)/demo.html"
echo "  Studio: http://localhost:8700/studio"
echo "=========================================="

# 打开前端
open demo.html 2>/dev/null || xdg-open demo.html 2>/dev/null || echo "请手动打开 demo.html"
