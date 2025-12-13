# PDF-MD 文献处理工具

## 功能

将 PDF 学术文献自动处理为 AI 可读的 Markdown 格式。

## 目录结构

```
PDF-MD/
├── pdfs/           # 放入待处理的 PDF
├── pdfs_done/      # 已处理的 PDF 存档
├── output_api/     # 输出的 Markdown 文件
├── process.py      # 一体化处理脚本 ⭐
├── convert_api.py  # 仅转录脚本
└── rename_papers.py # 仅重命名脚本
```

## 使用方法

### 一键处理（推荐）

```powershell
# 1. 将 PDF 放入 pdfs/ 目录
# 2. 运行一体化脚本
python process.py
```

脚本会自动完成：
1. **转录** - 调用 Marker API 将 PDF 转为 Markdown
2. **重命名** - 提取论文标题，将文件名改为论文标题
3. **加入索引** - 自动更新 `Reference/_INDEX.md`

### 单独操作

```powershell
# 仅转录 PDF
python convert_api.py

# 仅重命名已有的 MD 文件
python rename_papers.py
```

## API 配置

使用 Datalab Marker API
- 文档: https://documentation.datalab.to/
- 定价: 每月 $25 免费额度
- API Key 已配置在脚本中
