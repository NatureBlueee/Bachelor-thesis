# PR 文件夹

## 设计目的

存放论文修改请求（Pull Request），每个 PR 是一个**独立完整**的修改说明，无需任何上下文即可执行。

## 内容结构

- `_INDEX.md` - PR 注册表，记录所有 PR 的编号、标题、状态
- `_TEMPLATE.md` - PR 模板
- `PR-XXXX.md` - 具体的修改请求文件

## 使用规则

1. **创建 PR**：使用 `_TEMPLATE.md` 模板创建新 PR，编号递增（PR-0001, PR-0002...）
2. **注册**：新 PR 必须在 `_INDEX.md` 中注册
3. **独立性**：PR 内容必须完整独立，包含：
   - 修改位置（精确到章节/段落）
   - 原文内容
   - 修改后内容
   - 修改理由与文献支持
4. **状态管理**：`pending` → `merged` 或 `rejected`

## 示例

查找待处理 PR：查看 `_INDEX.md` 中 status 为 `pending` 的条目

执行 PR：打开对应 PR 文件，按其中描述的修改内容更新 Target/Draft.md
