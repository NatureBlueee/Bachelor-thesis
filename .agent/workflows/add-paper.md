---
description: 添加新的PDF文献并转换为Markdown格式
---


1. 将PDF文件放入 `Reference/PDF-MD/pdfs/` 目录

// turbo
2. 运行转换脚本
   ```powershell
   cd Reference/PDF-MD
   python process.py
   ```

3. 确认转换成功
   - 检查 `Reference/PDF-MD/output_api/` 是否有新的MD文件
   - 检查文件名是否已重命名为论文标题

4. 确认 `Reference/_INDEX.md` 已更新
   - 如未自动更新，手动添加条目

5. 如需深入阅读，进入 `/deep_read`