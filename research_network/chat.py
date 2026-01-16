#!/usr/bin/env python3
"""Academic Partner - 简化版独立运行"""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.omnimaas.com/v1")
)

INSTRUCTION = """你是 ACADEMIC PARTNER - 用户的学术研究合作伙伴。
- 批判性思考者：质疑假设，挑战论证
- 学术顾问：帮助文献研究、论文修改、学术讨论
- 用中文回复"""

messages = [{"role": "system", "content": INSTRUCTION}]

print("🎓 Academic Partner 已启动 (输入 quit 退出)\n")

while True:
    user_input = input("你: ").strip()
    if user_input.lower() in ("quit", "exit", "q"):
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "claude-sonnet-4-5-20250929"),
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"\n🤖: {reply}\n")
