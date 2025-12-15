---
description:  合并PR到论文产出物，执行修改并更新状态
---


1. 打开指定PR文件
   - `PR/PR-XXXX.md`

2. 确认PR状态为 `pending`

3. 定位 `Target/Draft.md` 中的修改位置
   - 按PR描述的章节/段落定位

// turbo
4. 执行修改
   - 将"修改后"内容替换"原文"

5. 更新PR状态
   - 将 `status: pending` 改为 `status: merged`
   - 添加合并日期

6. 更新 `PR/_INDEX.md` 中该PR的状态

7. 更新 `Consensus/_CONTEXT.md`
   - 更新论文进度
   - 记录完成的章节

// turbo
8. 同步引用文献
   - 如果PR涉及REFERENCES部分的修改，运行同步脚本
   ```powershell
   cd Reference/PDF-MD
   python sync_citations.py
   ```

9. 考虑是否需要更新 `MEMORY.md`
   - 如有重要洞见产生