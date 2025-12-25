"""
Literature Agent - 文献专家 (Python 版本)
负责文献搜索、深度阅读、引用建议

兼容 OpenAgents 0.6+ API
"""

import asyncio
import os
import sys
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

# OpenAgents 导入
from openagents.agents.worker_agent import WorkerAgent, on_event
from openagents.models.event_context import EventContext, ChannelMessageContext

# 导入我们的工具
try:
    from tools.document_tools import DocumentTools
except ImportError:
    # 如果 tools 模块不在路径中，尝试绝对导入
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from tools.document_tools import DocumentTools


class LiteratureAgent(WorkerAgent):
    """
    文献专家 Agent
    
    核心能力：
    1. 搜索本地文献库 (Reference/Cited, Reference/Uncited)
    2. 深度阅读文献，提取与研究相关的信息
    3. 建议可引用的文献（优先从 Uncited 中找）
    4. 生成结构化的阅读笔记
    
    与 OpenAgents WorkerAgent 完全兼容
    """
    
    # WorkerAgent 类属性
    default_agent_id = "literature-agent"
    ignore_own_messages = True
    
    def __init__(self, project_root: str = None, **kwargs):
        """初始化文献专家"""
        # 调用父类初始化 - WorkerAgent 不需要 agent_config
        super().__init__(**kwargs)
        
        # 初始化文档工具
        self.project_root = project_root or self._find_project_root()
        self.doc_tools = DocumentTools(self.project_root)
        
        logger.info(f"📚 Literature Agent 初始化")
        logger.info(f"   项目根目录: {self.project_root}")
    
    def _find_project_root(self) -> str:
        """查找项目根目录"""
        # 从脚本位置向上查找
        current = Path(__file__).parent.parent.parent
        for _ in range(3):
            if (current / "MEMORY.md").exists():
                return str(current)
            current = current.parent
        return str(Path(__file__).parent.parent.parent)
    
    async def on_startup(self):
        """Agent 启动时调用（WorkerAgent hook）"""
        logger.info("📚 Literature Agent 正在启动...")
        
        try:
            # 尝试发送上线消息到 literature 频道
            ws = self.workspace()
            await ws.channel("literature").post(
                "📚 Literature Agent 上线\n\n"
                "我可以帮你：\n"
                "- 搜索本地文献库\n"
                "- 深度阅读文献\n"
                "- 建议可引用的文献"
            )
            logger.info("📚 Literature Agent 已连接到网络并发送上线消息")
        except Exception as e:
            logger.warning(f"无法发送上线消息: {e}")
        
        logger.info("📚 Literature Agent 启动完成")
    
    async def on_shutdown(self):
        """Agent 关闭时调用（WorkerAgent hook）"""
        logger.info("📚 Literature Agent 正在关闭...")
    
    @on_event("task.delegate")
    async def handle_task(self, context: EventContext):
        """处理来自 Facilitator 的任务"""
        payload = context.incoming_event.payload
        
        task_id = payload.get("task_id", "unknown")
        task_type = payload.get("task_type", "search")
        content = payload.get("content", "")
        
        logger.info(f"📚 收到任务: {task_type} - {content[:50]}...")
        
        result = None
        status = "success"
        citations = []
        
        try:
            if task_type == "search":
                result = await self._handle_search(content)
                citations = result.get("files", [])
                
            elif task_type == "deep_read":
                file_path = payload.get("file_path", "")
                result = await self._handle_deep_read(file_path, content)
                
            elif task_type == "suggest":
                result = await self._handle_suggest(content)
                citations = result.get("suggestions", [])
                
            else:
                result = {"error": f"未知任务类型: {task_type}"}
                status = "failed"
                
        except Exception as e:
            result = {"error": str(e)}
            status = "failed"
            logger.error(f"❌ 任务执行失败: {e}")
        
        # 发送结果回 Facilitator - 使用 workspace agent API
        try:
            ws = self.workspace()
            await ws.agent("facilitator").send({
                "event_type": "task.complete",
                "task_id": task_id,
                "results": result,
                "citations": citations,
                "status": status
            })
            logger.info(f"📚 任务完成: {task_id} - {status}")
        except Exception as e:
            logger.error(f"无法发送结果到 Facilitator: {e}")
    
    async def on_channel_post(self, context: ChannelMessageContext):
        """处理频道消息（直接提问）- WorkerAgent hook"""
        text = context.text if hasattr(context, 'text') else ""
        channel = context.channel if hasattr(context, 'channel') else ""
        
        if not text:
            return
        
        logger.info(f"📚 收到频道消息 [{channel}]: {text[:50]}...")
        
        # 如果是在 literature 频道的提问，直接处理
        if channel == "literature":
            results = await self._handle_search(text)
            
            try:
                ws = self.workspace()
                await ws.channel("literature").reply(
                    context.incoming_event.event_id,
                    f"🔍 搜索结果:\n\n"
                    f"找到 {results['count']} 篇相关文献:\n" +
                    "\n".join([f"- {f}" for f in results['files'][:5]])
                )
            except Exception as e:
                logger.error(f"无法发送回复: {e}")
    
    async def on_direct(self, context: EventContext):
        """处理直接消息 - WorkerAgent hook"""
        payload = context.incoming_event.payload
        text = payload.get("content", {}).get("text", "") if isinstance(payload, dict) else ""
        
        if not text:
            return
        
        logger.info(f"📚 收到直接消息: {text[:50]}...")
        
        # 搜索相关文献
        results = await self._handle_search(text)
        
        try:
            ws = self.workspace()
            source_id = context.incoming_event.source_id
            await ws.agent(source_id).send(
                f"🔍 搜索结果:\n\n"
                f"找到 {results['count']} 篇相关文献:\n" +
                "\n".join([f"- {f}" for f in results['files'][:5]])
            )
        except Exception as e:
            logger.error(f"无法发送回复: {e}")
    
    # ========== 业务逻辑方法 ==========
    
    async def _handle_search(self, query: str) -> Dict[str, Any]:
        """处理文献搜索任务"""
        # 优先搜索 Uncited
        results = await self.doc_tools.search_literature(
            query=query,
            search_cited=False,
            search_uncited=True,
            limit=5
        )
        
        # 如果 Uncited 没有结果，再搜索 Cited
        if not results:
            results = await self.doc_tools.search_literature(
                query=query,
                search_cited=True,
                search_uncited=False,
                limit=5
            )
        
        return {
            "query": query,
            "count": len(results),
            "files": [r["file_name"] for r in results],
            "details": results
        }
    
    async def _handle_deep_read(
        self,
        file_path: str,
        query: str
    ) -> Dict[str, Any]:
        """处理深度阅读任务"""
        try:
            content = await self.doc_tools.read_file(file_path)
        except FileNotFoundError:
            results = await self.doc_tools.search_literature(
                query=Path(file_path).stem,
                limit=1
            )
            if results:
                content = await self.doc_tools.read_file(results[0]["file_path"])
            else:
                return {"error": f"文献未找到: {file_path}"}
        
        # 返回文献内容摘要
        analysis = {
            "file": file_path,
            "query": query,
            "content_preview": content[:2000],
            "total_length": len(content)
        }
        
        return {
            "file": file_path,
            "analysis": analysis
        }
    
    async def _handle_suggest(self, topic: str) -> Dict[str, Any]:
        """处理引用建议任务"""
        suggestions = await self.doc_tools.suggest_citations(topic)
        
        return {
            "topic": topic,
            "count": len(suggestions),
            "suggestions": [
                {
                    "file": s["file_name"],
                    "directory": s["directory"],
                    "relevance": s["relevance_score"]
                }
                for s in suggestions
            ]
        }


# ========== 启动入口 ==========

def main():
    """主函数 - 启动 Literature Agent"""
    print("=" * 60)
    print("  Literature Agent - 学术研究文献专家")
    print("=" * 60)
    print()
    
    # 检查环境变量
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️ 警告: OPENAI_API_KEY 未设置")
        print("   请设置: $env:OPENAI_API_KEY = 'your-key'")
        print()
    
    # 创建 Agent
    agent = LiteratureAgent()
    
    print(f"📚 Agent ID: {agent.default_agent_id}")
    print(f"📚 项目根目录: {agent.project_root}")
    print()
    
    # 连接到网络并启动
    try:
        agent.start(
            network_host="localhost",
            network_port=8700,
            transport="grpc"
        )
        
        print("✅ Literature Agent 正在运行")
        print("   按 Ctrl+C 停止")
        print()
        
        # 等待停止信号
        agent.wait_for_stop()
        
    except KeyboardInterrupt:
        print("\n📚 正在关闭...")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        raise


if __name__ == "__main__":
    main()
