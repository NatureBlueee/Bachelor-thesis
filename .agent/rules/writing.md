---
trigger: model_decision
description: 论文写作规则。核心原则：通过PR修改Target/Draft.md、每个论点需文献支撑、APA第7版引用格式、保持整体风格一致。包含正文引用格式（单/双/多作者）、参考文献格式（期刊/专著）、修改流程（创建PR→讨论→合并→更新Context）、质量检查清单。
---

# 论文写作规则

## 核心原则

1. **通过PR修改**：不直接编辑`Target/Draft.md`，所有修改通过PR流程
2. **文献支撑**：每个论点必须有`Reference/`中的文献支持
3. **引用规范**：APA第7版格式
4. **一致性**：保持论文整体风格和论述逻辑一致

## 引用格式

### 正文引用
- 单作者：(Smith, 2020)
- 双作者：(Smith & Jones, 2020)
- 三人及以上：(Smith et al., 2020)
- 直接引用：(Smith, 2020, p. 45)

### 参考文献
- 期刊：Author, A. A. (Year). Title of article. *Journal Name*, *Volume*(Issue), pages. https://doi.org/xxx
- 专著：Author, A. A. (Year). *Title of book*. Publisher.

## 修改流程

```
发现需要修改
    ↓
创建PR（/create_pr）
    ↓
填写原文、修改后内容、理由
    ↓
讨论确认
    ↓
合并PR（/merge_pr）
    ↓
更新Context
```

## 质量检查

在修改论文前确认：
- [ ] 修改有文献支持？
- [ ] 与上下文逻辑一致？
- [ ] 符合APA格式？
- [ ] PR描述清晰完整？