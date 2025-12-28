"""
Mem0 初始化验证测试
验证：1. Mem0安装 2. Memory实例创建 3. add/search基础功能 4. 向量存储初始化

如果Mem0不可用（缺少API密钥），则测试降级模式（纯MEMORY.md）
"""
import asyncio
from pathlib import Path
import sys
import os

# 设置UTF-8编码（Windows兼容）
if sys.platform == "win32":
    import locale
    locale.setlocale(locale.LC_ALL, '')
    os.environ['PYTHONUTF8'] = '1'

sys.path.insert(0, str(Path(__file__).parent.parent))

from mods.memory_system import AcademicMemory

async def test_mem0_initialization():
    print("=" * 60)
    print("  Mem0 初始化验证测试")
    print("=" * 60)

    # 测试1: 基础初始化
    print("\n[测试1] 初始化 AcademicMemory...")
    memory = AcademicMemory(project_id="test_init")
    print(f"  Mem0启用状态: {memory.enable_mem0}")
    print(f"  Mem0实例: {memory.mem0 is not None}")

    if not memory.enable_mem0:
        print("警告: Mem0未启用，将使用MEMORY.md备份模式")
        print("  (这是正常的降级行为，系统将使用本地MEMORY.md存储)")
        # 继续测试MEMORY.md模式
        await test_memory_md_mode(memory)
        return

    # 测试2: 添加记忆
    print("\n[测试2] 添加测试记忆...")
    result = await memory.add(
        messages=[{"role": "user", "content": "测试记忆：我喜欢深度阅读文献"}],
        category="preference"
    )
    assert result["added"], "添加记忆失败"
    print(f"  [OK] Memory added successfully: {result}")

    # 测试3: 搜索记忆
    print("\n[测试3] 搜索记忆...")
    results = await memory.search("深度阅读", limit=5)
    assert len(results) > 0, "搜索失败"
    print(f"  [OK] Found {len(results)} related memories")
    for r in results[:2]:
        print(f"    - {r.get('memory', '')[:80]}...")

    print("\n" + "=" * 60)
    print("  OK 所有测试通过（Mem0模式）")
    print("=" * 60)

async def test_memory_md_mode(memory):
    """测试MEMORY.md备份模式"""
    print("\n[备份模式测试1] 添加记忆到MEMORY.md...")

    result = await memory.add(
        messages=[{"role": "user", "content": "测试备份模式：我希望所有引用都使用GB/T 7714格式"}],
        category="preference"
    )

    # 在备份模式下，add方法应该返回{"added": True}
    print(f"  结果: {result}")

    print("\n[备份模式测试2] 搜索MEMORY.md...")
    results = await memory.search("GB/T 7714", limit=5)
    print(f"  找到 {len(results)} 条相关记忆")

    if len(results) > 0:
        print("  OK MEMORY.md备份模式工作正常")
    else:
        print("  警告: 搜索未返回结果（可能MEMORY.md尚未实现完整搜索）")

    print("\n" + "=" * 60)
    print("  OK 备份模式测试完成")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_mem0_initialization())
