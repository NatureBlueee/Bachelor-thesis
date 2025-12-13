# Reference 文件夹

## 设计目的

存放学术文献，是论文论据的根基和知识库。

## 内容结构

```
Reference/
├── agent.md        # 本指引
├── _INDEX.md       # 文献注册表
└── PDF-MD/         # PDF 转换工具
    ├── pdfs/       # 待转换的 PDF
    ├── pdfs_done/  # 已转换的 PDF 存档
    ├── output_api/ # 转换后的 Markdown（AI 阅读用）
    └── convert_api.py  # 转换脚本
```

## 使用规则

### 添加新文献
1. 将 PDF 放入 `PDF-MD/pdfs/`
2. 运行 `python PDF-MD/convert_api.py`
3. 在 `_INDEX.md` 中注册文献信息

### 阅读文献
- **AI 阅读**：使用 `PDF-MD/output_api/` 中的 Markdown 版本
- **人工阅读**：使用 `PDF-MD/pdfs_done/` 中的原始 PDF

### 引用格式
所有引用必须符合 **APA 第7版** 规范

## 示例

查找某文献：在 `_INDEX.md` 中按作者/关键词搜索

阅读文献内容：打开 `PDF-MD/output_api/文献名.md`
