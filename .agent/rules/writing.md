---
trigger: model_decision
description: 论文写作规则。核心原则：通过PR修改Target/Draft.md、每个论点需文献支撑、APA第7版引用格式、保持整体风格一致。包含正文引用格式（单/双/多作者）、参考文献格式（期刊/专著）、修改流程（创建PR→讨论→合并→更新Context）、质量检查清单。
---


# 论文写作规则

<rules>
## 核心原则

| 原则 | 说明 | 违反后果 |
|------|------|----------|
| **通过PR修改** | 不直接编辑`Target/Draft.md` | 破坏版本控制 |
| **文献支撑** | 每个论点需要`Reference/`中的文献 | 论据不可信 |
| **APA第7版** | 统一引用格式 | 格式混乱 |
| **风格一致** | 保持论述逻辑和语言风格统一 | 读者困惑 |

## 明确禁止

❌ **禁止直接编辑Draft.md** → 必须使用 `/create_pr`
❌ **禁止无文献或数据（可以是假设数据，但必须验证我们的调查计划中涵盖了，而且要明确标注出是假数据与预期结论）支撑的论据** → 先用 `/ask_academic_ai` 获取支持
❌ **禁止混用引用格式** → 统一使用APA第7版
</rules>

<reference_format>
## 引用格式

### 正文引用

| 情况 | 格式 | 示例 |
|------|------|------|
| 单作者 | (Author, Year) | (Smith, 2020) |
| 双作者 | (Author1 & Author2, Year) | (Smith & Jones, 2020) |
| 三人及以上 | (Author1 et al., Year) | (Smith et al., 2020) |
| 直接引用 | (Author, Year, p. X) | (Smith, 2020, p. 45) |

### 参考文献

**期刊**:
```
Author, A. A. (Year). Title of article. Journal Name, Volume(Issue), pages. https://doi.org/xxx
```

**专著**:
```
Author, A. A. (Year). Title of book. Publisher.
```
</reference_format>

<workflow>
## 修改流程

```
发现需要修改
    ↓
/create_pr（创建PR）
    ↓
填写：原文、修改后、理由、文献支持
    ↓
讨论确认
    ↓
/merge_pr（合并）
    ↓
更新 _CONTEXT.md
```
</workflow>

<checklist>
## 质量检查（修改前必读）

- [ ] 修改有文献支持？
- [ ] 与上下文逻辑一致？
- [ ] 符合APA格式？
- [ ] PR描述清晰完整？
- [ ] 是否需要更新_CONTEXT.md？
</checklist>