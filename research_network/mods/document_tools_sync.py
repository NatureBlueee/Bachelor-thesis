"""
Document Tools - 同步版本 (供 YAML Agent 使用)
直接调用 tools.document_tools 中的函数
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import Dict, Any
from tools.document_tools import search_literature as _search, read_file as _read, list_literature as _list


def search_literature(query: str, limit: int = 5) -> Dict[str, Any]:
    """搜索本地文献库"""
    return _search(query=query, limit=limit)


def read_literature(file_path: str) -> Dict[str, Any]:
    """读取文献内容"""
    content = _read(file_path)
    if content.startswith("Error"):
        return {"error": content}
    return {
        "file_path": file_path,
        "content_preview": content[:3000],
        "total_length": len(content)
    }


def list_literature(category: str = None) -> Dict[str, Any]:
    """列出文献库中的文献"""
    return _list(category=category)
