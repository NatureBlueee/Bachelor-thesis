# Multi-Agent Design Discussion

> 创建时间: 2025-12-27
> 目的: 记录多Agent协作系统设计的完整讨论过程，包括用户原文、AI思考、决策理由

---

## 1. 核心问题：如何划分Agent？

### 用户提出的两个标准（原文）

> "我觉得区分开来 agent 的标准就是在于他们有没有必要共享同一个 context。这个 context 不是一个文档的 context，它是跟这个对话过程中产生很多的 context。就是区分掉这个 context 会不会让他工作得更好，给他一个更干净的上下文。我觉得目前第一个标准是这样。"
>
> "第二个标准是不是他们的思维是截然不同，或者是说把这个思维分开会更加的工作精准一点？"

### 用户补充的核心需求（原文）

> "我想要的是一个统一的窗口进入，然后在过程中，它会自己去调用是否启动这个工作流，是否启动那个 agent。它会自己判断的，而不是说我进入一个什么论文修改的工作流，或者我进入一个什么深度讨论的工作流。"

**AI理解**：用户不想手动选择工作流，而是希望有一个统一入口（Academic Partner），由它自动判断需要调用哪个 Agent。

### AI理解与应用

**标准1: Context隔离**
- 问题：需要的上下文是否不同？隔离会不会让Agent工作得更干净？
- 应用：如果一个任务不需要当前对话的细节，隔离它可以减少噪音

**标准2: 思维差异**
- 问题：思维方式是否截然不同？分开会不会更精准？
- 应用：批判性思考 vs 机械执行 = 不同的Agent

---

## 2. 从MEMORY.md识别的核心问题

### 用户原文（关于状态同步问题）

> "文档化的工作做得非常差，他们总是喜欢用自己的话去记录，但实际上很多时候用原文去记录是更好的。而且他很多时候无法同步这个状态，就无法同步各个系统之间。就比如说我在这里做了更改，因为这是一个复杂系统，那我在这里做了更改，他很可能在另外一地方就没有更改，就导致这里是旧的，那里是新的。"

### AI分析

这反映了两个独立的问题：
1. **幻觉叠加**：AI用自己的话重述，信息逐渐失真
2. **状态不同步**：复杂系统中一处更改，其他地方没有同步

**解决方案**：需要一个专门的Archivist Agent，职责是：
- 精确引用原文，不重述
- 确保所有相关文件同步更新

---

## 3. 用户对"图书馆管理员"的构想（原文）

> "这个东西是不是要做一个单独的工具吗？还是说做一个单独的，像图书馆里员一样的状态，他会管理我们系统里面每个文件，确保发生新的更新的时候，所有的文件或者有可能涉及到的相关地方都会被更新、被同步。我觉得这个是不是单独做一个 agent，因为他不需要知道任何的其他东西，他只需要知道这一次我们完成了什么东西，我去同步，我去更新。"

### 用户关于文档化和防止幻觉的洞见（原文）

> "包括很多的习惯，比如说为了防止 AI 幻觉的叠加，尤其是用户给你的输出或者是关键的文献这种原材料，很好的东西，它不是 AI 生成的东西。就一旦涉及到引用，不能让 AI 去重述，而是说直接把原文放出来。"
>
> "还有一个很大的能力，就是要文档化的工作。因为 AI 实际上是没有长期记忆的。那文档就是它的大脑，它才知道自己刚刚干什么。"

### 用户关于上下文连续性的洞见（原文）

> "有些东西你要考虑到：当他进行一个长期的话题讨论的时候，尽量是就单个话题。他要做一个上下文的衔接。然后，比如说我开启了一个新的 PR。那么我就期待我在这个 PR 里面会得到连续的上下文。他连续地理解。"
>
> "包括很多时候，用户如果输入了很优质的一些回答，但其实他需要存下来的，为什么要存下来？因为很多时候，用户的回答会体现出他的风格和要求。可能是统一的，可能这一次你没法提取出来，但下次你是可以提取出来的。"
>
> "所以，尤其是像我这种，我会说很多的话，我会给出很多的意见。我就发现很多时候，他会一遍一遍、一遍一遍地去理解这个意见，要我一遍一遍地说。但其实不应该是这样的。"

### AI分析

这些洞见揭示了几个关键设计原则：

