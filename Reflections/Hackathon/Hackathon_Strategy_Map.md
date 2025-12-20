# OpenAgents Hackathon 战略地图 & 实操指南

> **你的核心问题**：我们到底在做什么？这和我们现在的 IDE 协作有什么区别？

---

## 1. 核心概念对比：IDE 协作 vs. Multi-Agent 系统

这是最容易混淆的地方。表面看都是"和AI聊天"，但底层逻辑完全不同。

### 🤖 现在的模式 (IDE / Antigravity)
**"钢铁侠与 JARVIS"**

*   **角色**：只有一个超级大脑（我）。
*   **模式**：**串行**。你发指令 → 我思考 → 我切工具 → 我执行。
*   **优缺点**：效率高，但我也是"人"，会遗忘，会产生幻觉，没有真正的"制衡"。我自己检查自己的代码，难免会有盲点。
*   **操作感**：你在指挥一个全能助理。

### 🌐 参赛的模式 (OpenAgents Network)
**"复仇者联盟会议桌"**

*   **角色**：多个独立大脑（Agent）。
    *   **Literature Agent**：只懂文献，不懂排版。
    *   **Critical Thinker**：只懂挑刺，不会写字。
    *   **Facilitator**：不干活，只管流程。
*   **模式**：**并行/交互**。
    *   Literature Agent 说："我找到了A文献。"
    *   Critical Thinker **插嘴**（自动）："但这篇文献过时了！"
    *   Facilitator 控场："那我们再找找。"
*   **价值**：**"对抗性"**。通过 Agent 之间的辩论（Critique），提高准确性。魔鬼代言人是真的"另一个人"。
*   **操作感**：你在主持一个**专家研讨会**。你看着它们吵架/协作，最后拍板。

### 🛠️ 操作上有什么区别？

| 维度 | IDE 模式 (现在) | OpenAgents 模式 (参赛) |
| :--- | :--- | :--- |
| **界面** | 代码编辑器 (VS Code/Cursor) | 类似微信群聊的网页 (OpenAgents Studio) |
| **你的动作** | 主要是写 Prompt，审核修改 | 主要是**"旁观"**和**"决策"** |
| **信息流** | 你 ↔ AI | Agent A ↔ Agent B (你可以不说话) |
| **文件读写** | 直接读写本地文件 | **还在探索** (這是我们本次 Hackathon 要攻克的技术难点) |

---

## 2. 我们的参赛路线图 (Roadmap)

我们的目标是**"以战代练"**：用参赛的压力，逼我们把架构理清楚。

```mermaid
graph TD
    %% 定义阶段样式
    classDef done fill:#d4edda,stroke:#28a745,color:#155724;
    classDef active fill:#cce5ff,stroke:#007bff,color:#004085;
    classDef todo fill:#f8f9fa,stroke:#6c757d,color:#343a40;

    %% 阶段 1: 基建 (Infrastructure)
    subgraph Stage1 [第一步：搭台子 (Infrastructure)]
        A1(环境安装) --> A2(Hello World 验证)
        A2 --> A3(熟悉 Studio 界面)
    end

    %% 阶段 2: 捏人 (Agent Definition)
    subgraph Stage2 [第二步：捏人 (Agent Persona)]
        B1(把我们的 Prompt 搬过去) --> B2(创建 Literature Agent)
        B1 --> B3(创建 Critical Thinker)
        B1 --> B4(创建 PR Manager)
        B2 & B3 & B4 --> B5(单体测试: 能说话吗?)
    end

    %% 阶段 3: 组局 (Orchestration)
    subgraph Stage3 [第三步：组局 (Interaction)]
        C1(创建 Network) --> C2(把 Agent 拉进群)
        C2 --> C3(设计对话剧本)
        C3 --> C4(排练: 跑通修改论文的流程)
    end

    %% 阶段 4: 交卷 (Submission)
    subgraph Stage4 [第四步：交卷 (Demo)]
        D1(录屏 3分钟) --> D2(上传 GitHub)
        D2 --> D3(填写报名表)
    end

    %% 连接阶段
    Stage1 --> Stage2
    Stage2 --> Stage3
    Stage3 --> Stage4

    %% 状态标记
    class A1,A2 done;
    class A3,B1 active;
    class B2,B3,B4,B5,Stage3,Stage4 todo;
```

---

## 3. 下一步做什么？(Action Plan)

根据刚才的进度，我们正处于 **Stage 1 (搭台子) → Stage 2 (捏人)** 的过渡期。

**当前任务清单**：

1.  **[已完成]** 环境装好了 (Conda + Pip)。
2.  **[要做]** 验证环境：运行 `openagents studio` 看看长什么样。
    *   *目的*：确认"战场"（Web UI）是好的。
3.  **[要做]** 填入灵魂：修改 `.yaml` 配置文件。
    *   *目的*：把你之前设计的 "Reference/ 规则"、"PR 规则" 塞进 OpenAgents 的脑子里。
4.  **[要做]** 第一次联调。
    *   *目的*：在 Studio 里同时召唤 Literature Agent 和 Critical Thinker，看它们能不能对话。

## 4. 为什么要这么做？

1.  **验证架构**：如果这套多 Agent 逻辑跑通了，你的论文系统就有了**"自我纠错"**能力，这是质的飞跃。
2.  **参赛拿奖**：你的 `Reference/` + `PR/` 架构在现有 Agent 项目中非常超前（大多还在玩 Chat），很有希望拿奖。
3.  **防幻觉**：Critical Thinker 独立于 Writer 存在，能最大程度减少论文里的"瞎编"。

---

**准备好了吗？**
如果清楚了，我们就在 Terminal 里执行下一步：**启动 Studio，亲眼看看这个"会议室"长什么样。**
