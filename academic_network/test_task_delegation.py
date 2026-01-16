"""
Multi-Agent Task Delegation Test
Tests: Academic Partner -> Literature Agent task flow
"""
import asyncio
import aiohttp
import json
import uuid
from datetime import datetime

API_URL = "http://localhost:8700"

async def send_event(agent_id: str, event_name: str, target: str, payload: dict):
    """Send event via HTTP API"""
    async with aiohttp.ClientSession() as session:
        data = {
            "event_id": str(uuid.uuid4()),
            "source_id": agent_id,
            "event_name": event_name,
            "target_id": target,
            "payload": payload
        }
        async with session.post(f"{API_URL}/api/send_event", json=data) as resp:
            return await resp.json()

async def test_task_delegation():
    """Test Academic Partner -> Literature Agent task delegation"""
    print("=" * 60)
    print("  Multi-Agent Task Delegation Test")
    print("=" * 60)
    print()

    # Task 1: Delegate literature search to Literature Agent
    task_id = f"test-task-{datetime.now().strftime('%H%M%S')}"

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Sending task delegation...")
    print(f"  From: academic-partner")
    print(f"  To: literature-agent")
    print(f"  Task: Search for 'AI literacy' literature")
    print()

    result = await send_event(
        agent_id="academic-partner",
        event_name="task.delegate",
        target="agent:literature-agent",
        payload={
            "task_id": task_id,
            "delegator_id": "academic-partner",
            "description": "Search for AI literacy related literature",
            "payload": {
                "task_type": "search",
                "query": "AI literacy"
            },
            "timeout_seconds": 60
        }
    )

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Event sent!")
    print(f"  Response: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}")
    print()

    # Wait for processing
    print("Waiting 3 seconds for agent processing...")
    await asyncio.sleep(3)

    # Task 2: Test channel message broadcast
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Testing channel broadcast...")

    result2 = await send_event(
        agent_id="academic-partner",
        event_name="thread.channel_message.send",
        target="channel:general",
        payload={
            "channel": "general",
            "content": {
                "text": "🔬 Multi-agent collaboration test: All agents please respond!"
            }
        }
    )

    print(f"  Channel broadcast result: {result2.get('success', False)}")
    print()

    print("=" * 60)
    print("  Test Complete!")
    print("=" * 60)
    print()
    print("Check the agent logs to verify:")
    print("  1. Literature Agent received task.delegate event")
    print("  2. Literature Agent processed the search task")
    print("  3. All agents received channel broadcast")

if __name__ == "__main__":
    asyncio.run(test_task_delegation())
