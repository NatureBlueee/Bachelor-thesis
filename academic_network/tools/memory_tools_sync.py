"""
Memory Tools for OpenAgents YAML Agent Integration
Synchronous wrappers that can be registered via YAML tools configuration

These functions are designed to be called by OpenAgents agents via YAML config:
  tools:
    - name: "add_memory"
      implementation: "memory_tools_sync.add_memory"
"""
import asyncio
from typing import Dict, Any, List, Optional
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from mods.memory_system import AcademicMemory

# Global memory instance (singleton)
_memory_instance: Optional[AcademicMemory] = None

def _get_memory() -> AcademicMemory:
    """Get or create the global memory instance"""
    global _memory_instance
    if _memory_instance is None:
        _memory_instance = AcademicMemory(project_id="academic_research")
    return _memory_instance


def _run_async(coro):
    """Run an async coroutine, handling the case where we're already in an event loop."""
    try:
        loop = asyncio.get_running_loop()
        # We're in an existing loop - need to use nest_asyncio or create a task
        import nest_asyncio
        nest_asyncio.apply()
        return loop.run_until_complete(coro)
    except RuntimeError:
        # No running loop, create one
        return asyncio.run(coro)
    except ImportError:
        # nest_asyncio not installed, try alternative approach
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Create a new thread to run the coroutine
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(asyncio.run, coro)
                    return future.result(timeout=30)
            else:
                return loop.run_until_complete(coro)
        except Exception as e:
            return {"error": str(e), "added": False}


def add_memory(content: str, category: str = "auto") -> Dict[str, Any]:
    """Add a memory to the system.

    Args:
        content: The memory content (what to remember)
        category: Memory category - one of: preference, decision, insight, constraint, correction, inspiration, auto

    Returns:
        Result dictionary with added status and conflict info
    """
    try:
        memory = _get_memory()
        messages = [{"role": "user", "content": content}]

        # Run async function using helper that handles nested loops
        result = _run_async(memory.add(messages=messages, category=category))

        return {
            "added": result.get("added", False) if isinstance(result, dict) else False,
            "conflict_detected": result.get("conflict_detected", False) if isinstance(result, dict) else False,
            "message": f"Memory added: {content[:50]}..."
        }
    except Exception as e:
        return {
            "added": False,
            "error": str(e),
            "message": f"Failed to add memory: {str(e)}"
        }


def search_memory(query: str, category: str = "", limit: int = 5) -> List[Dict[str, Any]]:
    """Search for relevant memories.

    Args:
        query: Search query in natural language
        category: Optional category filter (preference, decision, insight, constraint, correction, inspiration)
        limit: Maximum number of results to return

    Returns:
        List of matching memories with text and metadata
    """
    try:
        memory = _get_memory()
        # Run async function using helper that handles nested loops
        results = _run_async(memory.search(query=query, category=category if category else None, limit=limit))
        return results if isinstance(results, list) else []
    except Exception as e:
        return [{"error": str(e)}]


def check_conflict(content: str, category: str = "preference") -> Dict[str, Any]:
    """Check if a new memory would conflict with existing ones.

    Args:
        content: The new content to check for conflicts
        category: Category to check within (default: preference)

    Returns:
        Conflict check result with has_conflict flag and details
    """
    try:
        memory = _get_memory()
        # Run async function using helper that handles nested loops
        result = _run_async(memory.check_conflict(new_preference=content, category=category))
        return result if isinstance(result, dict) else {"has_conflict": False}
    except Exception as e:
        return {"has_conflict": False, "error": str(e)}


def get_preferences() -> List[Dict[str, Any]]:
    """Get all user preferences from memory.

    Returns:
        List of preference memories
    """
    return search_memory(query="user preference", category="preference", limit=20)


def get_project_context() -> Dict[str, Any]:
    """Get overall project context including decisions, constraints, and insights.

    Returns:
        Dictionary with decisions, constraints, and insights lists
    """
    decisions = search_memory(query="decision", category="decision", limit=10)
    constraints = search_memory(query="constraint rule", category="constraint", limit=10)
    insights = search_memory(query="insight finding", category="insight", limit=10)

    return {
        "decisions": decisions,
        "constraints": constraints,
        "insights": insights
    }


# Test the tools
if __name__ == "__main__":
    print("Testing memory tools sync...")

    # Test add
    result = add_memory("Test: User prefers APA citation format", "preference")
    print(f"Add result: {result}")

    # Test search
    results = search_memory("citation format")
    print(f"Search found {len(results)} results")

    # Test conflict
    conflict = check_conflict("User prefers MLA format", "preference")
    print(f"Conflict check: {conflict}")

    print("All tests passed!")
