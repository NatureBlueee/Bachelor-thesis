"""
Memory Tools for OpenAgents Integration
Provides Agent-friendly wrappers for the AcademicMemory system
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

async def add_memory_tool(
    content: str,
    category: str = "auto",
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Add a memory to the system

    Args:
        content: The memory content (what to remember)
        category: Memory category (preference, decision, insight, constraint, correction, inspiration, auto)
        metadata: Optional additional metadata

    Returns:
        {
            "added": bool,
            "conflict_detected": bool,
            "conflict_info": Optional[str],
            "memory_id": Optional[str]
        }

    Example:
        result = await add_memory_tool(
            content="User prefers GB/T 7714-2015 citation format",
            category="preference"
        )
    """
    memory = _get_memory()

    messages = [{"role": "user", "content": content}]

    result = await memory.add(
        messages=messages,
        category=category,
        metadata=metadata
    )

    return result

async def search_memory_tool(
    query: str,
    category: Optional[str] = None,
    limit: int = 5
) -> List[Dict[str, Any]]:
    """
    Search for relevant memories

    Args:
        query: Search query (natural language)
        category: Optional category filter
        limit: Maximum number of results

    Returns:
        List of memory dictionaries with keys:
        - memory: The memory text
        - metadata: Associated metadata
        - score: Relevance score (if available)

    Example:
        results = await search_memory_tool(
            query="citation format preferences",
            category="preference"
        )
    """
    memory = _get_memory()

    results = await memory.search(
        query=query,
        category=category,
        limit=limit
    )

    return results

async def check_conflict_tool(
    content: str,
    category: Optional[str] = None
) -> Dict[str, Any]:
    """
    Check if a new memory would conflict with existing memories

    Args:
        content: The new memory to check
        category: Optional category to check within

    Returns:
        {
            "has_conflict": bool,
            "conflicting_memories": List[Dict],
            "suggestion": Optional[str]
        }

    Example:
        result = await check_conflict_tool(
            content="User prefers APA citation format",
            category="preference"
        )
    """
    memory = _get_memory()

    # Search for similar memories
    similar = await memory.search(
        query=content,
        category=category,
        limit=3
    )

    has_conflict = len(similar) > 0

    return {
        "has_conflict": has_conflict,
        "conflicting_memories": similar,
        "suggestion": "Review existing preferences before adding" if has_conflict else None
    }

async def get_all_preferences_tool() -> List[Dict[str, Any]]:
    """
    Get all user preferences from memory

    Returns:
        List of preference memories

    Example:
        prefs = await get_all_preferences_tool()
    """
    memory = _get_memory()

    results = await memory.search(
        query="user preference",
        category="preference",
        limit=20
    )

    return results

async def get_project_context_tool() -> Dict[str, Any]:
    """
    Get overall project context from memory

    Returns:
        {
            "decisions": List[Dict],
            "constraints": List[Dict],
            "insights": List[Dict]
        }

    Example:
        context = await get_project_context_tool()
    """
    memory = _get_memory()

    decisions = await memory.search(query="decision", category="decision", limit=10)
    constraints = await memory.search(query="constraint rule", category="constraint", limit=10)
    insights = await memory.search(query="insight finding", category="insight", limit=10)

    return {
        "decisions": decisions,
        "constraints": constraints,
        "insights": insights
    }

# Robust async runner for nested event loops (YAML Agent compatible)
def _run_async(coro):
    """Run an async coroutine, handling nested event loops."""
    try:
        loop = asyncio.get_running_loop()
        import nest_asyncio
        nest_asyncio.apply()
        return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)
    except ImportError:
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(asyncio.run, coro)
                    return future.result(timeout=30)
            else:
                return loop.run_until_complete(coro)
        except Exception as e:
            return {"error": str(e), "added": False}

# Synchronous wrappers for YAML Agent (implementation: "memory_tools.add_memory")
def add_memory(content: str, category: str = "auto") -> Dict[str, Any]:
    """Add a memory (sync, for YAML Agent)."""
    try:
        memory = _get_memory()
        messages = [{"role": "user", "content": content}]
        result = _run_async(memory.add(messages=messages, category=category))
        return {
            "added": result.get("added", False) if isinstance(result, dict) else False,
            "conflict_detected": result.get("conflict_detected", False) if isinstance(result, dict) else False,
            "message": f"Memory added: {content[:50]}..."
        }
    except Exception as e:
        return {"added": False, "error": str(e)}

def search_memory(query: str, category: str = "", limit: int = 5) -> List[Dict[str, Any]]:
    """Search memories (sync, for YAML Agent)."""
    try:
        memory = _get_memory()
        results = _run_async(memory.search(query=query, category=category if category else None, limit=limit))
        return results if isinstance(results, list) else []
    except Exception as e:
        return [{"error": str(e)}]

def check_conflict(content: str, category: str = "preference") -> Dict[str, Any]:
    """Check memory conflict (sync, for YAML Agent)."""
    try:
        memory = _get_memory()
        result = _run_async(memory.check_conflict(new_preference=content, category=category))
        return result if isinstance(result, dict) else {"has_conflict": False}
    except Exception as e:
        return {"has_conflict": False, "error": str(e)}

def get_preferences() -> List[Dict[str, Any]]:
    """Get all preferences (sync, for YAML Agent)."""
    return search_memory(query="user preference", category="preference", limit=20)

def get_project_context() -> Dict[str, Any]:
    """Get project context (sync, for YAML Agent)."""
    return {
        "decisions": search_memory(query="decision", category="decision", limit=10),
        "constraints": search_memory(query="constraint rule", category="constraint", limit=10),
        "insights": search_memory(query="insight finding", category="insight", limit=10)
    }

# Legacy aliases
add_memory_sync = add_memory
search_memory_sync = search_memory
check_conflict_sync = check_conflict
