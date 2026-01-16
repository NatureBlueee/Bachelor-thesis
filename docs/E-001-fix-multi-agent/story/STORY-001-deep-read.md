# STORY-001 文献深度阅读与结构化笔记

> 文档路径：`/docs/E-001-fix-multi-agent/story/STORY-001-deep-read.md`

* EPIC_ID：E-001
* EPIC_DIR：`E-001-fix-multi-agent`
* STORY_ID：STORY-001
* Story 状态：可开发
* 优先级：Must
* 创建人：PRD Agent
* 创建日期：2025-01-14

---

## 0. 关联信息（References）

* 关联 Epic：`E-001 修复多 Agent 协作系统`
* 关联 PRD：`../prd/PRD-E-001-v0.md`

---

## 1. 背景与目标（Background & Goal）

### 1.1 背景

* 现状 / 痛点：当前系统对话"聊两句就没了"，无法完成文献深度阅读任务
* 上游上下文：biz-overview 确定 MVP 聚焦于文献阅读 + 结构化笔记
* 为什么必须做：这是黑客松演示的核心路径

### 1.2 Story 目标

* 用户视角目标：能通过对话获得高质量的文献深度阅读笔记
* 业务视角目标：展示多 Agent 协作能力

---

## 2. 用户 & 场景（Users & Scenarios）

### 2.1 用户角色

* 主要用户角色：学术研究者

### 2.2 主要使用场景（高层）

* 场景 S1：用户请求搜索某主题文献
* 场景 S2：用户请求深度阅读某篇文献

---

## 3. 用户故事描述（User Story）

* As a：学术研究者
* I want：通过对话请求深度阅读某篇文献
* So that：获得结构化的文献笔记，包含方法论、关键发现、与我研究的关联

---

## 4. 验收标准（Acceptance Criteria）

* AC1：用户发送"帮我深度阅读 XXX 文献"，系统能识别并委派给 literature-agent
* AC2：literature-agent 返回结构化笔记，包含：基本信息、研究问题、方法论、关键发现、RQ 关联、追踪文献
* AC3：整个过程在 OpenAgents Studio UI 中可见

## 4.1 状态机与关键状态

* 状态列表：
  * IDLE：等待用户输入
  * PROCESSING：academic-partner 分析中
  * DELEGATING：委派任务给 literature-agent
  * READING：literature-agent 执行深度阅读
  * COMPLETED：返回结构化笔记
  * FAILED：执行失败
* 状态切换条件：
  * IDLE → PROCESSING：用户发送消息
  * PROCESSING → DELEGATING：识别为文献任务
  * DELEGATING → READING：literature-agent 接收任务
  * READING → COMPLETED：阅读完成
  * 任意 → FAILED：发生错误

## 4.2 契约草案（Contract Draft）

* 委派任务 payload：
```json
{
  "task_type": "deep_read",
  "file_path": "Reference/Cited/xxx.md",
  "context": "用户研究主题描述"
}
```

* 返回结果 payload：
```json
{
  "task_type": "deep_read",
  "results": "结构化笔记内容",
  "citations": ["追踪文献列表"],
  "notes": "## 文献笔记：[标题]\n..."
}
```

---

## 5. 验收用例（Acceptance Scenarios）

### 场景 S1：文献搜索

* Given：用户已连接到 OpenAgents Studio UI
* When：用户发送"帮我搜索 AI literacy 相关文献"
* Then：
  * academic-partner 识别为搜索任务
  * 委派给 literature-agent
  * 返回匹配的文献列表

### 场景 S2：深度阅读

* Given：用户已知某篇文献存在
* When：用户发送"帮我深度阅读 Qin et al 2018 这篇文献"
* Then：
  * academic-partner 委派深度阅读任务
  * literature-agent 执行博士生式阅读
  * 返回结构化笔记（含方法论、关键发现、RQ 关联）

---

## 6. 风险 & OPEN

* 风险：文献内容过长可能导致 LLM 截断
* [OPEN]：是否需要分段阅读长文献？

---

## 7. 变更记录（Changelog）

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| v1.0 | 2025-01-14 | PRD Agent | 初版 |
