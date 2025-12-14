---
description: 向学术AI（Consensus）提问，使用四部分模板确保获得有颗粒度的回答
---


1. 检查 `Consensus/_CONTEXT.md` 是否是最新的
   - 如果过时，先更新Context

2. 明确问题动机
   - 为什么要问这个问题？
   - 来自什么讨论或困惑？

3. 在 `Consensus/_INDEX.md` 注册新编号（CON-XXXX）

4. 使用四部分模板撰写问题：
   ```
   ## Context
   [从_CONTEXT.md复制]
   
   ## Why I'm Asking
   [问题动机]
   
   ## My Question
   [具体问题]
   
   ## Output Requirements
   Please act as an experienced researcher. Provide:
   - Research methodology (sample size, context)
   - How variables were measured
   - Specific findings (effect sizes, coefficients)
   - Authors' reasoning logic
   - Limitations acknowledged
   Do NOT just provide conclusions.
   ```

5. 创建 `Consensus/CON-XXXX.md` 文件，粘贴完整问题

6. 向Consensus提问，粘贴回答到文件

7. 进入答案分析（/analyze）