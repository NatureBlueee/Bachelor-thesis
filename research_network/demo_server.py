#!/usr/bin/env python3
"""
Academic Research Network - Hackathon Demo Server
展示多 Agent 协作系统的完整功能
"""
import os
import sys
import json
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

sys.path.insert(0, os.path.dirname(__file__))

from openai import OpenAI
from mods.memory_tools_sync import add_memory, search_memory
from tools.document_tools import search_literature, read_file, list_literature
from tools.academic_search import search_academic

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.omnimaas.com/v1")
)

TOOLS = [
    {"type": "function", "function": {
        "name": "add_memory", "description": "记住用户偏好、重要决策或洞见",
        "parameters": {"type": "object", "properties": {
            "content": {"type": "string", "description": "要记住的内容"},
            "category": {"type": "string", "description": "分类: preference/decision/insight/constraint"}
        }, "required": ["content"]}
    }},
    {"type": "function", "function": {
        "name": "search_memory", "description": "搜索相关记忆和历史偏好",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "搜索查询"}
        }, "required": ["query"]}
    }},
    {"type": "function", "function": {
        "name": "search_literature", "description": "搜索本地文献库 (Reference/)",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "搜索关键词"},
            "limit": {"type": "integer", "description": "返回数量", "default": 5}
        }, "required": ["query"]}
    }},
    {"type": "function", "function": {
        "name": "read_literature", "description": "读取文献内容",
        "parameters": {"type": "object", "properties": {
            "file_path": {"type": "string", "description": "文献文件路径"}
        }, "required": ["file_path"]}
    }},
    {"type": "function", "function": {
        "name": "search_academic", "description": "搜索学术数据库 (CrossRef + OpenAlex)",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "搜索关键词"},
            "limit": {"type": "integer", "description": "返回数量", "default": 3}
        }, "required": ["query"]}
    }},
]

SYSTEM_PROMPT = """你是 ACADEMIC PARTNER - 学术研究多Agent协作系统的协调者。

## 你的能力
1. **记忆系统** (Mem0 + MEMORY.md 双层存储)
   - add_memory: 记住用户偏好、决策、洞见
   - search_memory: 语义搜索相关记忆

2. **文献工具** (本地文献库)
   - search_literature: 搜索 Reference/ 目录下的文献
   - read_literature: 读取文献内容

3. **学术搜索** (外部 API)
   - search_academic: 搜索 CrossRef + OpenAlex 数据库

## 工作原则
- 当用户表达偏好时 ("我喜欢...", "不要...")，主动使用 add_memory 记录
- 回答学术问题前，先 search_memory 查找相关记忆
- 每个学术观点都要有文献支持
- 批判性思考：质疑假设，挑战论证
- 用中文回复

## 演示场景
这是一个用于本科毕业论文的学术协作系统，研究主题是：
"AI素养对Z世代员工向上影响行为的影响：资源依赖视角"
"""

# 会话存储
sessions = {}

def call_tool(name, args):
    """执行工具调用"""
    try:
        result = None
        if name == "add_memory":
            result = add_memory(args["content"], args.get("category", "auto"))
        elif name == "search_memory":
            result = search_memory(args["query"])
        elif name == "search_literature":
            result = search_literature(args["query"], args.get("limit", 5))
        elif name == "read_literature":
            content = read_file(args["file_path"])
            if content.startswith("Error"):
                return {"error": content}
            result = {"content_preview": content[:2000], "total_length": len(content)}
        elif name == "search_academic":
            result = search_academic(args["query"], args.get("limit", 3))
        else:
            return {"error": f"Unknown tool: {name}"}
        # Ensure non-empty result for API compatibility
        if not result:
            return {"status": "ok", "message": "No results found"}
        return result
    except Exception as e:
        return {"error": str(e)}

