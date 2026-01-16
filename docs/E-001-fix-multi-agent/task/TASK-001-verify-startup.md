# TASK-001 验证系统启动和基本对话

> * Beads 任务ID：`Bachelor-thesis-2hj`
> * EPIC_ID：E-001
> * STORY_ID：STORY-001
> * TASK_ID：TASK-001
> * 优先级：P0
> * 状态：TODO
> * Owner：用户
> * 预估：10min

---

## 1. 任务描述

验证修复后的多 Agent 系统能正常启动，并支持 3+ 轮连续对话。

## 2. 验收标准

- [ ] `openagents start network.yaml` 启动成功，无报错
- [ ] 打开 http://localhost:8700/studio 能看到 Studio UI
- [ ] 发送消息能收到 academic-partner 回复
- [ ] 连续对话 3+ 轮不中断

## 3. 执行步骤

```bash
# 1. 进入项目目录
cd /Users/nature/个人项目/Bachelor-thesis/academic_network

# 2. 启动系统
openagents start network.yaml

# 3. 打开浏览器访问
open http://localhost:8700/studio
```

## 4. 测试用例

| 用例 | 输入 | 预期输出 |
|------|------|----------|
| TC1 | "你好" | 收到欢迎回复 |
| TC2 | "你能做什么？" | 收到功能介绍 |
| TC3 | "介绍一下你自己" | 收到自我介绍 |
| TC4 | 继续任意对话 | 不中断 |

## 5. 实现记录

[待填写]

## 6. 变更记录

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| v1 | 2025-01-14 | Proj Agent | 初版 |
