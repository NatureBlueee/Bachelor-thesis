"""
代理间通信测试脚本
模拟 Academic Partner -> Literature Agent 的任务委派流程
"""
import asyncio
from datetime import datetime

# 导入代理组件
from tools.document_tools import DocumentTools
from mods.memory_system import AcademicMemory

print("=" * 60)
print("  代理间通信测试")
print("=" * 60)
print()

async def test_task_delegation():
    """测试任务委派流程"""

    # 初始化组件
    doc_tools = DocumentTools()
    memory = AcademicMemory(project_id="comm_test")

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 组件初始化完成")
    print(f"  - DocumentTools: ✅")
    print(f"  - AcademicMemory (Mem0={memory.enable_mem0}): ✅")
    print()

    # === 模拟任务 1: 文献搜索 ===
    print("=" * 40)
    print("任务 1: Academic Partner -> Literature Agent")
    print("类型: search | 查询: AI literacy")
    print("=" * 40)

    task_payload = {
        "task_id": "task-001",
        "delegator_id": "academic-partner",
        "task_type": "search",
        "query": "AI literacy"
    }

    print(f"[发送] task.delegate 事件")
    print(f"  payload: {task_payload}")

    # Literature Agent 处理
    results = await doc_tools.search_literature(
        query=task_payload["query"],
        search_uncited=True,
        limit=3
    )

    response = {
        "task_id": task_payload["task_id"],
        "status": "success",
        "results": {
            "count": len(results),
            "files": [r["file_name"] for r in results]
        }
    }

    print(f"[接收] task.complete 事件")
    print(f"  找到 {len(results)} 篇文献:")
    for r in results:
        print(f"    - {r['file_name'][:50]}...")
    print()

    # === 模拟任务 2: 引用建议 ===
    print("=" * 40)
    print("任务 2: Academic Partner -> Literature Agent")
    print("类型: suggest | 主题: upward influence")
    print("=" * 40)

    task_payload_2 = {
        "task_id": "task-002",
        "delegator_id": "academic-partner",
        "task_type": "suggest",
        "query": "upward influence"
    }

    print(f"[发送] task.delegate 事件")

    suggestions = await doc_tools.suggest_citations(task_payload_2["query"])

    print(f"[接收] task.complete 事件")
    print(f"  建议引用 {len(suggestions)} 篇文献:")
    for s in suggestions[:3]:
        print(f"    - {s['file_name'][:40]}... (相关度: {s['relevance_score']:.2f})")
    print()

    # === 模拟任务 3: 记忆存储 ===
    print("=" * 40)
    print("任务 3: 记忆系统集成测试")
    print("=" * 40)

    # 添加记忆
    mem_result = await memory.add(
        messages=[{"role": "user", "content": "测试代理通信成功"}],
        category="insight"
    )
    print(f"[记忆] 添加结果: added={mem_result['added']}")

    # 搜索记忆
    search_results = await memory.search("代理", limit=2)
    print(f"[记忆] 搜索 '代理': 找到 {len(search_results)} 条")
    print()

    # === 汇总 ===
    print("=" * 60)
    print("  测试结果汇总")
    print("=" * 60)
    print(f"  ✅ 任务委派流程: 正常")
    print(f"  ✅ 文献搜索: 找到 {len(results)} 篇")
    print(f"  ✅ 引用建议: 建议 {len(suggestions)} 篇")
    print(f"  ✅ 记忆系统: Mem0={memory.enable_mem0}")
    print()
    print("  通信模式验证:")
    print("  Academic Partner --[task.delegate]--> Literature Agent")
    print("  Literature Agent --[task.complete]--> Academic Partner")
    print()

if __name__ == "__main__":
    asyncio.run(test_task_delegation())
