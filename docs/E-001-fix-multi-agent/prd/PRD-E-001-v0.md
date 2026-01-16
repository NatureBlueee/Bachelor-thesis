# 多 Agent 文献协作系统 PRD - v0（E-001）

> * EPIC_ID：E-001
> * EPIC_DIR：`E-001-fix-multi-agent`
> * 文档状态：草稿
> * 版本：v0
> * 创建人：PRD Agent
> * 创建日期：2025-01-14

---

## 0. 关联信息（References）

* biz-overview：`/docs/_project/biz-overview.md`
* Story：`../story/STORY-001-deep-read.md`

---

## 1. 背景与动机（Background）

* 现状：已有 academic_network 多 Agent 系统，包含 academic-partner、literature-agent、pr-manager、archivist 四个 Agent
* 问题：对话"聊两句就没了"，无法完成多轮协作
* 影响：无法在黑客松演示多 Agent 协作能力

## 2. 目标与成功标准（Goals & Success Metrics）

* 本 Epic 业务目标：在黑客松演示多 Agent 协作完成文献深度阅读
* 本 Epic 交付目标：
  * 多轮对话不中断（3+ 轮）
  * Agent 间任务委派可见
  * 输出结构化文献笔记

## 3. 范围与非目标（Scope & Non-goals）

* In Scope：
  * 修复对话中断问题
  * 文献搜索 + 深度阅读主路径
  * 结构化笔记输出
* Out of Scope：
  * PR 创建/合并流程
  * 记忆系统（Mem0）
  * 自动文献检索（外部 API）

## 4. 用户与场景（Users & Scenarios）

* 用户角色：学术研究者（本科毕业论文作者）
* 关键场景：
  * S1：用户请求搜索某主题文献
  * S2：用户请求深度阅读某篇文献并输出笔记

## 5. 功能需求（Functional Requirements）

### 5.1 功能 F1：多轮对话

* 描述：用户与 academic-partner 进行多轮对话，不中断
* 业务规则：至少支持 3+ 轮连续对话
* 边界条件：单轮对话超时 30s 提示用户

### 5.2 功能 F2：任务委派

* 描述：academic-partner 将文献任务委派给 literature-agent
* 业务规则：委派过程在 UI 中可见（显示任务流转）
* 边界条件：委派失败时返回错误信息

### 5.3 功能 F3：深度阅读

* 描述：literature-agent 执行博士生式深度阅读
* 业务规则：输出结构化笔记（基本信息、研究问题、方法论、关键发现、RQ 关联、追踪文献）
* 边界条件：文献不存在时返回"未找到"

## 6. UI 证据（Evidence）

* 演示界面：OpenAgents Studio UI（http://localhost:8700/studio）
* 关键状态：
  * 空态：欢迎消息，提示可用功能
  * 加载态：显示"正在处理..."
  * 成功态：显示结构化笔记
  * 失败态：显示错误信息和重试建议

## 7. 验收标准（Acceptance Criteria）

* AC1：启动系统后，发送消息能收到 academic-partner 回复
* AC2：连续对话 3 轮以上不中断
* AC3：请求"搜索 AI literacy 相关文献"，能看到委派给 literature-agent 的过程
* AC4：请求深度阅读某文献，能输出包含"基本信息、方法论、关键发现、RQ关联"的结构化笔记

## 8. 待确认问题（[OPEN]）

* [OPEN-1]：是否需要在 UI 中显示 Agent 间通信的详细日志？

## 9. 变更记录（Changelog）

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| v0 | 2025-01-14 | PRD Agent | 初版 |
