"""
Standalone Academic Agent - 独立运行版本
绕过 OpenAgents protobuf 依赖冲突
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from openai import OpenAI
from mods.memory_tools_sync import add_memory, search_memory
from tools.document_tools import search_literature, read_file, list_literature
from tools.academic_search import search_academic
import json

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.omnimaas.com/v1")
)

TOOLS = [
    {"type": "function", "function": {
        "name": "add_memory", "description": "添加记忆（偏好/决策/洞见/约束/纠正）",
        "parameters": {"type": "object", "properties": {
            "content": {"type": "string", "description": "要记住的内容"},
            "category": {"type": "string", "description": "分类"}
        }, "required": ["content"]}
    }},
    {"type": "function", "function": {
        "name": "search_memory", "description": "搜索相关记忆",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "搜索查询"}
        }, "required": ["query"]}
    }},
    {"type": "function", "function": {
        "name": "search_literature", "description": "搜索本地文献库",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "搜索关键词"}
        }, "required": ["query"]}
    }},
    {"type": "function", "function": {
        "name": "search_academic", "description": "搜索学术数据库(CrossRef+OpenAlex)",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "搜索关键词"},
            "limit": {"type": "integer", "description": "返回数量"}
        }, "required": ["query"]}
    }},
]

SYSTEM = """你是 ACADEMIC PARTNER - 学术研究合作伙伴。

能力：
- add_memory: 记住用户偏好和重要信息
- search_memory: 搜索相关记忆
- search_literature: 搜索本地文献库
- search_academic: 搜索 CrossRef/OpenAlex 学术数据库

原则：
- 当用户表达偏好时，使用 add_memory 记录
- 回答问题前，先 search_memory 查找相关记忆
- 每个观点都要有理论支持
- 用中文回复"""

def call_tool(name, args):
    if name == "add_memory":
        return add_memory(args["content"], args.get("category", "auto"))
    elif name == "search_memory":
        return search_memory(args["query"])
    elif name == "search_literature":
        return search_literature(args["query"], args.get("limit", 5))
    elif name == "search_academic":
        return search_academic(args["query"], args.get("limit", 3))
    return {"error": f"Unknown tool: {name}"}

def chat(messages):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "claude-sonnet-4-5-20250929"),
        messages=messages, tools=TOOLS, tool_choice="auto"
    )
    msg = response.choices[0].message

    if msg.tool_calls:
        messages.append(msg)
        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)
            result = call_tool(tc.function.name, args)
            print(f"  🔧 {tc.function.name}({args}) -> {str(result)[:100]}...")
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": json.dumps(result, ensure_ascii=False)})
        return chat(messages)
    return msg.content

def main():
    print("🎓 Academic Partner Agent (Standalone)")
    print("输入 'quit' 退出\n")

    messages = [{"role": "system", "content": SYSTEM}]

    while True:
        user_input = input("你: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        response = chat(messages)
        messages.append({"role": "assistant", "content": response})
        print(f"\n🤖 Agent: {response}\n")

if __name__ == "__main__":
    main()
