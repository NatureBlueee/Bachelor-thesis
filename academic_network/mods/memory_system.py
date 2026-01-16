"""
Academic Research Memory System - Mem0 Integration
基于 Mem0 的智能记忆层，为学术研究Agent提供持久化记忆

核心功能：
1. 自动捕捉用户偏好和洞见
2. 冲突检测：发现矛盾时主动确认
3. 分类存储：偏好、决策、洞见、约束
4. 语义搜索：快速找到相关记忆
"""

import os
from typing import Optional, Dict, List, Any
from datetime import datetime
from pathlib import Path

# 尝试导入 Mem0，如果没安装则使用本地备份
try:
    from mem0 import Memory
    MEM0_AVAILABLE = True
except ImportError:
    MEM0_AVAILABLE = False
    print("⚠️ Mem0 未安装，使用本地备份模式")


class AcademicMemory:
    """
    学术研究记忆系统
    
    设计原则：
    1. 双层架构：Mem0 + MEMORY.md 备份
    2. 冲突检测：发现矛盾时返回警告
    3. 分类存储：按类型组织记忆
    4. 透明可编辑：用户可以直接编辑 MEMORY.md
    """
    
    # 记忆分类
    CATEGORIES = {
        "preference": "用户偏好",      # "我喜欢...", "我不要..."
        "decision": "决策",            # "我决定...", "我们选择..."
        "insight": "洞见",             # 重要认识
        "constraint": "约束",          # "必须...", "不能..."
        "correction": "纠正",          # 用户纠正AI的假设
        "inspiration": "灵感",         # 小想法、待探索
    }
    
    def __init__(
        self,
        project_id: str = "thesis_project",
        memory_file: str = None,
        enable_mem0: bool = True
    ):
        """
        初始化记忆系统
        
        Args:
            project_id: 项目标识（用于隔离不同项目的记忆）
            memory_file: MEMORY.md 的路径
            enable_mem0: 是否启用 Mem0（如果可用）
        """
        self.project_id = project_id
        self.memory_file = memory_file or self._find_memory_file()
        self.enable_mem0 = enable_mem0 and MEM0_AVAILABLE
        
        # 初始化 Mem0
        if self.enable_mem0:
            try:
                # 方案：通过LangChain集成智谱AI embeddings
                from langchain_community.embeddings import ZhipuAIEmbeddings

                # 创建智谱AI embeddings实例
                zhipu_embeddings = ZhipuAIEmbeddings(
                    model="embedding-3",  # 智谱AI的embedding模型
                    api_key=os.getenv("ZHIPUAI_API_KEY")
                )

                # 配置Mem0使用LangChain provider
                mem0_config = {
                    "llm": {
                        "provider": "openai",  # GLM兼容OpenAI接口
                        "config": {
                            "model": "glm-4-flash",
                            "api_key": os.getenv("ZHIPUAI_API_KEY"),
                            "openai_base_url": "https://open.bigmodel.cn/api/paas/v4"  # 正确参数名
                        }
                    },
                    "embedder": {
                        "provider": "langchain",  # 关键：使用LangChain provider
                        "config": {
                            "model": zhipu_embeddings  # 传入LangChain embeddings实例
                        }
                    },
                    "vector_store": {
                        "provider": "qdrant",
                        "config": {
                            "collection_name": "academic_memory_zhipu",  # 使用自定义collection名称
                            "embedding_model_dims": 2048,  # ZhipuAI embedding-3的维度
                            "path": "./qdrant_data"  # 本地存储路径
                        }
                    }
                }

                self.mem0 = Memory.from_config(mem0_config)
                print("[OK] Mem0 memory layer enabled (Zhipu AI via LangChain)")
            except Exception as e:
                print(f"[WARNING] Mem0 initialization failed: {e}")
                self.enable_mem0 = False
                self.mem0 = None
        else:
            self.mem0 = None
    
    def _find_memory_file(self) -> str:
        """查找 MEMORY.md 文件"""
        # 从当前目录向上查找
        current = Path.cwd()
        for _ in range(5):
            memory_path = current / "MEMORY.md"
            if memory_path.exists():
                return str(memory_path)
            current = current.parent
        return "MEMORY.md"
    
    async def add(
        self,
        messages: List[Dict[str, str]],
        category: str = None,
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        添加记忆（从对话中提取）
        
        Args:
            messages: 对话消息列表 [{"role": "user/assistant", "content": "..."}]
            category: 可选的分类提示
            metadata: 附加元数据
        
        Returns:
            添加结果，包含是否有冲突
        """
        result = {
            "added": False,
            "conflict_detected": False,
            "conflict_info": None,
            "memory_id": None
        }
        
        # 1. 使用 Mem0 添加
        if self.enable_mem0 and self.mem0:
            try:
                mem0_result = self.mem0.add(
                    messages=messages,
                    user_id=self.project_id,
                    metadata={
                        "category": category or "auto",
                        "timestamp": datetime.now().isoformat(),
                        **(metadata or {})
                    }
                )
                result["added"] = True
                result["mem0_result"] = mem0_result
                
                # 检查是否有冲突（Mem0 会返回 update 操作）
                if mem0_result and "event" in str(mem0_result):
                    if "UPDATE" in str(mem0_result).upper():
                        result["conflict_detected"] = True
                        
            except Exception as e:
                print(f"[WARNING] Mem0 tian jia shi bai: {e}")
        
        # 2. 同步到 MEMORY.md 备份
        await self._sync_to_markdown(messages, category)
        
        return result
    
    async def search(
        self,
        query: str,
        category: str = None,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        搜索相关记忆
        
        Args:
            query: 搜索查询
            category: 可选的分类过滤
            limit: 返回数量限制
        
        Returns:
            相关记忆列表
        """
        results = []
        
        if self.enable_mem0 and self.mem0:
            try:
                # Mem0 requires user_id as a parameter, not in filters
                filters = {}
                if category:
                    filters["category"] = category

                mem0_results = self.mem0.search(
                    query=query,
                    user_id=self.project_id,  # user_id as separate parameter
                    filters=filters if filters else None,
                    limit=limit
                )

                if mem0_results and "results" in mem0_results:
                    results = mem0_results["results"]

            except Exception as e:
                print(f"[WARNING] Mem0 search failed: {e}")
        
        # 如果 Mem0 没有结果，从 MEMORY.md 搜索
        if not results:
            results = await self._search_markdown(query)
        
        return results
    
    async def check_conflict(
        self,
        new_preference: str,
        category: str = "preference"
    ) -> Dict[str, Any]:
        """
        检查新偏好是否与已有记忆冲突
        
        Args:
            new_preference: 新的偏好表述
            category: 偏好类别
        
        Returns:
            冲突检查结果
        """
        # 搜索相似的现有记忆
        existing = await self.search(new_preference, category=category, limit=3)
        
        result = {
            "has_conflict": False,
            "conflicting_memories": [],
            "suggestion": None
        }
        
        if existing:
            # 让 LLM 判断是否冲突（这里简化为关键词对比）
            for mem in existing:
                memory_text = mem.get("memory", "")
                # 简单的冲突检测：如果包含相反的词
                if self._detect_contradiction(new_preference, memory_text):
                    result["has_conflict"] = True
                    result["conflicting_memories"].append(mem)
            
            if result["has_conflict"]:
                result["suggestion"] = (
                    f"检测到可能的冲突：\n"
                    f"新内容: {new_preference}\n"
                    f"已有记忆: {result['conflicting_memories'][0].get('memory', '')}\n"
                    f"是否要更新为新内容？(y/n)"
                )
        
        return result
    
    def _detect_contradiction(self, new_text: str, old_text: str) -> bool:
        """简单的矛盾检测"""
        contradiction_pairs = [
            ("要", "不要"),
            ("需要", "不需要"),
            ("喜欢", "不喜欢"),
            ("希望", "不希望"),
            ("必须", "不必"),
            ("always", "never"),
            ("want", "don't want"),
        ]
        
        new_lower = new_text.lower()
        old_lower = old_text.lower()
        
        for pos, neg in contradiction_pairs:
            if (pos in new_lower and neg in old_lower) or \
               (neg in new_lower and pos in old_lower):
                return True
        
        return False
    
    async def _sync_to_markdown(
        self,
        messages: List[Dict],
        category: str = None
    ):
        """同步记忆到 MEMORY.md"""
        try:
            # 提取用户消息中的关键信息
            user_messages = [m["content"] for m in messages if m["role"] == "user"]
            if not user_messages:
                return
            
            # 简单的内容提取（实际应该用LLM）
            content = user_messages[-1]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # 添加到 MEMORY.md
            category_name = self.CATEGORIES.get(category, category or "自动")
            # 智能截断：保留完整句子
            if len(content) > 200:
                content = content[:197] + "..."

            entry = f"- [{timestamp}] {category_name}: {content}"

            # 启用同步到MEMORY.md
            await self._append_to_memory_file(entry)

        except Exception as e:
            print(f"[WARNING] Tong bu dao MEMORY.md shi bai: {e}")

    async def _append_to_memory_file(self, entry: str):
        """追加记忆到MEMORY.md"""
        try:
            import aiofiles

            memory_path = Path(self.memory_file)

            # 如果文件不存在，创建基础结构
            if not memory_path.exists():
                initial_content = f"""# AI 讨论笔记

> 最后更新: {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## 用户偏好

## 关键洞见

## 决策记录
"""
                async with aiofiles.open(memory_path, 'w', encoding='utf-8') as f:
                    await f.write(initial_content)

            # 读取现有内容
            async with aiofiles.open(memory_path, 'r', encoding='utf-8') as f:
                content = await f.read()

            # 简单去重检查
            entry_clean = entry.strip()
            if entry_clean in content:
                return  # 已存在，跳过

            # 追加到文件末尾
            async with aiofiles.open(memory_path, 'a', encoding='utf-8') as f:
                await f.write(f"\n{entry}\n")

            print(f"[OK] Yi tong bu dao MEMORY.md: {entry[:50]}...")

        except Exception as e:
            print(f"[WARNING] Tong bu dao MEMORY.md shi bai: {e}")

    async def _search_markdown(self, query: str) -> List[Dict]:
        """从 MEMORY.md 搜索（备份方案）"""
        results = []
        try:
            if Path(self.memory_file).exists():
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # 简单的关键词搜索
                query_words = query.lower().split()
                for line in content.split("\n"):
                    if any(word in line.lower() for word in query_words):
                        results.append({
                            "memory": line.strip(),
                            "source": "MEMORY.md",
                            "score": 0.5
                        })
        except Exception as e:
            print(f"⚠️ MEMORY.md 搜索失败: {e}")
        
        return results[:5]
    
    async def get_all_memories(self) -> List[Dict]:
        """获取所有记忆"""
        if self.enable_mem0 and self.mem0:
            try:
                return self.mem0.get_all(user_id=self.project_id)
            except Exception as e:
                print(f"⚠️ 获取记忆失败: {e}")
        
        return await self._search_markdown("")


# 便捷函数
_memory_instance = None

def get_memory(project_id: str = "thesis_project") -> AcademicMemory:
    """获取记忆系统单例"""
    global _memory_instance
    if _memory_instance is None:
        _memory_instance = AcademicMemory(project_id=project_id)
    return _memory_instance


async def remember(content: str, category: str = None) -> Dict:
    """快速添加记忆"""
    memory = get_memory()
    messages = [{"role": "user", "content": content}]
    return await memory.add(messages, category=category)


async def recall(query: str, limit: int = 5) -> List[Dict]:
    """快速搜索记忆"""
    memory = get_memory()
    return await memory.search(query, limit=limit)


# 使用示例
if __name__ == "__main__":
    import asyncio
    
    async def demo():
        memory = AcademicMemory(project_id="thesis_demo")
        
        # 添加记忆
        result = await memory.add(
            messages=[
                {"role": "user", "content": "我不想听到学术论文的结果，只要方法论"},
                {"role": "assistant", "content": "好的，我记住了你的偏好"}
            ],
            category="preference"
        )
        print(f"添加结果: {result}")
        
        # 检查冲突
        conflict = await memory.check_conflict(
            "我需要学术论文的结果",
            category="preference"
        )
        print(f"冲突检查: {conflict}")
        
        # 搜索记忆
        results = await memory.search("论文")
        print(f"搜索结果: {results}")
    
    asyncio.run(demo())
