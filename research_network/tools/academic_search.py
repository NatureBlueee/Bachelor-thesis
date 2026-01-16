"""
Academic Search Tools - 学术搜索 API
CrossRef 和 OpenAlex API 集成（免费，无需 API Key）
"""
import urllib.request
import urllib.parse
import json
from typing import List, Dict, Any

def search_crossref(query: str, limit: int = 5) -> Dict[str, Any]:
    """
    搜索 CrossRef 学术数据库

    Args:
        query: 搜索关键词
        limit: 返回数量限制

    Returns:
        {"query": str, "count": int, "results": List[Dict]}
    """
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://api.crossref.org/works?query={encoded_query}&rows={limit}"

        req = urllib.request.Request(url, headers={"User-Agent": "AcademicResearchAgent/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        results = []
        for item in data.get("message", {}).get("items", []):
            results.append({
                "title": item.get("title", [""])[0],
                "authors": [a.get("family", "") for a in item.get("author", [])[:3]],
                "year": item.get("published-print", {}).get("date-parts", [[None]])[0][0],
                "doi": item.get("DOI", ""),
                "abstract": item.get("abstract", "")[:300] if item.get("abstract") else "",
                "source": "crossref"
            })

        return {"query": query, "count": len(results), "results": results}
    except Exception as e:
        return {"query": query, "count": 0, "results": [], "error": str(e)}

def search_openalex(query: str, limit: int = 5) -> Dict[str, Any]:
    """
    搜索 OpenAlex 学术数据库

    Args:
        query: 搜索关键词
        limit: 返回数量限制

    Returns:
        {"query": str, "count": int, "results": List[Dict]}
    """
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://api.openalex.org/works?search={encoded_query}&per_page={limit}"

        req = urllib.request.Request(url, headers={"User-Agent": "AcademicResearchAgent/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        results = []
        for item in data.get("results", []):
            authors = [a.get("author", {}).get("display_name", "") for a in item.get("authorships", [])[:3]]
            results.append({
                "title": item.get("title", ""),
                "authors": authors,
                "year": item.get("publication_year"),
                "doi": item.get("doi", "").replace("https://doi.org/", "") if item.get("doi") else "",
                "cited_by": item.get("cited_by_count", 0),
                "open_access": item.get("open_access", {}).get("is_oa", False),
                "source": "openalex"
            })

        return {"query": query, "count": len(results), "results": results}
    except Exception as e:
        return {"query": query, "count": 0, "results": [], "error": str(e)}

def search_academic(query: str, limit: int = 5, source: str = "both") -> Dict[str, Any]:
    """
    统一学术搜索接口

    Args:
        query: 搜索关键词
        limit: 每个来源的返回数量
        source: "crossref", "openalex", 或 "both"
    """
    results = []

    if source in ("crossref", "both"):
        cr = search_crossref(query, limit)
        results.extend(cr.get("results", []))

    if source in ("openalex", "both"):
        oa = search_openalex(query, limit)
        results.extend(oa.get("results", []))

    return {"query": query, "count": len(results), "results": results}
