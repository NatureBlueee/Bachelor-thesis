# 新文献批量阅读规划

> **创建日期**: 2025-12-26 09:30
> **状态**: 🟡 执行中
> **目的**: 处理21篇新入库文献，提取与论文相关的价值，更新研究Gap论证
> **关联任务**: PR-0010, Task-0001, Task-0003

---

## 背景

用户通过PDF-MD工具批量转换了21篇新文献（跳过2篇大文件）。需要逐一阅读并评估其对论文的价值。

**论文核心关注**：
- 自变量：Z世代AI素养（知识、情感、思维）
- 中介：感知资源优势
- 因变量：向上影响行为
- 调节：上级开放性
- 理论：资源依赖理论(RDT)、领导身份建构理论

**关键搜索词**：
- Resource Dependence / RDT
- Upward Influence / Voice
- AI Literacy
- Generation Z / Gen Z
- Supervisor / Manager Openness
- Proactive Behavior

---

## 执行计划

### 批次1：高优先级（直接相关）【#111-#119】

| # | 文献名 | 预期相关度 | 状态 |
|---|--------|-----------|------|
| 111 | A taxonomy framework and process model to explore AI-enabled workplace inclusion | ⭐⭐⭐ | ⏳ |
| 114 | Artificial Intelligence, Organizational Justice and Organizational Trust | ⭐⭐⭐ | ⏳ |
| 115 | Generative AI in Business - Towards a Strategic HRM Framework | ⭐⭐⭐⭐⭐ | ⏳ |
| 116 | Human-AI collaboration in the workplace | ⭐⭐⭐⭐ | ⏳ |
| 119 | INVITED REVIEW (HRM in the age of GenAI, 54页) | ⭐⭐⭐⭐⭐ | ⏳ |

### 批次2：中优先级（可能相关）【#120-#124】

| # | 文献名 | 预期相关度 | 状态 |
|---|--------|-----------|------|
| 121 | Perceived Usefulness, Perceived Ease of Use (TAM原论) | ⭐⭐⭐ | ⏳ |
| 124 | 人工智能对企业人力资源管理实践影响研究 | ⭐⭐⭐⭐ | ⏳ |
| 128 | 基于生成式人工智能的经济管理学科相关研究综述 | ⭐⭐⭐⭐⭐ | ✅ 已读 |

### 批次3：低优先级（边缘相关）【#112, #113, #117, #118, #122-#131】

| # | 文献名 | 预期相关度 | 状态 |
|---|--------|-----------|------|
| 112 | AIGC技术赋能广告内容生产 | ⭐ | ⏳ |
| 113 | AI赋能企业财务管理价值提升 | ⭐ | ⏳ |
| 117 | Fairness and Bias in Multimodal AI - A Survey | ⭐⭐ | ⏳ |
| 118 | Fairness and Bias in AI - Systematic Review | ⭐⭐ | ⏳ |
| 120 | L'intelligence artificielle au service de la gestion | ⭐ | ⏳ |
| 122 | 人工智能在财会领域的应用 | ⭐ | ⏳ |
| 123 | 人工智能在高校教学与管理 | ⭐ | ⏳ |
| 125 | 人工智能技术在抑郁症临床管理 | ⚪ | ⏳ |
| 126 | 人工智能技术对学生价值观形成 | ⚪ | ⏳ |
| 127 | 人工智能时代科技企业管理变革 | ⭐⭐ | ⏳ |
| 129 | 学校人工智能应用亟需有效的社会监督 | ⚪ | ⏳ |
| 130 | 生成式人工智能的偏见：主要表现、发生机制与治理路径 | ⭐⭐ | ⏳ |
| 131 | 生成式人工智能赋能软件工程教育 | ⚪ | ⏳ |

---

## 执行流程

每篇文献：
1. 快速扫描摘要和结论
2. 搜索关键词（RDT, upward influence, Gen Z等）
3. 评估相关度
4. 如高度相关 → 深度阅读，提取引用
5. 更新笔记文档

每2-3篇后：
- 更新本规划的状态
- 追加发现到 `Reference/Note/Uncited_Literature_Findings.md`

---

## 输出位置

- **阅读笔记**: `Reference/Note/Uncited_Literature_Findings.md`
- **本规划文档**: `PR/PR-0010-Tasks/Literature_Batch_Reading_Plan.md`

---

## 当前进度

### 已完成（6篇）
- [x] #128 基于生成式人工智能的经济管理学科相关研究综述
  - RDT未被提及 ✅ 理论Gap确认
  - 识别了4篇HR相关文献[183]-[186]
- [x] #119 INVITED REVIEW (HRM in the age of GenAI)
  - Open RBV框架、human-centric AI
  - 确认综述未提及RDT、向上影响、Z世代 → 理论贡献空间
- [x] #115 Generative AI in Business - Strategic HRM Framework
  - 70%AI项目失败、HRM Institutional Entrepreneurship
  - Eight Complexities框架
- [x] #116 Human-AI collaboration in the workplace (Patil 2024)
  - Augmentative Intelligence概念
  - 新职业角色出现
- [x] #124 人工智能对企业人力资源管理实践影响研究
  - "改善而非替代"表述
  - 五维度影响框架
- [x] #122 Generation Z: AI Affinity (Nebgen & Kurz 2024)
  - ⭐黄金数据：41%Z世代使用AI、58.42%认为Z世代发挥核心作用
  - 46%更愿意咨询AI而非同事/上司
  - 62%担心AI导致失业
- [x] ★★★ 人工智能冲击意识对Z世代员工主动性创新行为的影响（付春香、侯庭轩 2025）
  - 极其重要！直接相关核心研究问题
  - AI冲击意识→工作不安全感/工作旺盛感→主动性创新行为
  - 用COR理论，我们用RDT → 理论对话机会

### 进行中
- [ ] 继续扫描剩余文献

### 待处理（13篇）
- [ ] 批次2：#121
- [ ] 批次3：#112, #113, #117, #118, #120, #123, #125, #126, #127, #129, #130, #131

---

## 如果上下文重载

**重新加载后请执行**：
1. 读取本文档：`PR/PR-0010-Tasks/Literature_Batch_Reading_Plan.md`
2. 检查"当前进度"部分
3. 继续未完成的批次
4. 每完成2-3篇更新本文档状态

---

## non-academic报告状态

| 报告 | 状态 | 发现 |
|------|------|------|
| McKinsey Superagency | ✅ 已处理 | 员工AI使用是领导估计的3倍 |
| Deloitte 2025 | ✅ 已处理 | 57% Z世代日常使用GenAI |
| OpenAI Enterprise | ✅ 已处理 | 岗位级每日节省40-80分钟 |
| IWG 2025 | ✅ 已处理 | 59% Z世代指导年长同事 |
| WEF Future of Jobs | ⏳ 待深入 | 已有分析文档 |
