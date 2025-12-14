---
description: 创建论文修改请求（Pull Request）
---


1. 确认修改需求
   - 修改什么？（章节/段落）
   - 为什么修改？（来自哪个讨论/文献）

2. 在 `PR/_INDEX.md` 注册新编号
   - 格式：PR-XXXX
   - 状态：pending

3. 创建 `PR/PR-XXXX.md` 文件，使用模板：

   ```markdown
   # PR-XXXX: [修改标题]

   ## 基本信息
   - 创建日期: YYYY-MM-DD
   - 状态: pending
   - 修改位置: [章节/段落]

   ## 原文
   [原始内容]

   ## 修改后
   [修改后内容]

   ## 修改理由
   [为什么要修改]

   ## 文献支持
   - [引用1]
   - [引用2]
   ```

4. 如果修改复杂，可能需要更多文献支持
   - 返回研究循环（/ask_academic_ai）

5. 讨论确认PR内容无误后，进入合并（/merge_pr PR-XXXX）