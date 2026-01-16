#!/bin/bash
cd "$(dirname "$0")"

# 使用 academic_network 的虚拟环境
source ../academic_network/venv/bin/activate

echo "=== Demo Network 启动 ==="

# 停止旧进程
pkill -f "demo-network" 2>/dev/null
sleep 1

# 启动 Network
echo "[1/2] 启动 Network..."
python -m openagents.cli network start network.yaml > /tmp/demo_network.log 2>&1 &
sleep 4

# 检查
if curl -s http://localhost:9700/api/health > /dev/null; then
    echo "  ✅ Network OK"
else
    echo "  ❌ Network 失败"; exit 1
fi

# 启动 Agent
echo "[2/2] 启动 Assistant..."
python -m openagents.cli agent start agents/assistant.yaml --network-host localhost --network-port 9700 > /tmp/demo_assistant.log 2>&1 &
sleep 3

echo ""
echo "=== 启动完成 ==="
echo "Studio: http://localhost:9700/studio"
