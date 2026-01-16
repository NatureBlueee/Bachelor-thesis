#!/usr/bin/env python3
"""命令行聊天客户端"""
import requests
import time
import random
import string
import sys

BASE = "http://localhost:9700"
CLIENT_ID = "cli-user"
SECRET = None

def gen_id():
    return f"{CLIENT_ID}_{int(time.time()*1000)}_{''.join(random.choices(string.ascii_lowercase, k=6))}"

def register():
    global SECRET
    r = requests.post(f"{BASE}/api/register", json={
        "agent_id": CLIENT_ID,
        "metadata": {"display_name": "CLI User", "platform": "cli"}
    })
    data = r.json()
    SECRET = data.get("secret")
    print(f"注册: {data.get('success')} secret={SECRET[:8] if SECRET else None}...")
    return data.get("success", False)

def send_dm(target: str, msg: str):
    r = requests.post(f"{BASE}/api/send_event", json={
        "event_id": gen_id(),
        "event_name": "thread.direct_message.send",
        "source_id": CLIENT_ID,
        "target_agent_id": f"agent:{target}",
        "payload": {"target_agent_id": target, "message_type": "direct_message", "content": {"text": msg}},
        "metadata": {},
        "visibility": "network",
        "secret": SECRET
    })
    print(f"发送: {r.status_code} - {r.json()}")

def poll():
    r = requests.get(f"{BASE}/api/poll", params={"agent_id": CLIENT_ID, "secret": SECRET})
    data = r.json()
    msgs = data.get("data", {}).get("messages", [])
    if msgs:
        for m in msgs:
            print(f"收到: {m}")
    else:
        print("无新消息")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python chat.py send <msg> | poll")
        sys.exit(1)

    register()

    if sys.argv[1] == "send" and len(sys.argv) > 2:
        send_dm("demo-assistant", " ".join(sys.argv[2:]))
    elif sys.argv[1] == "poll":
        poll()
