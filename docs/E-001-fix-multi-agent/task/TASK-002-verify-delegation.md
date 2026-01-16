# TASK-002 验证任务委派流程

> * Beads 任务ID：`Bachelor-thesis-2g8`
> * EPIC_ID：E-001
> * STORY_ID：STORY-001
> * TASK_ID：TASK-002
> * 优先级：P0
> * 状态：TODO
> * Owner：用户
> * 预估：10min
> * 依赖：TASK-001

---

## 1. 任务描述

验证 academic-partner 能正确委派文献搜索任务给 literature-agent，并返回结果。

## 2. 验收标准

- [ ] 请求"搜索 AI literacy 相关文献"
- [ ] 能看到委派给 literature-agent 的过程
- [ ] literature-agent 能调用 search_literature 工具
- [ ] 结果能返回给 academic-partner 并展示给用户

## 3. 执行步骤

1. 确保系统已启动（TASK-001 完成）
2. 在 Studio UI 中发送文献搜索请求
3. 观察任务委派过程
4. 验证返回结果

## 4. 测试用例

| 用例 | 输入 | 预期输出 |
|------|------|----------|
| TC1 | "帮我搜索 AI literacy 相关文献" | 看到委派过程 + 文献列表 |
| TC2 | "搜索关于 upward influence 的文献" | 看到委派过程 + 文献列表 |

## 5. 实现记录

[待填写]

## 6. 变更记录

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| v1 | 2025-01-14 | Proj Agent | 初版 |
