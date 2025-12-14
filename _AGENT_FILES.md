# Rules和Workflows完整内容

> 由于.agent目录写入受限，请手动将以下内容复制到对应文件。

---

## 目录

1. [Rules文件](#rules文件)
   - [thesis_project.md](#1-thesis_projectmd)
   - [writing.md](#2-writingmd)
   - [context_update.md](#3-context_updatemd)
2. [Workflows文件](#workflows文件)
   - [ask_academic_ai.md](#1-ask_academic_aimd)
   - [analyze_answer.md](#2-analyze_answermd)
   - [add_paper.md](#3-add_papermd)
   - [deep_read.md](#4-deep_readmd)
   - [create_pr.md](#5-create_prmd)
   - [merge_pr.md](#6-merge_prmd)

---

# Rules文件

## 1. thesis_project.md

**位置**: `.agent/rules/thesis_project.md`

```markdown
---
trigger: model_decision
description: 本科毕业论文项目核心规则。定义了项目身份（AI素养对Z世代员工向上影响行为研究）、理论框架（资源依赖理论）、关键变量（AI素养、感知资源优势、向上影响行为、上级开放性）、语言规范（英文正文、中文讨论、APA第7版）。包含讨论人设（批判性学术伙伴）、自动笔记行为（识别偏好/洞见/约束时更新MEMORY.md）、AI行为约束（通过PR修改论文、文献为真相）。
---

# 论文项目规则

## 项目身份

这是一个**本科毕业论文**项目：
- **中文**：AI素养对Z世代员工向上影响行为的影响：资源依赖视角
- **英文**：The Impact of AI Literacy on Upward Influence Behavior among Generation Z Employees: A Resource Dependence Perspective

## 核心理论框架

- **主理论**：资源依赖理论 (Pfeffer & Salancik, 1978; Tripathi, 2021)
- **AI素养框架**：钟柏昌三维 - AI知识、AI情感、AI思维
- **辅助理论**：社会认知理论、领导建构理论

## 关键变量

| 变量 | 类型 | 定义 |
|------|------|------|
| AI素养 | 自变量 | AI知识 + AI情感 + AI思维 |
| 感知资源优势 | 中介 | 员工对自己持有上级需要但缺乏的AI资源的主观认知 |
| 向上影响行为 | 因变量 | 想法生成、推广、实施 |
| 上级开放性 | 调节 | 上级对下属意见和新技术的接受程度 |

## 语言规范

- 论文正文：**英文**
- 讨论、笔记、PR描述：**中文**
- 引用格式：**APA第7版**

## 文件结构

| 目录 | 用途 |
|------|------|
| `Target/` | 论文正文 `Draft.md` |
| `Reference/` | 文献库 |
| `Consensus/` | 学术AI问答 |
| `PR/` | 论文修改请求 |
| `MEMORY.md` | AI讨论笔记 |

---

## 讨论人设

当与用户进行学术讨论时：

### 角色
你是一个与用户共同研究的学术伙伴，对组织行为学、AI素养、资源依赖理论有深入理解。

### 思维框架
在回答前，依次考虑：
1. 这个问题的理论基础是什么？
2. 有哪些相关文献支持或反驳？
3. 对我们的研究框架有什么影响？
4. 是否需要调度其他workflow？

### 行为规范
- 引用必须完整（作者, 年份, 具体发现）
- 对文献进行批判性分析，不只是总结
- 保持批判性立场，不要过于中立
- 主动识别讨论中的关键洞见

---

## 自动笔记行为

在讨论中，当识别到以下信息时，主动更新`MEMORY.md`：

### 触发条件

**保存触发**：
- 用户表达偏好："我喜欢...", "我不要...", "我希望..."
- 项目信息："我们在做...", "我们使用..."
- 决策依据："我选择...因为..."
- 约束条件："必须...", "不能..."
- 用户纠正AI的假设
- 用户说"记住这个"

**更新触发**：
- 用户意见与已记录内容矛盾
- 新洞见产生
- 问题解决

### 更新方式

1. 简短说明你要记录什么
2. 展示具体内容
3. 允许用户修改
4. 不要过度记录，只记录真正重要的

---

## AI行为约束

1. **不直接编辑论文**：修改`Target/Draft.md`必须通过创建PR
2. **文献为真相**：论据必须来自`Reference/`中的文献
3. **保持聚焦**：代际冲突等宏大话题不是核心
4. **问题要深入**：与学术AI交互需要颗粒度
```

---

## 2. writing.md

**位置**: `.agent/rules/writing.md`

```markdown
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
```

---

## 3. context_update.md

**位置**: `.agent/rules/context_update.md`

```markdown
---
trigger: model_decision
description: Context更新规则。定义Consensus/_CONTEXT.md的更新时机：合并PR后、与导师讨论后、关闭CON问答后、理论框架调整后。明确不触发更新的情况：添加文献、阅读文献、日常讨论。精简原则：1-2页、只含提问时需要的核心信息。
---

# Context更新规则

## 什么是Context

`Consensus/_CONTEXT.md`是提问学术AI时需要的研究上下文，包含：
- 论文主题与目标
- 理论框架
- 关键变量定义
- 当前进度
- 最近的困惑

## 更新触发时机

| 时机 | 更新什么 |
|------|----------|
| 合并PR后 | 论文进度、已完成章节 |
| 与导师讨论后 | 最近的困惑、讨论要点 |
| 关闭CON问答后 | 形成的关键洞见 |
| 理论框架调整后 | 变量定义、命题修改 |

## 不触发更新

- 添加文献（不改变研究核心）
- 阅读文献（不改变研究核心）
- 日常讨论（除非产生重要洞见）

## 精简原则

Context不是论文副本，而是：
- 1-2页
- 只含提问时需要的核心信息
- 可直接复制到提问模板
```

---

# Workflows文件

## 1. ask_academic_ai.md

**位置**: `.agent/workflows/ask_academic_ai.md`

```markdown
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
```

---

## 2. analyze_answer.md

**位置**: `.agent/workflows/analyze_answer.md`

```markdown
---
description: 分析学术AI回答，标记文献优先级，提炼关键洞见
---

1. 评估回答质量
   - [ ] 获得了至少1个研究的具体样本信息？
   - [ ] 获得了变量测量方式/量表名称？
   - [ ] 获得了具体统计数据？
   - [ ] 获得了作者论证逻辑？

2. 如果质量不够 → 追问或重新提问

3. 标记文献优先级

   | 文献 | 优先级 | 理由 | 状态 |
   |------|--------|------|------|
   | [引用] | 🔴核心/🟡参考/⚪存疑 | [理由] | ❌需收集/✅已有 |

4. 提炼关键洞见
   - 这个回答告诉我们什么？
   - 对论文有什么影响？
   - 是否需要调整理论框架？

5. 将🔴核心文献加入收集清单

6. 更新 `MEMORY.md` 如有重要洞见

7. 决定是否关闭本轮问答或继续追问
```

---

## 3. add_paper.md

**位置**: `.agent/workflows/add_paper.md`

```markdown
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
```

---

## 4. deep_read.md

**位置**: `.agent/workflows/deep_read.md`

```markdown
---
description: AI深度批判性阅读文献，输出结构化阅读笔记
---

1. 确认目标文献
   - 文件路径：`Reference/PDF-MD/output_api/[文献名].md`
   - 确认文献已转换为Markdown

2. 按结构阅读
   - **摘要**：研究目的、方法、主要发现
   - **理论背景**：使用的理论框架
   - **方法论**：样本、测量工具、分析方法
   - **发现**：具体数据、效应量
   - **讨论**：作者的解释和论证
   - **局限**：作者承认的限制

3. 批判性评估
   - 方法论强度如何？
   - 样本是否有代表性？
   - 论证逻辑是否严密？
   - 与其他研究是否一致？

4. 提取与我们研究的关联
   - 支持哪个命题（P1-P4）？
   - 变量定义是否与我们一致？
   - 有什么可借鉴的方法？

5. 输出阅读笔记
   - 保存到 `Reference/Note/` 或直接记录

6. 最终评价
   - 🔴 直接可用于论文
   - 🟡 间接参考价值
   - ⚪ 价值有限，存档即可

7. 更新 `Reference/_INDEX.md` 的评价标记
```

---

## 5. create_pr.md

**位置**: `.agent/workflows/create_pr.md`

```markdown
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
```

---

## 6. merge_pr.md

**位置**: `.agent/workflows/merge_pr.md`

```markdown
---
description: 合并PR到论文产出物，执行修改并更新状态
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

8. 考虑是否需要更新 `MEMORY.md`
   - 如有重要洞见产生
```

---

# 使用说明

## 手动创建步骤

1. 在项目根目录创建 `.agent/rules/` 目录（如不存在）
2. 在项目根目录创建 `.agent/workflows/` 目录（如不存在）
3. 复制上面每个代码块的内容到对应文件

## 文件位置汇总

```
Graduate-thesis/
├── MEMORY.md                         # ✅ 已创建
├── .agent/
│   ├── rules/
│   │   ├── thesis_project.md         # 复制第1个Rules
│   │   ├── consensus.md              # 已存在
│   │   ├── writing.md                # 复制第2个Rules
│   │   └── context_update.md         # 复制第3个Rules
│   └── workflows/
│       ├── ask_academic_ai.md        # 复制第1个Workflow
│       ├── analyze_answer.md         # 复制第2个Workflow
│       ├── add_paper.md              # 复制第3个Workflow
│       ├── deep_read.md              # 复制第4个Workflow
│       ├── create_pr.md              # 复制第5个Workflow
│       └── merge_pr.md               # 复制第6个Workflow
```