def chat_with_tools(messages, tool_calls_log):
    """带工具调用的对话"""
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "claude-sonnet-4-5-20250929"),
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )
    msg = response.choices[0].message

    if msg.tool_calls:
        # Ensure assistant message has non-empty content for Bedrock API compatibility
        assistant_msg = {
            "role": "assistant",
            "content": msg.content or "Calling tools...",
            "tool_calls": [{"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}} for tc in msg.tool_calls]
        }
        messages.append(assistant_msg)
        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)
            result = call_tool(tc.function.name, args)
            tool_calls_log.append({
                "tool": tc.function.name,
                "args": args,
                "result": result
            })
            # Ensure tool result is never empty
            result_str = json.dumps(result, ensure_ascii=False)
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result_str if result_str else '{"status": "ok"}'
            })
        return chat_with_tools(messages, tool_calls_log)

    return msg.content or "No response"

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Academic Research Network - OpenAgents Hackathon Demo</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh; color: #e0e0e0;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { text-align: center; padding: 30px 0; }
        h1 { font-size: 2.5em; background: linear-gradient(90deg, #00d4ff, #7b2cbf);
             -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .subtitle { color: #888; margin-top: 10px; }
        .main-grid { display: grid; grid-template-columns: 1fr 350px; gap: 20px; margin-top: 20px; }
        .chat-panel { background: rgba(255,255,255,0.05); border-radius: 16px;
                      border: 1px solid rgba(255,255,255,0.1); overflow: hidden; }
        .chat-header { padding: 15px 20px; background: rgba(0,212,255,0.1);
                       border-bottom: 1px solid rgba(255,255,255,0.1); }
        .chat-messages { height: 500px; overflow-y: auto; padding: 20px; }
        .message { margin-bottom: 15px; animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .message.user { text-align: right; }
        .message.user .bubble { background: linear-gradient(135deg, #00d4ff, #0099cc); color: white; }
        .message.assistant .bubble { background: rgba(255,255,255,0.1); }
        .bubble { display: inline-block; padding: 12px 18px; border-radius: 18px; max-width: 80%; text-align: left; }
        .chat-input { display: flex; padding: 15px; border-top: 1px solid rgba(255,255,255,0.1); }
        .chat-input input { flex: 1; padding: 12px 18px; border: none; border-radius: 25px;
                           background: rgba(255,255,255,0.1); color: white; font-size: 14px; }
        .chat-input input::placeholder { color: #888; }
        .chat-input button { margin-left: 10px; padding: 12px 25px; border: none; border-radius: 25px;
                            background: linear-gradient(135deg, #00d4ff, #7b2cbf); color: white;
                            cursor: pointer; font-weight: bold; transition: transform 0.2s; }
        .chat-input button:hover { transform: scale(1.05); }
        .chat-input button:disabled { opacity: 0.5; cursor: not-allowed; }
        .side-panel { display: flex; flex-direction: column; gap: 20px; }
        .panel { background: rgba(255,255,255,0.05); border-radius: 16px; padding: 20px;
                 border: 1px solid rgba(255,255,255,0.1); }
        .panel h3 { color: #00d4ff; margin-bottom: 15px; font-size: 1.1em; }
        .tool-call { background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; margin-bottom: 10px;
                     border-left: 3px solid #7b2cbf; font-size: 13px; }
        .tool-name { color: #00d4ff; font-weight: bold; }
        .tool-args { color: #888; font-size: 12px; margin-top: 5px; }
        .agent-status { display: flex; align-items: center; gap: 10px; padding: 10px;
                       background: rgba(0,0,0,0.2); border-radius: 8px; margin-bottom: 10px; }
        .status-dot { width: 10px; height: 10px; border-radius: 50%; background: #00ff88;
                      animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .quick-actions { display: flex; flex-wrap: wrap; gap: 8px; }
        .quick-btn { padding: 8px 14px; border: 1px solid rgba(255,255,255,0.2); border-radius: 20px;
                    background: transparent; color: #e0e0e0; cursor: pointer; font-size: 12px;
                    transition: all 0.2s; }
        .quick-btn:hover { background: rgba(0,212,255,0.2); border-color: #00d4ff; }
        .loading { display: none; text-align: center; padding: 20px; }
        .loading.active { display: block; }
        .spinner { width: 30px; height: 30px; border: 3px solid rgba(255,255,255,0.1);
                  border-top-color: #00d4ff; border-radius: 50%; animation: spin 1s linear infinite; margin: 0 auto; }
        @keyframes spin { to { transform: rotate(360deg); } }
        #toolCalls { max-height: 300px; overflow-y: auto; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Academic Research Network</h1>
            <p class="subtitle">OpenAgents Hackathon Demo - Multi-Agent Collaboration System</p>
        </header>

        <div class="main-grid">
            <div class="chat-panel">
                <div class="chat-header">
                    <strong>Academic Partner</strong> - 学术研究协调者
                </div>
                <div class="chat-messages" id="chatMessages">
                    <div class="message assistant">
                        <div class="bubble">
                            你好！我是 Academic Partner，你的学术研究合作伙伴。<br><br>
                            我可以帮你：<br>
                            - 搜索和阅读本地文献库<br>
                            - 搜索学术数据库 (CrossRef/OpenAlex)<br>
                            - 记住你的研究偏好<br>
                            - 进行批判性学术讨论<br><br>
                            试试问我关于 "AI literacy" 或 "upward influence" 的问题！
                        </div>
                    </div>
                </div>
                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p style="margin-top: 10px; color: #888;">Agent 思考中...</p>
                </div>
                <div class="chat-input">
                    <input type="text" id="userInput" placeholder="输入你的问题..." onkeypress="if(event.key==='Enter')sendMessage()">
                    <button onclick="sendMessage()" id="sendBtn">发送</button>
                </div>
            </div>

            <div class="side-panel">
                <div class="panel">
                    <h3>Agent 状态</h3>
                    <div class="agent-status">
                        <div class="status-dot"></div>
                        <span>Academic Partner</span>
                        <span style="color: #00ff88; margin-left: auto;">在线</span>
                    </div>
                    <div class="agent-status">
                        <div class="status-dot" style="background: #ffaa00;"></div>
                        <span>Literature Agent</span>
                        <span style="color: #ffaa00; margin-left: auto;">待命</span>
                    </div>
                </div>

                <div class="panel">
                    <h3>快速测试</h3>
                    <div class="quick-actions">
                        <button class="quick-btn" onclick="quickSend('搜索关于 AI literacy 的文献')">搜索文献</button>
                        <button class="quick-btn" onclick="quickSend('记住：我偏好使用资源依赖理论')">记忆偏好</button>
                        <button class="quick-btn" onclick="quickSend('搜索 upward influence behavior 的学术论文')">学术搜索</button>
                        <button class="quick-btn" onclick="quickSend('我之前说过什么偏好？')">查询记忆</button>
                    </div>
                </div>

                <div class="panel">
                    <h3>工具调用日志</h3>
                    <div id="toolCalls">
                        <p style="color: #666; font-size: 13px;">等待工具调用...</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const sessionId = 'demo-' + Date.now();

        function addMessage(role, content) {
            const messages = document.getElementById('chatMessages');
            const div = document.createElement('div');
            div.className = 'message ' + role;
            div.innerHTML = '<div class="bubble">' + content.replace(/\\n/g, '<br>') + '</div>';
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }

        function addToolCall(tool, args, result) {
            const container = document.getElementById('toolCalls');
            if (container.querySelector('p')) container.innerHTML = '';

            const div = document.createElement('div');
            div.className = 'tool-call';
            div.innerHTML = '<div class="tool-name">' + tool + '</div>' +
                           '<div class="tool-args">' + JSON.stringify(args).substring(0, 100) + '...</div>';
            container.insertBefore(div, container.firstChild);
        }

        function quickSend(text) {
            document.getElementById('userInput').value = text;
            sendMessage();
        }

        async function sendMessage() {
            const input = document.getElementById('userInput');
            const text = input.value.trim();
            if (!text) return;

            input.value = '';
            addMessage('user', text);

            document.getElementById('loading').classList.add('active');
            document.getElementById('sendBtn').disabled = true;

            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text, session_id: sessionId })
                });

                const data = await response.json();

                if (data.tool_calls) {
                    data.tool_calls.forEach(tc => addToolCall(tc.tool, tc.args, tc.result));
                }

                addMessage('assistant', data.response);
            } catch (error) {
                addMessage('assistant', '抱歉，发生了错误: ' + error.message);
            }

            document.getElementById('loading').classList.remove('active');
            document.getElementById('sendBtn').disabled = false;
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    session_id = data.get('session_id', 'default')

    if session_id not in sessions:
        sessions[session_id] = [{"role": "system", "content": SYSTEM_PROMPT}]

    sessions[session_id].append({"role": "user", "content": message})

    tool_calls_log = []
    response = chat_with_tools(sessions[session_id], tool_calls_log)

    sessions[session_id].append({"role": "assistant", "content": response})

    return jsonify({
        "response": response,
        "tool_calls": tool_calls_log
    })

@app.route('/api/tools')
def list_tools():
    return jsonify({"tools": [t["function"]["name"] for t in TOOLS]})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  Academic Research Network - Hackathon Demo")
    print("="*60)
    print(f"\n  API Key: {os.getenv('OPENAI_API_KEY', 'NOT SET')[:20]}...")
    print(f"  Base URL: {os.getenv('OPENAI_BASE_URL', 'NOT SET')}")
    print(f"\n  Open http://localhost:5001 in your browser")
    print("="*60 + "\n")
    app.run(host='0.0.0.0', port=5001, debug=True)