1. **防止幻觉叠加**：原材料（用户输入、文献）不能让 AI 重述，直接引用原文
2. **文档是大脑**：AI 没有长期记忆，文档就是记忆载体
3. **PR 内上下文连续**：一个 PR 内应该有连续的理解，不断章取义
4. **用户输入要保存**：用户的高质量输入体现风格和要求，要保存下来
5. **避免重复解释**：不应该让用户一遍一遍说同样的话

这完美符合两个标准：
1. **Context隔离**：只需要知道"本次完成了什么"，不需要对话细节
2. **思维差异**：机械式执行，不需要批判性思考

---

## 4. 关于记忆系统的讨论

### 用户问题（原文）

> "我们的记忆框架现在是采用的 mem0 一个开源记忆框架。然后你觉得记忆这个东西要不要单独做？或者是说记忆框架应该已经是 memo0 配置在 agent 的协作当中过程中了。"

### AI回答

**不需要单独的Memory Agent**

理由：
- Mem0是**基础设施**，每个Agent都可以调用
- 但**什么值得记住**是一个判断，这个判断需要理解对话价值
- 只有Academic Partner能做这个判断，因为它有完整的对话Context
- 记忆的写入应该由Academic Partner触发，通过调用Mem0实现

**结论**：记忆是核心思维的一部分，不是独立Agent

---

## 5. 关于文献阅读的讨论

### 用户原文

> "我觉得文献阅读肯定是要单独分开的，因为文献阅读跟我们所需要的上下文没什么区别，没什么关系。"

### 用户对深度阅读的详细要求（原文）

> "这个呢，其实是去阅读深入阅读的那个优质的文献。他不仅是说充分理解这个文献本身是什么东西，而不是说你要重新去看我们 memory 里面的文档。他不是说我去看他跟我们的论题符不符合、相不相关，而是真实地去理解他，去批判他。"
>
> "看到这篇论文，他都看了什么东西？他重要的输出点是说这篇论文的这个文献的核心贡献是什么？他论证强度是什么？他的逻辑走不走得通？他的细节都是怎么样？还有哪些可以高光的点？有哪些可以批判的点？"
>
> "就这么一个，作为一个博士生去读这个论文，去读这个文献，然后去联想，而不只是说跟我们哪一个点单独的对上。而是在了解了我们当前抽象的研究命题以后，去看带着我们已经有的 context 去看的时候，要遵循一步一步地看。"
>
> "就是看完一点，我有个大概想法，我先记录下来这篇文章里我看到了什么。他可能不只是说输出一个结构化的笔记，他有临时的想法，而且这个想法本身要是经过批判的。他就像一个思考者一样。"
>
> "然后他的步骤为什么要这么多的步骤？是因为他读一篇文献可能很大，所以我们要提前判断这篇文献大概有多大。我们一次的短期记忆能不能存得了？短期记忆存不了，我们就是读一篇文献，写一下笔记；读一篇文件，写一下笔记。"
>
> "而这个笔记，它是有索引的，它是可以溯源的。这样子以后别人再来读文献，他就不需要直接一整封文献去读，几乎文献里面所有的关键点都会列出来。"

### AI分析

这段原文非常重要，揭示了 Literature Agent 的核心设计：

1. **不是机械匹配**：不是"跟我们有12点相关"，而是真正理解和批判
2. **像博士生一样**：有自己的思考，有临时想法，经过批判
3. **分块阅读**：因为文献可能很长，需要预估并分块
4. **可溯源笔记**：每个要点都能追溯到原文，方便后续使用
5. **输出不只是结构化笔记**：还有临时想法、批判点

完全同意。Literature Agent应该隔离的原因：
1. **Context隔离**：只需要文献内容 + 研究框架（RQ1-RQ3, 理论框架）
2. **不需要**：当前对话的来回讨论、用户的情绪、之前的争论
3. **思维方式**：深度理解、结构化提取、精确溯源（与批判性思考不同）

**隔离的好处**：给它一个干净的上下文，它就专注于"理解这篇文献"，不会被对话中的噪音干扰。

---

## 6. proj_tpl框架的启发

### 核心设计原则

从 `proj_tpl/.claude/agents/` 的5个Agent（biz-owner, prd, tech, proj, dev）学到：

| 原则 | 说明 |
|------|------|
| **能力卡片** | 定位、产出、输入、关键判断、质量门槛、明确不做 |
| **两种模式** | 探索模式（对话澄清）→ 总结模式（生成文档） |
| **升级规则** | 明确什么时候需要回推给其他Agent |
| **边界约束** | "明确不做"比"负责什么"更重要 |
| **产出物导向** | 每个Agent有明确的文档产出 |

