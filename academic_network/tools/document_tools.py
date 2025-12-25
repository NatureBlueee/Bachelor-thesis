"""
Academic Research Network - 文档访问工具
提供 Agent 访问本地文件系统的能力

核心功能：
1. PDF 转换 (调用 Datalab API)
2. 文献库搜索
3. Draft 读写 (通过 PR 系统)
4. 引用检查
"""

import os
import asyncio
from pathlib import Path
from typing import List, Dict, Optional, Any
import subprocess


class DocumentTools:
    """
    文档处理工具集
    
    设计原则：
    1. 不直接修改 Draft.md（必须通过 PR）
    2. 支持搜索 Cited/Uncited 文献
    3. 集成 PDF 转换
    """
    
    def __init__(self, project_root: str = None):
        """
        初始化文档工具
        
        Args:
            project_root: 项目根目录
        """
        self.project_root = Path(project_root) if project_root else self._find_project_root()
        self.reference_dir = self.project_root / "Reference"
        self.target_dir = self.project_root / "Target"
        self.pr_dir = self.project_root / "PR"
        
    def _find_project_root(self) -> Path:
        """查找项目根目录（通过 MEMORY.md 定位）"""
        current = Path.cwd()
        for _ in range(5):
            if (current / "MEMORY.md").exists():
                return current
            current = current.parent
        return Path.cwd()
    
    async def search_literature(
        self,
        query: str,
        search_cited: bool = True,
        search_uncited: bool = True,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        搜索文献库
        
        Args:
            query: 搜索关键词
            search_cited: 是否搜索已引用文献
            search_uncited: 是否搜索未引用文献
            limit: 返回数量限制
        
        Returns:
            匹配的文献列表
        """
        results = []
        query_lower = query.lower()
        
        dirs_to_search = []
        if search_cited:
            dirs_to_search.append(self.reference_dir / "Cited")
        if search_uncited:
            dirs_to_search.append(self.reference_dir / "Uncited")
        
        for search_dir in dirs_to_search:
            if not search_dir.exists():
                continue
                
            for file_path in search_dir.glob("*.md"):
                try:
                    content = file_path.read_text(encoding="utf-8")
                    
                    # 简单的关键词匹配
                    if query_lower in content.lower() or query_lower in file_path.stem.lower():
                        # 提取摘要（前500字符）
                        abstract = content[:500].replace("\n", " ")
                        
                        results.append({
                            "file_name": file_path.name,
                            "file_path": str(file_path),
                            "directory": search_dir.name,
                            "abstract": abstract,
                            "relevance_score": self._calculate_relevance(query_lower, content.lower())
                        })
                        
                except Exception as e:
                    print(f"⚠️ 读取文件失败 {file_path}: {e}")
        
        # 按相关度排序
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        return results[:limit]
    
    def _calculate_relevance(self, query: str, content: str) -> float:
        """计算相关度得分"""
        words = query.split()
        score = 0.0
        for word in words:
            count = content.count(word)
            score += min(count / 10.0, 1.0)  # 单个词最多贡献1分
        return score / len(words) if words else 0.0
    
    async def read_file(self, file_path: str) -> str:
        """
        读取文件内容
        
        Args:
            file_path: 文件路径（相对或绝对）
        
        Returns:
            文件内容
        """
        path = Path(file_path)
        if not path.is_absolute():
            path = self.project_root / file_path
        
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {path}")
        
        return path.read_text(encoding="utf-8")
    
    async def read_draft_section(
        self,
        start_line: int = 1,
        end_line: int = 100
    ) -> str:
        """
        读取 Draft.md 的指定行范围
        
        Args:
            start_line: 起始行（1-indexed）
            end_line: 结束行（1-indexed）
        
        Returns:
            指定行范围的内容
        """
        draft_path = self.target_dir / "Draft.md"
        if not draft_path.exists():
            raise FileNotFoundError("Draft.md 不存在")
        
        lines = draft_path.read_text(encoding="utf-8").split("\n")
        selected = lines[start_line - 1:end_line]
        
        return "\n".join(selected)
    
    async def check_missing_citations(self) -> List[Dict[str, str]]:
        """
        检查 Draft.md 中缺失的引用
        
        Returns:
            缺失引用列表
        """
        # 调用现有的 sync_citations.py
        sync_script = self.reference_dir / "PDF-MD" / "sync_citations.py"
        
        if sync_script.exists():
            try:
                result = subprocess.run(
                    ["python", str(sync_script)],
                    cwd=str(self.reference_dir / "PDF-MD"),
                    capture_output=True,
                    text=True
                )
                # 解析输出
                return [{"message": result.stdout}]
            except Exception as e:
                return [{"error": str(e)}]
        
        return [{"warning": "sync_citations.py 不存在"}]
    
    async def convert_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """
        调用 Datalab API 转换 PDF 为 Markdown
        
        Args:
            pdf_path: PDF 文件路径
        
        Returns:
            转换结果
        """
        convert_script = self.reference_dir / "PDF-MD" / "convert_api.py"
        pdfs_dir = self.reference_dir / "PDF-MD" / "pdfs"
        
        # 将 PDF 复制到 pdfs 目录
        source = Path(pdf_path)
        if not source.exists():
            return {"success": False, "error": f"PDF 文件不存在: {pdf_path}"}
        
        import shutil
        dest = pdfs_dir / source.name
        shutil.copy(source, dest)
        
        # 运行转换脚本
        try:
            result = subprocess.run(
                ["python", str(convert_script)],
                cwd=str(self.reference_dir / "PDF-MD"),
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONUTF8": "1"}
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr if result.returncode != 0 else None
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def list_pr_status(self) -> List[Dict[str, str]]:
        """
        列出所有 PR 的状态
        
        Returns:
            PR 状态列表
        """
        index_path = self.pr_dir / "_INDEX.md"
        
        if not index_path.exists():
            return []
        
        content = index_path.read_text(encoding="utf-8")
        prs = []
        
        for line in content.split("\n"):
            if line.startswith("| PR-"):
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 5:
                    prs.append({
                        "id": parts[1],
                        "title": parts[2],
                        "status": parts[3],
                        "date": parts[4] if len(parts) > 4 else ""
                    })
        
        return prs
    
    async def get_uncited_literature_list(self) -> List[str]:
        """
        获取未引用文献列表（用于建议可引用的文献）
        
        Returns:
            未引用文献文件名列表
        """
        uncited_dir = self.reference_dir / "Uncited"
        
        if not uncited_dir.exists():
            return []
        
        return [f.stem for f in uncited_dir.glob("*.md")]
    
    async def suggest_citations(self, topic: str) -> List[Dict[str, Any]]:
        """
        建议可引用的文献（优先从未引用库中找）
        
        Args:
            topic: 主题关键词
        
        Returns:
            建议的文献列表
        """
        # 优先搜索 Uncited
        uncited_results = await self.search_literature(
            topic,
            search_cited=False,
            search_uncited=True,
            limit=5
        )
        
        # 如果 Uncited 没有，再搜索 Cited
        if not uncited_results:
            return await self.search_literature(
                topic,
                search_cited=True,
                search_uncited=False,
                limit=5
            )
        
        return uncited_results


# 便捷函数
_tools_instance = None

def get_document_tools(project_root: str = None) -> DocumentTools:
    """获取文档工具单例"""
    global _tools_instance
    if _tools_instance is None:
        _tools_instance = DocumentTools(project_root=project_root)
    return _tools_instance


# 使用示例
if __name__ == "__main__":
    async def demo():
        tools = DocumentTools()
        
        # 搜索文献
        results = await tools.search_literature("AI literacy")
        print(f"搜索结果: {len(results)} 篇")
        for r in results[:3]:
            print(f"  - {r['file_name']} ({r['directory']})")
        
        # 获取未引用文献
        uncited = await tools.get_uncited_literature_list()
        print(f"\n未引用文献: {len(uncited)} 篇")
        
        # PR 状态
        prs = await tools.list_pr_status()
        print(f"\nPR 状态:")
        for pr in prs:
            print(f"  - {pr['id']}: {pr['status']}")
    
    asyncio.run(demo())
