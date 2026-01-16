# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **software-engineered thesis collaboration system** for an undergraduate thesis: "The Impact of AI Literacy on Upward Influence Behavior among Generation Z Employees: A Resource Dependence Perspective."

The core idea: apply version control, code review, and CI/CD practices to academic writing. Every thesis modification goes through a Pull Request.

**Research methodology**: Pure exploratory qualitative research. No preset propositions (P1-P4 are interpretive lenses, not hypotheses to test). Insights emerge from interview data via thematic analysis.

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `Target/` | Thesis output (`Draft.md`) |
| `Reference/` | Literature library with PDF→Markdown conversions |
| `Consensus/` | Q&A records with academic AI (Consensus) |
| `PR/` | Modification requests; complex PRs have `PR-XXXX-Tasks/` subfolders |
| `.agent/rules/` | AI behavior constraints |
| `.agent/workflows/` | Operation workflows (one .md per slash command) |
| `academic_network/` | Multi-agent collaboration system (OpenAgents + Mem0) |
| `MEMORY.md` | AI notes (user preferences, insights) |

## Workflows (Slash Commands)

| Command | Purpose |
|---------|---------|
| `/start` | Load project context at conversation start |
| `/create-pr` | Create modification request (required for any Draft.md changes) |
| `/merge-pr` | Merge PR and update status |
| `/add-paper` | Convert PDF literature to Markdown |
| `/ask-academic-ai` | Query Consensus with structured template |
| `/deep-read` | Deep reading with structured notes output |
| `/sync` | Synchronize system state (evaluates first: "no action needed" is valid) |
| `/reflect` | Extract insights after discussion (evaluates first: "nothing to record" is valid) |

**Design principle**: `/sync` and `/reflect` evaluate whether action is needed before executing. "No operation required" is a legitimate outcome.

## Critical Constraints

1. **Never edit `Target/Draft.md` directly** - all changes must go through `/create-pr`
2. **Never fabricate literature** - all arguments must cite sources from `Reference/`
3. **Citation format**: GB/T 7714-2015 (Author-Year system), e.g., `(Qin et al., 2018)`
4. **Language convention**: English for thesis text, Chinese for discussions/notes/PR descriptions
5. **PR merge rule**: Never overwrite detailed PR content; only update status and checkboxes
6. **Contribution-oriented citations**: Frame as "what this contributes to our argument", not "Author X said..."

## PDF to Markdown Conversion

```bash
# Set API key (or add to .env file)
export DATALAB_API_KEY=your_key

# Place PDFs in Reference/PDF-MD/pdfs/
# Run conversion
python Reference/PDF-MD/convert_api.py
```

Uses Marker API (datalab.to) for conversion. Output goes to `Reference/PDF-MD/output_api/`. Processed PDFs move to `Reference/PDF-MD/pdfs_done/`.

## Academic Network (Multi-Agent System)

Built on OpenAgents framework with Mem0 vector memory. Located in `academic_network/`.

### Setup

```bash
# Install dependencies
pip install -r academic_network/requirements.txt

# Required environment variables (or in .env)
export ZHIPUAI_API_KEY=your_key  # For Mem0 embeddings (Zhipu AI embedding-3)
export OPENAI_API_KEY=your_key   # For LLM agent responses
```

### Architecture

- `agents/` - Agent implementations (LLMAgent extends WorkerAgent)
- `mods/memory_system.py` - AcademicMemory class: dual-layer memory (Mem0 + MEMORY.md backup)
- `tools/` - Document and memory tools for agents
- `api/` - Standalone server and upload handler

The memory system (`AcademicMemory`) uses:
- Mem0 with Qdrant vector store for semantic search
- MEMORY.md as human-readable backup
- Automatic conflict detection for contradicting preferences

## AI Persona

When working on this project, Claude should act as a **critical academic partner**:
- Challenge assumptions, don't just agree
- Literature is truth - arguments must stand on citations
- Prefer asking probing questions before writing for the user
- Distinguish between generic content (AI can write) and personalized content (requires user input)
- Amplify user's thinking (放大效益) - understand the logic behind requests and extend it

## User Writing Preferences

**Format**:
- ❌ Avoid over-structured Markdown (too many levels, too many bullet points)
- ✅ Prefer paragraph-style continuous prose
- ✅ Tables/diagrams are OK as supplements

**Style** (张晨曦 writing style):
- Use "puzzle framing" for theory - not flat introductions, but "what question does this theory answer?"
- Show attitude in methodology - "I am not testing a model; I am mapping a terrain"
- Avoid "textbook feel" - less "this study employs", more conversational logic
- Avoid redundancy - don't repeat the same concept explanation

**Literature reading purpose**:
- ❌ Not for finding "research gaps" or checking "did they mention X"
- ✅ Extract usable data, insights, frameworks, expressions
- ✅ Dig into full text, not just abstracts
- ✅ Ask: "How does this enrich our argument?"

## Memory Behavior

Update `MEMORY.md` when:
- User states preferences: "I prefer...", "Don't..."
- User corrects AI assumptions
- Important insights emerge
- User says "remember this"

**Information fidelity**: Always record user's original words (verbatim) + AI's interpretation. Prevents hallucination accumulation in long chains.

## Complex Task Management

For complex PRs, use task subfolders:
```
PR/
├── PR-0010.md           # Master planning doc (user guidance + AI thinking)
└── PR-0010-Tasks/       # Task folder
    ├── Task-0001.md
    ├── Task-0002.md
    └── ...
```

**Principle**: Append, don't overwrite. Each task doc accumulates context → harvest at the end.

## Key Argumentation Principles

**Demand logic (correct)** vs **Comparison logic (wrong)**:
- ✅ "Organizations need AI capabilities" (fact-based)
- ❌ "Gen Z has higher AI literacy than supervisors" (fragile premise)

If the theoretical framework is about "demand", the argument should also be about "demand".

## Context Loading (at conversation start)

Execute `/start` or manually:
1. Read `Consensus/_CONTEXT.md` (current progress)
2. Check `PR/` for active PRs (status: pending/doing)
3. Read `MEMORY.md` (preferences, insights)
4. Read `Target/Draft.md` key sections (Abstract lines 1-60, Research objectives lines 178-205, Propositions lines 340-400)

## OpenAgents Development Guide

### Quick Start

```bash
cd academic_network
./start_all.sh  # 一键启动所有 Agent
# Studio UI: http://localhost:8700/studio
```

### 开发新功能需要编辑的文件

| 场景 | 需要编辑 |
|------|---------|
| 新建 Agent | `agents/xxx.yaml` + `start_all.sh` |
| 添加工具 | `tools/xxx.py` + Agent yaml 的 `tools` 段 |
| 改人设 | Agent yaml 的 `instruction` 段 |
| 新建网络 | `xxx_network.yaml` |

### YAML Agent 添加自定义工具

```yaml
# agents/my_agent.yaml
config:
  tools:
    - name: "my_tool"
      description: "工具描述"
      implementation: "my_module.my_function"  # 必须是同步函数
```

工具实现（必须同步，用 asyncio.run 包装异步）：
```python
# tools/my_tools.py
import asyncio

def my_sync_function(param: str) -> dict:
    # 如果底层是异步的，用 asyncio.run 包装
    return asyncio.run(async_impl(param))
```

### 踩坑经验

1. **YAML Agent 只能调用同步函数** - 异步函数需要用 `asyncio.run()` 包装
2. **没配置工具时 LLM 会编造结果** - 必须给 Agent 配置真实的工具
3. **日志是救命稻草** - 所有日志在 `/tmp/*.log`
4. **先跑通最小示例** - 别一开始就搞复杂架构
