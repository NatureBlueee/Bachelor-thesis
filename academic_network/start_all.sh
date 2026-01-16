#!/bin/bash
# Academic Network 一键启动脚本
# 启动顺序: Network -> Literature Agent -> Other Agents

cd "$(dirname "$0")"

# 激活虚拟环境（如果存在）
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "警告: 未找到虚拟环境 (venv 或 .venv)，使用系统 Python"
fi

echo "=========================================="
echo "  Academic Research Network 启动脚本"
echo "=========================================="

# 1. 停止所有现有进程
echo "[1/6] 停止现有进程..."
pkill -f "openagents" 2>/dev/null
sleep 2

# 2. 启动 Network
echo "[2/6] 启动 Network..."
python -m openagents.cli network start network.yaml > /tmp/network.log 2>&1 &
sleep 5

# 检查 Network 是否启动
if curl -s http://localhost:8700/api/health > /dev/null; then
    echo "  ✅ Network 启动成功"
else
    echo "  ❌ Network 启动失败"
    exit 1
fi

# 3. 启动 Literature Agent (YAML 版本，有 LLM 能力)
echo "[3/6] 启动 Literature Agent..."
python -m openagents.cli agent start agents/literature_agent.yaml --network-host localhost --network-port 8700 > /tmp/literature_agent.log 2>&1 &
sleep 3

# 4. 启动 Academic Partner
echo "[4/6] 启动 Academic Partner..."
python -m openagents.cli agent start agents/academic_partner.yaml --network-host localhost --network-port 8700 > /tmp/academic_partner.log 2>&1 &
sleep 2

# 5. 启动 PR Manager
echo "[5/6] 启动 PR Manager..."
python -m openagents.cli agent start agents/pr_manager.yaml --network-host localhost --network-port 8700 > /tmp/pr_manager.log 2>&1 &
sleep 2

# 6. 启动 Archivist
echo "[6/6] 启动 Archivist..."
python -m openagents.cli agent start agents/archivist.yaml --network-host localhost --network-port 8700 > /tmp/archivist.log 2>&1 &
sleep 2

# 验证所有 Agent
echo ""
echo "=========================================="
echo "  验证 Agent 状态"
echo "=========================================="
curl -s http://localhost:8700/api/health | python3 -c "
import sys,json
d=json.load(sys.stdin)
agents=list(d['data']['agents'].keys())
print(f'已注册 Agent ({len(agents)}):')
for a in agents:
    print(f'  ✅ {a}')
"

echo ""
echo "=========================================="
echo "  启动完成!"
echo "=========================================="
echo "Studio: http://localhost:8700/studio"
echo "日志目录: /tmp/*.log"
