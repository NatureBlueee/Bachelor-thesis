# TASK-002: 补全 requirements.txt 依赖

> 文档路径：`/docs/E-002-fix-research-network/task/TASK-002-fix-requirements.md`
> 任务ID：TASK-002
> Beads 任务ID：`[TBD]`
> 任务标题：补全 requirements.txt 依赖
> Epic：E-002 fix-research-network
> Epic 目录：`E-002-fix-research-network`
> 状态（以 beads 为准）：TODO
> 负责人：[TBD]
> 预估工期：0.5h
> 创建日期：2026-01-15
> 优先级：P0（阻塞运行）

---

## 1. 任务目标

* 做什么：补全 `requirements.txt` 缺失的 8 个关键依赖
* 为什么做：缺少依赖导致 `pip install -r requirements.txt` 后仍无法运行
* 缺失依赖列表：
  - mem0ai
  - qdrant-client
  - langchain-community
  - zhipuai
  - aiofiles
  - nest_asyncio
  - fastapi
  - uvicorn

## 2. 关联关系

* 关联 Epic：E-002
* 关联 Story：NO_STORY（技术债修复）
* 关联 Slice：NO_SLICE
* 上游依赖：
  - **无依赖**：可以立即启动
* 下游任务：所有其他任务都依赖环境正确配置

## 3. 验收标准

### 3.1 功能验收标准

- [ ] AC1：`pip install -r requirements.txt` 成功安装所有依赖
- [ ] AC2：`python -c "import mem0ai, qdrant_client, langchain_community, zhipuai, aiofiles, nest_asyncio, fastapi, uvicorn"` 无报错

## 4. 实施方案

* 改动点列表：
  - `research_network/requirements.txt`
* 添加内容：
  ```
  mem0ai>=0.1.0
  qdrant-client>=1.7.0
  langchain-community>=0.0.10
  zhipuai>=2.0.0
  aiofiles>=23.0.0
  nest_asyncio>=1.5.0
  fastapi>=0.100.0
  uvicorn>=0.23.0
  ```

## 5. 测试

- [ ] pip install 测试
- [ ] import 测试

## 6. 风险与回滚

* 风险：版本兼容性问题
* 回滚：git revert
