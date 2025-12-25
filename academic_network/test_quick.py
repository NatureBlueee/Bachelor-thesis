"""
Academic Research Network - 快速测试脚本
验证文档工具是否正常工作
"""

import asyncio
import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

async def test_document_tools():
    """测试文档工具"""
    print("=" * 60)
    print("  测试文档工具 (DocumentTools)")
    print("=" * 60)
    print()
    
    try:
        from tools.document_tools import DocumentTools
        
        # 初始化
        tools = DocumentTools()
        print(f"✅ DocumentTools 初始化成功")
        print(f"   项目根目录: {tools.project_root}")
        print(f"   Reference 目录: {tools.reference_dir}")
        print()
        
        # 测试 1: 搜索文献
        print("📚 测试 1: 搜索文献 (AI literacy)")
        results = await tools.search_literature("AI literacy", limit=3)
        print(f"   找到 {len(results)} 篇文献")
        for r in results:
            print(f"   - {r['file_name']} ({r['directory']})")
        print()
        
        # 测试 2: 获取未引用文献
        print("📚 测试 2: 获取未引用文献列表")
        uncited = await tools.get_uncited_literature_list()
        print(f"   Uncited 目录有 {len(uncited)} 篇文献")
        for name in uncited[:3]:
            print(f"   - {name}")
        print()
        
        # 测试 3: 获取 PR 状态
        print("📝 测试 3: 获取 PR 状态")
        prs = await tools.list_pr_status()
        print(f"   共有 {len(prs)} 个 PR")
        for pr in prs[:3]:
            print(f"   - {pr['id']}: {pr['status']}")
        print()
        
        # 测试 4: 读取 Draft 章节
        print("📄 测试 4: 读取 Draft.md 前 10 行")
        try:
            draft = await tools.read_draft_section(1, 10)
            print(f"   成功读取 Draft.md")
            print(f"   内容预览: {draft[:100]}...")
        except FileNotFoundError as e:
            print(f"   ⚠️ Draft.md 未找到: {e}")
        print()
        
        print("=" * 60)
        print("  ✅ 文档工具测试通过")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()


async def test_memory_system():
    """测试记忆系统"""
    print()
    print("=" * 60)
    print("  测试记忆系统 (AcademicMemory)")
    print("=" * 60)
    print()
    
    try:
        from mods.memory_system import AcademicMemory
        
        # 初始化
        memory = AcademicMemory(project_id="test_project")
        print(f"✅ AcademicMemory 初始化成功")
        print(f"   Mem0 可用: {memory.enable_mem0}")
        print(f"   MEMORY.md: {memory.memory_file}")
        print()
        
        # 测试 1: 添加记忆（不实际写入）
        print("🧠 测试 1: 检查冲突检测")
        result = await memory.check_conflict("我不要看学术论文的结论")
        print(f"   has_conflict: {result['has_conflict']}")
        print()
        
        # 测试 2: 搜索 MEMORY.md
        print("🧠 测试 2: 从 MEMORY.md 搜索")
        results = await memory.search("PR")
        print(f"   找到 {len(results)} 条相关记忆")
        for r in results[:2]:
            text = r.get('memory', '')[:80]
            print(f"   - {text}...")
        print()
        
        print("=" * 60)
        print("  ✅ 记忆系统测试通过")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()


async def main():
    """主测试函数"""
    print()
    print("=" * 60)
    print("  Academic Research Network - 快速测试")
    print("=" * 60)
    print()
    
    await test_document_tools()
    await test_memory_system()
    
    print()
    print("=" * 60)
    print("  所有测试完成！")
    print("=" * 60)
    print()
    print("接下来可以测试启动网络和 Agent：")
    print()
    print("1. 启动网络:")
    print("   cd academic_network")
    print("   python -m openagents network start network.yaml")
    print()
    print("2. 启动 Literature Agent:")
    print("   python agents/literature_agent.py")
    print()
    print("3. 访问 Studio:")
    print("   http://localhost:8700/studio/")
    print()


if __name__ == "__main__":
    asyncio.run(main())
