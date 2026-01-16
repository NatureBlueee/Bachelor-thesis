#!/bin/bash
# Demo Network 控制台
cd "$(dirname "$0")"
source ../academic_network/venv/bin/activate

case "$1" in
  start)
    pkill -f "demo-network" 2>/dev/null
    sleep 1
    python -m openagents.cli network start network.yaml > /tmp/demo_network.log 2>&1 &
    sleep 3
    python -m openagents.cli agent start agents/assistant.yaml --network-host localhost --network-port 9700 > /tmp/demo_assistant.log 2>&1 &
    sleep 2
    echo "✅ 已启动 - http://localhost:9700/studio"
    ;;
  stop)
    pkill -f "demo-network" 2>/dev/null
    pkill -f "demo-assistant" 2>/dev/null
    echo "✅ 已停止"
    ;;
  log)
    cat /tmp/demo_assistant.log | tail -100
    ;;
  status)
    curl -s http://localhost:9700/api/health | python3 -c "import sys,json; d=json.load(sys.stdin); print('Agents:', list(d['data']['agents'].keys()))" 2>/dev/null || echo "❌ 未运行"
    ;;
  *)
    echo "用法: ./ctl.sh {start|stop|log|status}"
    ;;
esac
