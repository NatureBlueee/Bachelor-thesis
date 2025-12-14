---
trigger: model_decision
---

# Consensus 文件夹

## 设计目的

记录与 Consensus App（学术AI）的问答，Consensus 连接 SCI 学术文献库，是获取文献支持和学术洞见的重要渠道。

## 内容结构

- `_INDEX.md` - 问答注册表
- `_TEMPLATE.md` - 问答模板
- `_CONTEXT.md` - 当前研究上下文（每次PR后更新）
- `CON-XXXX.md` - 具体问答记录

---

## Consensus 的价值与边界

### ✅ 应该用 Consensus 做的事

- **把它当博学的人**：问"是什么"、"是不是这样"类问题
- **在海量文献中识别重要文献**：它的回答会自动引用相关文献
- **发现未知维度**：让它告诉你"你可能没想到的角度"
- **获取颗粒度**：要求它提供样本、方法论、效应量等细节

### ❌ 不应该用 Consensus 做的事

- **分析单篇或几篇已知文献**：直接用 `/deep_read` 读我们的文献库
- **指定它研究特定文献**：如果已知答案在某文献里，直接 `/add_paper` 下载
- **要求它"引用文献"**：它本身就会引用，不需要强调

### 我们的角色

收到回答后，**我们自己判断**文献是否有用，进行分类（🔴🟡⚪），而不是让它替我们判断。

---

## ⚠️ 核心原则：好问题 = 上下文 + 动机 + 具体需求 + 颗粒度要求

> **关键认识**：Consensus 默认会给出"结论性"回答（如"X与Y显著正相关"），但这对研究者来说**没有用**。我们需要的是**具体论证过程**。

### 一个完整的提问必须包含四个部分

| 部分 | 内容 | 为什么需要 |
|------|------|-----------|
| **Part 1: 研究上下文** | 我们论文的主题、理论框架、当前进度 | 让AI理解我们在做什么 |
| **Part 2: 问题动机** | 为什么要问这个问题？遇到了什么困惑/讨论？ | 让AI理解我们的真实需求 |
| **Part 3: 具体问题** | 我们想知道什么？可能有哪些未知维度？ | 核心提问 |
| **Part 4: 输出要求** | 需要什么颗粒度？方法论/样本/效应量？ | 避免只得到结论 |

### 提问模板（复制使用）

```markdown
## Context (研究上下文)
I am conducting a qualitative study on [论文主题]. My theoretical framework is based on [核心理论]. Currently, I am at the stage of [当前阶段]. 

The key constructs in my study include:
- [变量1]: [定义]
- [变量2]: [定义]
- [变量3]: [定义]

## Why I'm Asking (问题动机)
In a recent discussion with my supervisor, we discussed [讨论内容]. This raised a question about [具体困惑]. I need to find literature support for [需要支持的观点].

## My Question
[具体问题]

Additionally, I'm open to discovering dimensions I might not be aware of. If there are related constructs or mechanisms that the literature discusses but I haven't mentioned, please bring them up.

## Output Requirements
Please act as an experienced organizational behavior researcher. Provide specific details from the studies, including:
- Research methodology (quantitative/qualitative, sample size, country/industry context)
- How key variables were measured (scales, instruments, number of items)
- Specific findings (effect sizes β, coefficients r, key quotes from qualitative studies)
- The authors' reasoning and argumentation logic
- Boundary conditions and limitations the authors acknowledged

Do NOT just provide conclusions like "X is positively related to Y." I need the granular details of HOW the research was conducted and WHAT specifically was found.
```

---

## 问答流程（完整生命周期）

### 阶段 1: 准备提问

1. **检查 `_CONTEXT.md`** 确认研究上下文是最新的
2. **明确问题动机** - 为什么要问？来自什么讨论/困惑？
3. **撰写问题** - 使用上面的四部分模板
4. **在 `_INDEX.md` 注册** - 分配 CON 编号

### 阶段 2: 提问与记录

1. **向 Consensus 提问** - 粘贴完整问题
2. **记录回答** - 粘贴到 CON 文件
3. **评估回答质量**：
   - [ ] 获得了至少1个研究的具体样本信息？
   - [ ] 获得了变量测量方式/量表名称？
   - [ ] 获得了具体统计数据（系数、效应量）？
   - [ ] 获得了作者论证逻辑而非仅结论？
4. **如果回答质量不够** → 追问或重新提问