### 关键洞见

每个Agent都有**能力维度（抽象）**，定义的是**思维能力**而不只是功能：

```
biz-owner的能力维度：
- 第一性原理推导
- JTBD建模
- 价值主张与取舍
- MVP切割与止损
```

这启发我们：Agent的定义应该是"你怎么思考"，而不是"你做什么功能"。

---

## 7. 当前决策：4个Agent架构

### 架构图

```
                          用户
                           ↓
┌──────────────────────────────────────────────────────────────┐
│              Academic Partner（学术伙伴）                      │
│                                                              │
│  定位：把"模糊想法"变成"可行的研究行动"                          │
│  思维：批判性 + 假设生成 + 第一性原理                           │
│  Context：完整对话                                            │
│  产出：讨论共识、记忆更新、任务分派                             │
│  不做：不直接读长文献、不直接改文件                             │
└───────────────────────┬──────────────────────────────────────┘
                        │
     ┌──────────────────┼──────────────────┐
     ↓                  ↓                  ↓
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Literature  │  │ PR Manager  │  │  Archivist  │
│   Agent     │  │             │  │             │
│             │  │             │  │             │
│ Context:    │  │ Context:    │  │ Context:    │
│ 隔离        │  │ 部分        │  │ 最小        │
│ (文献+框架)  │  │ (意图+规则)  │  │ (变更内容)   │
│             │  │             │  │             │
│ 思维：       │  │ 思维：       │  │ 思维：       │
│ 深度理解    │  │ 流程验证    │  │ 机械执行    │
│ 结构化提取  │  │ checklist   │  │ 精确引用    │
│ 精确溯源    │  │ 风险识别    │  │ 不重述      │
└─────────────┘  └─────────────┘  └─────────────┘
```

### 为什么是4个？

| Agent | 满足标准1(Context隔离)? | 满足标准2(思维差异)? |
|-------|------------------------|---------------------|
| Academic Partner | ❌ 需要完整Context | 批判性思考 |
| Literature Agent | ✅ 只需文献+框架 | 深度理解、溯源 |
| PR Manager | ⚠️ 部分（意图+规则） | 流程验证、checklist |
| Archivist | ✅ 只需变更内容 | 机械执行 |

### 为什么PR Manager单独？

从MEMORY.md的教训：
> "PR-0004合并时遗漏了3条参考文献，尽管`/merge-pr`工作流明确要求'新引用检查'"
> "长对话中，AI在执行过程中没有按工作流逐项检查，而是直觉式操作"

**结论**：批判性思考和checklist执行是两种不同的思维，放在同一个Agent会导致长对话中流程遗漏。

---

## 8. PR Manager"全文理解"问题的深度分析

### 用户最新反馈（原文）

> "关于修改的那一部分，PR manager那一部分，我觉得有时候他修改的时候，我感觉很多时候他并没有很好地理解全文的，你知道吗？就很好，就是没有很好地理解全文。"

### 从proj_tpl获得的启发

在 proj_tpl 中，`dev` 角色有一个关键设计：

> "你的职责不是决定做哪个 Epic（那是 biz-owner），也不是改 PRD / 改技术方案（那是 prd / tech / proj），而是：在已经确定好的 Story / Task / 技术方案 / 项目计划基础上，真正把任务做完。"

**关键模式**：
- `dev` 不需要理解"业务全貌"
- 它只需要理解 `TASK描述 + TECH方案 + STORY的AC`
- 如果上游输入不清晰，`dev` 用 `[OPEN]` 标记问题，**回推上游**

### 问题根因分析

PR Manager "不理解全文" 的真正原因是：

| 表面问题 | 根因 |
|---------|------|
| PR Manager 不理解全文 | Academic Partner 没有输出足够清晰的"修改规格" |
| PR Manager 需要猜测意图 | 上游给的是模糊指令而不是结构化任务 |
| 修改结果偏离预期 | 缺少明确的验收标准 |

### 解决方案：结构化的任务交接

**不是让 PR Manager 理解全文，而是让 Academic Partner 输出清晰的修改规格。**

