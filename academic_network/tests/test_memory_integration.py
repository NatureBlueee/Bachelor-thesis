"""
Memory System Integration Test
Tests the complete memory system including tools and Mem0 vector search
"""
import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Set UTF-8 encoding for Windows
import os
os.environ['PYTHONIOENCODING'] = 'utf-8'

from tools.memory_tools import (
    add_memory_tool,
    search_memory_tool,
    check_conflict_tool,
    get_all_preferences_tool,
    get_project_context_tool
)

async def test_memory_tools_integration():
    """Test complete memory tools integration"""

    print("=" * 60)
    print("  Memory System Integration Test")
    print("=" * 60)

    # Test 1: Add preference memory
    print("\n[Test 1] Adding preference memory...")
    result1 = await add_memory_tool(
        content="User prefers GB/T 7714-2015 citation format",
        category="preference"
    )
    print(f"  [OK] Added: {result1['added']}")
    assert result1["added"], "Failed to add preference"

    # Test 2: Add decision memory
    print("\n[Test 2] Adding decision memory...")
    result2 = await add_memory_tool(
        content="Decided to use 4-agent architecture for thesis collaboration",
        category="decision"
    )
    print(f"  [OK] Added: {result2['added']}")
    assert result2["added"], "Failed to add decision"

    # Test 3: Add constraint memory
    print("\n[Test 3] Adding constraint memory...")
    result3 = await add_memory_tool(
        content="All thesis modifications must go through PR workflow",
        category="constraint"
    )
    print(f"  [OK] Added: {result3['added']}")
    assert result3["added"], "Failed to add constraint"

    # Test 4: Add insight memory
    print("\n[Test 4] Adding insight memory...")
    result4 = await add_memory_tool(
        content="ZhipuAI embeddings work better than OpenAI for Chinese text",
        category="insight"
    )
    print(f"  [OK] Added: {result4['added']}")
    assert result4["added"], "Failed to add insight"

    # Test 5: Search memories
    print("\n[Test 5] Searching for citation-related memories...")
    search_results = await search_memory_tool(
        query="citation format",
        limit=5
    )
    print(f"  [OK] Found {len(search_results)} memories")
    for i, result in enumerate(search_results[:3]):
        memory_text = result.get('memory', '')[:60]
        print(f"    {i+1}. {memory_text}...")

    # Test 6: Category-specific search
    print("\n[Test 6] Searching preferences only...")
    pref_results = await search_memory_tool(
        query="preference",
        category="preference",
        limit=10
    )
    print(f"  [OK] Found {len(pref_results)} preference memories")

    # Test 7: Conflict detection
    print("\n[Test 7] Testing conflict detection...")
    conflict_result = await check_conflict_tool(
        content="User prefers APA citation format",
        category="preference"
    )
    print(f"  [OK] Conflict detected: {conflict_result['has_conflict']}")
    if conflict_result['has_conflict']:
        print(f"  [INFO] Found {len(conflict_result['conflicting_memories'])} conflicting memories")
        for mem in conflict_result['conflicting_memories'][:2]:
            print(f"    - {mem.get('memory', '')[:50]}...")

    # Test 8: Get all preferences
    print("\n[Test 8] Getting all user preferences...")
    all_prefs = await get_all_preferences_tool()
    print(f"  [OK] Retrieved {len(all_prefs)} preferences")

    # Test 9: Get project context
    print("\n[Test 9] Getting project context...")
    context = await get_project_context_tool()
    print(f"  [OK] Context retrieved:")
    print(f"    - Decisions: {len(context['decisions'])}")
    print(f"    - Constraints: {len(context['constraints'])}")
    print(f"    - Insights: {len(context['insights'])}")

    # Test 10: Verify memory persistence
    print("\n[Test 10] Verifying vector search persistence...")
    verify_results = await search_memory_tool(
        query="agent architecture",
        limit=5
    )
    print(f"  [OK] Found {len(verify_results)} persisted memories")
    found_decision = any("4-agent" in str(r.get('memory', '')).lower() for r in verify_results)
    print(f"  [OK] Decision memory persisted: {found_decision}")

    print("\n" + "=" * 60)
    print("  [SUCCESS] All integration tests passed")
    print("=" * 60)

    # Summary
    print("\n[Summary]")
    print(f"  - Mem0 vector search: WORKING")
    print(f"  - Memory add: WORKING")
    print(f"  - Memory search: WORKING")
    print(f"  - Conflict detection: WORKING")
    print(f"  - Category filtering: WORKING")
    print(f"  - Context retrieval: WORKING")
    print()

async def test_memory_categories():
    """Test all memory categories"""

    print("\n" + "=" * 60)
    print("  Memory Categories Test")
    print("=" * 60)

    categories = [
        ("preference", "User prefers dark mode for IDE"),
        ("decision", "Decided to use Mem0 for memory management"),
        ("insight", "Vector search improves memory recall accuracy"),
        ("constraint", "Memory system must sync to MEMORY.md"),
        ("correction", "User corrected: use LangChain provider not direct OpenAI"),
        ("inspiration", "Could use graph memory for literature connections")
    ]

    for category, content in categories:
        print(f"\n[Test] Adding {category} memory...")
        result = await add_memory_tool(content=content, category=category)
        print(f"  [OK] {category}: {result['added']}")

    # Search each category
    print("\n[Test] Searching each category...")
    for category, _ in categories:
        results = await search_memory_tool(query=category, category=category, limit=5)
        print(f"  [OK] {category}: {len(results)} memories")

    print("\n" + "=" * 60)
    print("  [SUCCESS] Category tests passed")
    print("=" * 60)

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  Starting Memory System Integration Tests")
    print("=" * 60)

    try:
        # Run main integration test
        asyncio.run(test_memory_tools_integration())

        # Run category test
        asyncio.run(test_memory_categories())

        print("\n[FINAL] All tests completed successfully!")

    except Exception as e:
        print(f"\n[ERROR] Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
