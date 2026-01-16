"""
Document Tools - 同步版本 (供 YAML Agent 使用)
"""
import asyncio
import nest_asyncio
from pathlib import Path
from typing import List, Dict, Any

# 允许嵌套事件循环
nest_asyncio.apply()

try:
    from .document_tools import DocumentTools
except ImportError:
    from document_tools import DocumentTools

# 全局实例
_doc_tools = None

def _get_doc_tools():
    global _doc_tools
    if _doc_tools is None:
        project_root = Path(__file__).parent.parent.parent
        _doc_tools = DocumentTools(str(project_root))
    return _doc_tools

def search_literature(query: str, search_uncited: bool = True, search_cited: bool = False, limit: int = 5) -> Dict[str, Any]:
    """搜索本地文献库"""
    doc_tools = _get_doc_tools()
    results = asyncio.run(doc_tools.search_literature(
        query=query,
        search_cited=search_cited,
        search_uncited=search_uncited,
        limit=limit
    ))
    return {
        "query": query,
        "count": len(results),
        "files": [{"name": r["file_name"], "path": r["file_path"], "directory": r["directory"]} for r in results]
    }

def suggest_citations(topic: str) -> Dict[str, Any]:
    """建议可引用的文献"""
    doc_tools = _get_doc_tools()
    results = asyncio.run(doc_tools.suggest_citations(topic))
    return {
        "topic": topic,
        "count": len(results),
        "suggestions": [{"name": r["file_name"], "relevance": r["relevance_score"]} for r in results]
    }

def read_literature(file_name: str) -> Dict[str, Any]:
    """读取文献内容"""
    doc_tools = _get_doc_tools()
    # 先搜索找到文件
    results = asyncio.run(doc_tools.search_literature(query=file_name, limit=1))
    if not results:
        return {"error": f"文献未找到: {file_name}"}

    # 直接同步读取，避免嵌套 asyncio.run
    file_path = Path(results[0]["file_path"])
    content = file_path.read_text(encoding="utf-8")
    return {
        "file_name": results[0]["file_name"],
        "content_preview": content[:3000],
        "total_length": len(content)
    }