```
┌─────────────────────────────────────────────────────────────┐
│                   Academic Partner                           │
│                                                              │
│  理解全文 → 批判性思考 → 生成【修改规格】                      │
│                                                              │
│  修改规格包含：                                               │
│  - 原文是什么（精确引用）                                     │
│  - 为什么要改（论证）                                         │
│  - 改成什么（目标状态）                                       │
│  - 验收标准（AC）                                            │
│  - 需要的文献支持（如有）                                     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓ 结构化的修改规格
┌─────────────────────────────────────────────────────────────┐
│                      PR Manager                              │
│                                                              │
│  职责：                                                       │
│  1. 验证规格是否完整（不完整则回推 [OPEN]）                    │
│  2. 执行10步合并checklist                                     │
│  3. 检查引用完整性                                            │
│  4. 确保状态同步                                              │
│                                                              │
│  不做：                                                       │
│  - 不自己判断"应该怎么改"                                     │
│  - 不重新解读用户意图                                         │
│  - 不跳过checklist                                            │
└─────────────────────────────────────────────────────────────┘
```

### 关键设计：升级规则

借鉴 proj_tpl 的升级规则：

**PR Manager 必须回推的情况**：
- 修改规格不完整（缺少原文/目标/AC）
- 发现引用缺失但没有提供来源
- checklist 项无法满足
- 发现与其他文件冲突

**回推格式**：
```markdown
[OPEN] 修改规格不完整
- 缺失项：原文引用
- 需要：Academic Partner 提供 Draft.md 中的精确原文位置
```

### 新的职责划分

| Agent | 理解全文？ | 核心职责 | 思维方式 |
|-------|----------|---------|---------|
| Academic Partner | ✅ 是 | 把模糊想法变成**结构化的修改规格** | 批判性思考 |
| PR Manager | ❌ 否 | 验证规格完整性 + 执行checklist | 流程验证 |
| Archivist | ❌ 否 | 精确执行文件操作 + 状态同步 | 机械执行 |

### 这解决了原始矛盾

- PR Manager 不需要理解全文 → Context 可以隔离
- 但修改结果准确 → 因为上游规格清晰
- 如果规格不清晰 → PR Manager 回推，而不是猜测

---

## 9. Anthropic 官方最佳实践研究

### 来源

- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Claude 4 Prompting Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices)

### 核心设计原则

#### 1. 简洁性优先

> "Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."

**应用**：不需要为每个功能创建 Agent，只有满足两个标准的才独立：
- Context 需要隔离
- 思维方式截然不同

#### 2. 提示词的"黄金区间"（Goldilocks Zone）

> "System prompts should be extremely clear and use simple, direct language that presents ideas at the right altitude—the Goldilocks zone between overly complex, brittle logic and vague, high-level guidance."

**两个极端要避免**：
- **太脆弱**：硬编码复杂逻辑，维护成本高
- **太模糊**：没有提供具体信号，假设共享上下文

**最佳做法**：
- 足够具体以引导行为
- 足够灵活以提供强启发式

#### 3. 工具设计 = 提示词设计

> "Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts."

**关键点**：
- 每个工具需要独特的目的和清晰的描述
- 在提示词中嵌入显式的工具选择启发式
- 先检查所有可用工具，匹配工具使用到用户意图

#### 4. 多 Agent 系统的任务委派

> "Designing good prompts turned out to be the single most important way to guide how the agents behaved. Since each agent is controlled by its prompt, small changes in phrasing could make the difference between efficient research and wasted effort."

**最佳实践**：
- 每个 subagent 接收：目标、输出格式、工具和来源指导、清晰的任务边界
- 详细的任务描述防止重复；模糊的指令会失败
- 嵌入"努力规模规则"：简单任务 1 个 agent + 3-10 次工具调用，复杂任务 10+ subagents

#### 5. 升级规则

> "The team explicitly designed guardrails to prevent agents from spiraling out of control."

**实现**：
- 明确什么时候需要回推上游
- 用 `[OPEN]` 标记问题
- 设置显式的护栏

#### 6. Claude 4.x 特定建议

**明确指令**：
```
# 不够明确
Create an analytics dashboard

# 更明确
Create an analytics dashboard. Include as many relevant features
and interactions as possible. Go beyond the basics.
```

**提供动机**：
```
# 不够好
NEVER use ellipses

# 更好
Your response will be read aloud by a text-to-speech engine,
so never use ellipses since the TTS engine won't know how to pronounce them.
```

**避免过度工程**：
```
Avoid over-engineering. Only make changes that are directly requested
or clearly necessary. Keep solutions simple and focused.

Don't add features, refactor code, or make "improvements" beyond what was asked.
```

### 对我们架构的启发

