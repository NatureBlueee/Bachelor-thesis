"""
Document Tools for Literature Agent
文献搜索、读取、列表工具
"""
import os
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent

def search_literature(query: str, limit: int = 5) -> dict:
    """搜索本地文献库"""
    results = []
    query_lower = query.lower()

    # 搜索目录
    search_dirs = [
        PROJECT_ROOT / "Reference" / "Cited",
        PROJECT_ROOT / "Reference" / "Uncited",
    ]

    for search_dir in search_dirs:
        if not search_dir.exists():
            continue
        for file_path in search_dir.rglob("*.md"):
            try:
                content = file_path.read_text(encoding="utf-8")
                if query_lower in content.lower() or query_lower in file_path.name.lower():
                    # 计算相关度
                    score = content.lower().count(query_lower)
                    results.append({
                        "file": str(file_path.relative_to(PROJECT_ROOT)),
                        "name": file_path.stem,
                        "category": "Uncited" if "Uncited" in str(file_path) else "Cited",
                        "score": score
                    })
            except Exception:
                continue

    # 按相关度排序，优先返回 Uncited
    results.sort(key=lambda x: (-1 if x["category"] == "Uncited" else 0, -x["score"]))
    return {"query": query, "count": len(results[:limit]), "results": results[:limit]}

def read_file(file_path: str) -> str:
    """读取文件内容"""
    full_path = PROJECT_ROOT / file_path
    if not full_path.exists():
        return f"Error: File not found: {file_path}"
    try:
        return full_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading file: {e}"

def list_literature(category: str = None) -> dict:
    """列出文献库中的文献"""
    results = []

    if category == "Cited":
        dirs = [PROJECT_ROOT / "Reference" / "Cited"]
    elif category == "Uncited":
        dirs = [PROJECT_ROOT / "Reference" / "Uncited"]
    else:
        dirs = [
            PROJECT_ROOT / "Reference" / "Cited",
            PROJECT_ROOT / "Reference" / "Uncited",
        ]

    for search_dir in dirs:
        if not search_dir.exists():
            continue
        for file_path in search_dir.rglob("*.md"):
            results.append({
                "file": str(file_path.relative_to(PROJECT_ROOT)),
                "name": file_path.stem,
                "category": "Uncited" if "Uncited" in str(file_path) else "Cited"
            })

    return {"count": len(results), "files": results}