### 阶段 3: 讨论与梳理

**对每个问题逐一讨论**：
1. 这个回答告诉我们什么？
2. 有哪些文献需要收集？
3. 对论文有什么影响？
4. 是否需要调整我们的理论框架/访谈提纲？

### 阶段 4: 关闭问答轮次

当讨论完成后，在 CON 文件底部写**梳理（不是总结）**：

```markdown
## 本轮问答梳理

### 状态: ✅ 已关闭

### 产出
- [ ] PR-XXXX: [描述修改需求]
- [ ] 需收集文献: [列表]
- [ ] 访谈提纲调整: [如有]
- [ ] 形成的关键洞见: [描述]

### 未解决的问题
- [如果有遗留问题，列在这里，可能成为新的CON]
```

---

## 上下文维护规则

### `_CONTEXT.md` 必须包含

1. **论文主题与目标** - 一句话描述
2. **理论框架** - 核心理论及其应用
3. **关键变量** - 定义和操作化
4. **当前进度** - 写到哪个章节了？
5. **已确认的命题/假设** - P1, P2, P3, P4...
6. **最近的讨论/困惑** - 当前面临什么问题？

### 更新时机

- **每次提交 PR 后** → 更新进度和已确认的内容
- **每次与导师讨论后** → 更新困惑和讨论要点
- **每次完成 CON 问答后** → 更新形成的洞见

---

## 好问题 vs 坏问题对比

| 坏问题 | 问题在哪 | 好问题 |
|--------|---------|--------|
| "领导者学习导向与开放性有什么关系？" | 没有上下文、没有颗粒度要求 | "[提供研究上下文]...关于领导者学习目标导向与其对下属建议开放性的研究，请详述：(1)样本规模和情境 (2)测量工具 (3)效应量 (4)论证逻辑" |
| "逆向导师制有什么效果？" | 太泛、没有说明我们为什么关心 | "[说明我们研究的是AI素养如何使年轻员工影响上级]...在逆向导师制中，资深员工成功学习的预测因素有哪些？特别是在技术/AI领域..." |

---

## 索引编码规则

1. **文件编码**：`CON-0001`, `CON-0002`...
2. **问题编码**：`CON-0001-Q1`, `CON-0001-Q2`...（一个文件可含多个相关问题）
3. **追问编码**：`CON-0001-Q1-F1`（Follow-up）
4. **注册要求**：新问答必须在 `_INDEX.md` 中注册
5. **文献追踪**：回答中提到的新文献，在 Reference 的缺失文献清单中标记

---

## 📚 文献识别与分类

> **核心认识**：Consensus 的主要价值是帮助**识别**哪些文献值得深入阅读，而非替代阅读。

### 分类标准

| 级别 | 标记 | 标准 | 处理方式 |
|------|------|------|----------|
| **核心** | 🔴 | 直接支撑理论框架、变量定义、核心命题 | 下载 → PDF-MD转换 → 详细阅读笔记 |
| **参考** | 🟡 | 间接相关、提供背景、方法论参考 | 记录APA引用，暂不下载 |
| **存疑** | ⚪ | 看起来相关但不确定价值 | 先标记，后续决定 |

### 在CON文件中标记文献

```markdown
### 回答中的文献

| 文献 | 优先级 | 理由 | 状态 |
|------|--------|------|------|
| Sijbom et al. (2015) | 🔴 核心 | 直接研究LGO与openness关系 | ❌ 需收集 |
| Murphy (2012) | 🔴 核心 | 逆向导师制经典文献 | ✅ 已收录 |
| Katz et al. (2023) | 🟡 参考 | 元分析，提供背景证据 | - 暂不需要 |
```

### 文献流转路径

```
Consensus回答 → 识别文献 → 分类标记
                              ↓
                    🔴 核心: 加入「缺失文献清单」→ 收集PDF → 转Markdown → 阅读笔记
                    🟡 参考: 记录APA引用即可
                    ⚪ 存疑: 暂存，后续评估
```

### 核心文献判断问题

在标记前问自己：
1. 这篇文献是否直接支撑我们的某个命题（P1-P4）？
2. 这篇文献定义/测量的变量是否与我们的变量相同？
3. 如果不读这篇文献，我们的理论框架是否会有漏洞？

如果答案是"是"→ 🔴 核心；如果只是"有点相关"→ 🟡 参考