| Anthropic 原则 | 应用到我们的系统 |
|---------------|-----------------|
| Orchestrator-Worker 模式 | Academic Partner (协调) + 3个专家 Agent |
| 详细的任务委派 | Academic Partner 输出结构化的"修改规格" |
| 升级规则 | 每个 Agent 明确"必须回推"的情况 |
| 工具设计 = 提示词设计 | 每个 Agent 的工具需要精确描述 |
| 黄金区间 | 提示词不要太脆弱也不要太模糊 |
| 并行执行 | 文献搜索可以并行，修改必须顺序 |

---

## 10. 设计文档索引

### 已完成的设计文档

| 文档 | 路径 | 内容 |
|-----|------|------|
| 本文档 | `MULTI_AGENT_DESIGN_DISCUSSION.md` | 设计讨论过程、决策理由 |
| 能力卡片 | `AGENT_CAPABILITY_CARDS.md` | 4 个 Agent 的详细能力定义 |
| 通信设计 | `AGENT_COMMUNICATION_DESIGN.md` | Agent 间通信机制、工具规范 |

### 设计总结

1. ✅ **PR Manager"全文理解"问题**：通过结构化的修改规格解决
2. ✅ **Anthropic最佳实践研究**：黄金区间、工具设计、升级规则
3. ✅ **4个Agent能力卡片**：Academic Partner, Literature Agent, PR Manager, Archivist
4. ✅ **Agent间通信机制**：基于 Task Delegation Mod
5. ✅ **工具设计规范**：每个工具有使用时机和不要使用说明
6. ✅ **PR Scope设计**：映射到 Project Mod

---

## 11. 实现路线图

### Phase 1: 基础架构（Week 1）

**目标**：让 Network 能跑起来，Academic Partner 能与用户对话

**任务**：
1. 更新 `network.yaml` 配置
   - 添加 Project Mod（thesis_modification 模板）
   - 添加 Task Delegation Mod
   - 配置 Agent Groups

2. 实现 Academic Partner 基础版
   - 基于 WorkerAgent
   - 能接收用户消息
   - 能创建 PR（Project）

3. 测试：用户能通过 Studio 与 Academic Partner 对话

### Phase 2: 专家 Agent 实现（Week 2）

**目标**：实现 Literature Agent，能完成一次完整的文献阅读任务

**任务**：
1. 实现 Literature Agent
   - 文献读取工具
   - 结构化笔记输出
   - 任务完成返回

2. 实现 Academic Partner 的委派能力
   - `delegate_literature_task` 工具
   - 处理任务完成通知

3. 测试：用户请求阅读文献 → Academic Partner 委派 → Literature Agent 返回笔记

### Phase 3: PR 流程实现（Week 3）

**目标**：完整的 PR 创建-验证-合并流程

**任务**：
1. 实现 PR Manager
   - 规格验证工具
   - 10步 Checklist 执行
   - 升级规则（回推 [OPEN]）

2. 实现 Archivist
   - 文件操作工具
   - 索引同步

3. 测试：完整的 PR 生命周期

### Phase 4: 集成与优化（Week 4）

**目标**：端到端流程、错误处理、用户体验

**任务**：
1. 端到端集成测试
2. 超时处理
3. 错误恢复
4. 用户体验优化
5. 文档完善

---

## 12. 下一步行动

### 立即可做（今天）

1. **更新 `network.yaml`**：添加新的 Mod 配置
2. **创建 Academic Partner 基础版**：能接收消息、创建 Project
3. **运行测试**：确保 Network 能正常启动

### 需要进一步研究

1. OpenAgents 的 Python Agent 实现细节
2. Mem0 集成方式
3. Studio 的前端定制

---

## 13. 关键文件引用

- `/Reflections/Hackathon/ARCHITECTURE_V2.md` - 三层架构设计
- `/Reflections/Hackathon/ARCHITECTURE_REDESIGN.md` - 最初的架构反思
- `/proj_tpl/.claude/agents/*.md` - 5个Agent的能力卡片模板
- `/MEMORY.md` - 用户偏好和历史问题
- `/academic_network/agents/*.yaml` - 当前Agent配置

---

## 附录：OpenAgents能力映射

| 我们的概念 | OpenAgents对应 |
|-----------|---------------|
| PR Scope（任务边界） | Project Mod |
| PR内的共享上下文 | project.global_state |
| Agent私有笔记 | project.agent_state |
| 产出物 | project.artifact |
| Agent间通信 | Events (task.delegate, task.complete) |
| 用户入口 | Messaging Mod / Channel |
