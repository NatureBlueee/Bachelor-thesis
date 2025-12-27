# Academic Research Network - Complete Handoff Document

> **Date**: 2025-12-27  
> **Project**: Academic Research Network (OpenAgents Multi-Agent Hackathon 2025)  
> **Status**: Core infrastructure complete, ready for network testing

---

## Executive Summary

This document provides a comprehensive handoff for continuing development of the **Academic Research Network** - a multi-agent collaborative system designed for academic thesis writing. The system is built on the OpenAgents framework and aims to transform a local IDE-based thesis collaboration workflow into a universal, multi-agent research assistant.

---

## Part 1: Project Background and Motivation

### 1.1 The Origin Story

The user is writing their **undergraduate thesis** titled:
- **Chinese**: AI素养对Z世代员工向上影响行为的影响：资源依赖视角
- **English**: The Impact of AI Literacy on Upward Influence Behavior among Generation Z Employees: A Resource Dependence Perspective

During the thesis writing process, the user developed a sophisticated **local collaboration system** using VS Code with an AI assistant (Gemini/Antigravity). This system includes:

1. **PR-Driven Modification System**: All thesis changes go through Pull Requests (similar to Git workflow)
2. **Memory System**: `MEMORY.md` stores AI discussion notes, user preferences, and insights
3. **Literature Management**: Organized `Reference/Cited/` and `Reference/Uncited/` directories with PDF-to-Markdown conversion
4. **Structured Workflows**: 9 defined workflows (e.g., `/start`, `/create-pr`, `/merge-pr`, `/deep-read`, `/reflect`)
5. **Negative Constraints Design**: Telling AI "what NOT to do" rather than just "what to do"

### 1.2 Why Build a Multi-Agent System?

The user discovered the **OpenAgents Multi-Agent Hackathon 2025** and decided to transform their local system into a universal research tool. The core insight is:

> "The rigor of academic writing workflows can be encoded into agent interactions."

**Key differentiators from typical AI writing tools**:
1. **PR-Driven Iteration**: Every modification is tracked, reviewed, and approved
2. **Mandatory Citation Checks**: No changes merged without verifying literature support
3. **Negative Constraints**: Agents are explicitly told what they CANNOT do
4. **Memory with Conflict Detection**: System detects when user preferences contradict earlier statements

### 1.3 Hackathon Goals

1. **Phase 1 (MVP)**: Build basic multi-agent collaboration on OpenAgents
2. **Phase 2**: Migrate core workflows (PR system, literature search)
3. **Phase 3**: Integrate intelligent memory (Mem0) and enhanced reading workflows

---

## Part 2: Technical Architecture

### 2.1 System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   Academic Research Network                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐│
│  │Facilitator│  │Literature │  │  Critical │  │    PR     ││
│  │(协调者)   │  │  Agent    │  │  Thinker  │  │  Manager  ││
│  │           │  │(文献专家) │  │ (批判者)  │  │(变更管理) ││
│  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘│
│        │              │              │              │       │
│        └──────────────┴──────────────┴──────────────┘       │
│                          ↕                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    Shared Resources                      ││
│  │   • Reference/ (Literature Library)                      ││
│  │   • PR/ (Change Management)                              ││
│  │   • MEMORY.md (AI Notes & Preferences)                   ││
│  │   • Target/Draft.md (Main Thesis Document)               ││
│  └─────────────────────────────────────────────────────────┘│
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Agent Definitions

| Agent | Type | Responsibility | Key Constraints |
|-------|------|----------------|-----------------|
| **Facilitator** | YAML (WorkerAgent) | Receives user requests, delegates to experts, integrates results | Must delegate literature questions to Literature Agent |
| **Literature Agent** | Python (WorkerAgent) | Searches local literature, deep reads papers, suggests citations | NO fabricating literature; prioritize Uncited over Cited |
| **Critical Thinker** | YAML (WorkerAgent) | Reviews arguments, checks logic, validates citations | Critique to improve, not to reject |
| **PR Manager** | YAML (WorkerAgent) | Creates/merges PRs, enforces 10-step verification | NEVER directly modify Draft.md |

### 2.3 File Structure

```
d:\Profolio\文章\Thesis\Graduate-thesis\
├── academic_network/           # OpenAgents implementation
│   ├── network.yaml            # Network configuration
│   ├── requirements.txt        # Python dependencies
│   ├── test_quick.py           # Quick validation script
│   ├── agents/
│   │   ├── facilitator.yaml    # Coordinator agent
│   │   ├── literature_agent.py # Literature expert (Python)
│   │   ├── critical_thinker.yaml
│   │   └── pr_manager.yaml
│   ├── mods/
│   │   └── memory_system.py    # Mem0 integration + MEMORY.md backup
│   └── tools/
│       └── document_tools.py   # File system access for agents
│
├── OpenAgents/                 # OpenAgents framework (cloned repo)
│
├── Reference/                  # Literature library
│   ├── Cited/                  # Papers already cited in thesis
│   ├── Uncited/                # Papers not yet cited (91 files)
│   └── PDF-MD/                 # PDF conversion tools
│
├── Target/                     # Thesis outputs
│   └── Draft.md                # Main thesis document
│
├── PR/                         # Pull Request management
│   ├── _INDEX.md               # PR status index
│   ├── PR-0001.md ... PR-0009.md
│
├── MEMORY.md                   # AI discussion notes & preferences
├── Consensus/                  # Academic AI Q&A records
│   └── _CONTEXT.md             # Current research status
│
└── .agent/                     # IDE agent configuration
    ├── rules/                  # Behavioral rules
    └── workflows/              # Defined workflows
```

### 2.4 Key Technologies

| Component | Technology | Notes |
|-----------|------------|-------|
| Agent Framework | OpenAgents 0.8.2 | Installed from local source |
| Memory Layer | Mem0 (optional) + MEMORY.md | Falls back to local file if Mem0 unavailable |
| LLM | gpt-4o-mini | Via OpenAI API |
| PDF Conversion | Datalab API | Existing tool in `Reference/PDF-MD/` |
| Network Transport | gRPC (port 8700) | HTTP also available |

---

## Part 3: What Was Accomplished

### 3.1 Infrastructure Created

1. **Network Configuration** (`network.yaml`)
   - Defined agent groups: coordinators, experts, managers
   - Configured messaging mod with channels: general, literature, methodology, writing
   - Created 3 project templates: thesis_modification, deep_reading, academic_discussion

2. **Four Agent Configurations**
   - Facilitator (YAML): Coordinator with event triggers
   - Literature Agent (Python): Local file access for literature search
   - Critical Thinker (YAML): Argument review with structured output
   - PR Manager (YAML): Change management with 10-step verification

3. **Memory System** (`mods/memory_system.py`)
   - `AcademicMemory` class with Mem0 integration
   - Conflict detection for contradicting preferences
   - Automatic sync to MEMORY.md as backup
   - Category-based storage: preference, decision, insight, constraint, correction, inspiration

4. **Document Tools** (`tools/document_tools.py`)
   - Literature search across Cited/Uncited directories
   - Relevance scoring algorithm
   - Draft.md reading (respects PR system - no direct writes)
   - PR status retrieval
   - PDF conversion integration

5. **Startup Scripts**
   - `start_academic_network.ps1`: One-click launcher
   - `test_quick.py`: Validation script (already tested successfully)

### 3.2 Testing Completed

| Test | Result | Notes |
|------|--------|-------|
| DocumentTools initialization | ✅ Pass | Project root correctly detected |
| Literature search | ✅ Pass | Found papers in both Cited and Uncited |
| Uncited literature count | ✅ Pass | 91 papers available |
| PR status retrieval | ✅ Pass | Correctly parsed PR/_INDEX.md |
| Draft.md reading | ✅ Pass | Successfully read thesis content |
| Memory conflict detection | ✅ Pass | Logic working correctly |
| MEMORY.md search | ✅ Pass | Found relevant records |
| OpenAgents CLI | ✅ Pass | `openagents --help` works |

### 3.3 Issues Resolved

1. **`python -m openagents` not working**: Solved by installing from local source with `pip install -e`
2. **CLI not on PATH**: Added `C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts` to PATH
3. **Mem0 API key warning**: Expected behavior - system gracefully falls back to MEMORY.md

---

## Part 4: Current Status

### 4.1 Where We Are Now

**Status**: Ready to start the OpenAgents network and test agent communication.

**Last completed step**:
```powershell
openagents --help  # Successfully shows CLI options
```

**Next step to execute**:
```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
$env:PYTHONUTF8 = "1"
$env:OPENAI_API_KEY = "sk-proj-xxx..."  # User has this key
openagents network start network.yaml
```

### 4.2 What Happens Next

After network starts successfully:

1. **Start Literature Agent** (in new terminal):
   ```powershell
   cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
   python agents/literature_agent.py
   ```

2. **Start YAML Agents** (in new terminals):
   ```powershell
   openagents agent start agents/facilitator.yaml
   openagents agent start agents/critical_thinker.yaml
   openagents agent start agents/pr_manager.yaml
   ```

3. **Access Studio**: http://localhost:8700/studio/

4. **Test Basic Flow**:
   - Create a project in Studio
   - Send a message like "帮我找关于 AI literacy 的文献"
   - Observe agent collaboration

---

## Part 5: Working Principles for Continuation

### 5.1 Core Philosophy

> **"Every discussion must yield tangible results."**

This means:
- Major decisions → Create PR
- Insights/corrections → Store in memory
- Literature discussions → Generate reading notes
- Small ideas → Captured in memory system

### 5.2 Negative Constraints (CRITICAL)

The system is designed with explicit prohibitions. These MUST be maintained:

| ❌ NEVER | ✅ INSTEAD |
|----------|-----------|
| Directly edit `Target/Draft.md` | Use `/create-pr` workflow |
| Fabricate literature citations | Only use papers from `Reference/` |
| Skip citation verification | Always run 10-step merge checklist |
| Ignore user corrections | Record in MEMORY.md |
| Give only conclusions | Provide methodology, sample, effect size |

### 5.3 Documentation Requirements

**For the continuing AI assistant**:

1. **Report key decisions in Chinese (中文)** to the user
2. **Document all changes** in appropriate files:
   - Technical changes → Update README or TESTING.md
   - Architecture decisions → Update ARCHITECTURE.md
   - Progress → Update `Consensus/_CONTEXT.md`
3. **Use PR system** for any thesis content modifications
4. **Update MEMORY.md** when user states new preferences

### 5.4 Communication Protocol

When working with the user:

1. **Before major actions**: Explain what you plan to do and why
2. **After completing tasks**: Summarize in Chinese what was accomplished
3. **When encountering issues**: Don't struggle silently - ask the user
4. **For commands that may fail**: Provide the command for user to run manually

---

## Part 6: Quick Reference

### 6.1 Important File Locations

| File | Purpose |
|------|---------|
| `academic_network/network.yaml` | Network configuration |
| `academic_network/agents/*.yaml` | Agent definitions |
| `academic_network/agents/literature_agent.py` | Python agent with file access |
| `MEMORY.md` | AI notes and user preferences |
| `PR/_INDEX.md` | Pull request status tracking |
| `Consensus/_CONTEXT.md` | Current research status |
| `Target/Draft.md` | Main thesis document |

### 6.2 Key Commands

```powershell
# Set environment (always run first in new terminal)
$env:PYTHONUTF8 = "1"
$env:Path += ";C:\Users\Lenovo\AppData\Roaming\Python\Python313\Scripts"
$env:OPENAI_API_KEY = "your-key"

# Quick test
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
python test_quick.py

# Start network
openagents network start network.yaml

# Start Python agent
python agents/literature_agent.py

# Start YAML agent
openagents agent start agents/facilitator.yaml
```

### 6.3 Troubleshooting

| Problem | Solution |
|---------|----------|
| `openagents` not found | Add Scripts folder to PATH |
| Network won't start | Check port 8700 is free |
| Agent can't connect | Ensure network is running first |
| Mem0 warnings | Normal - system uses MEMORY.md fallback |
| Chinese encoding issues | Set `$env:PYTHONUTF8 = "1"` |

---

## Part 7: Thesis Research Context

### 7.1 Research Questions

The thesis investigates:

1. **RQ1**: How does AI literacy influence Gen Z employees' perceived resource advantage?
2. **RQ2**: How does perceived resource advantage translate into upward influence behavior?
3. **RQ3**: How does supervisor openness moderate these relationships?

### 7.2 Theoretical Framework

| Theory | Role |
|--------|------|
| Resource Dependence Theory (Pfeffer & Salancik, 1978) | Main theoretical lens |
| AI Literacy Framework (钟柏昌, 2024) | Defines AI knowledge, affect, and thinking |
| Social Cognitive Theory (Bandura, 1997) | Explains perception formation |
| Leadership Construction Theory (DeRue & Ashford, 2010) | Explains influence dynamics |

### 7.3 Key Variables

| Variable | Type | Definition |
|----------|------|------------|
| AI Literacy | Independent | AI knowledge + AI affect + AI thinking |
| Perceived Resource Advantage | Mediator | Subjective belief that one holds AI resources the supervisor lacks |
| Upward Influence Behavior | Dependent | Idea generation, promotion, implementation |
| Supervisor Openness | Moderator | Supervisor's receptivity to subordinate input and new technology |

---

## Conclusion

This handoff document provides everything needed to continue developing the Academic Research Network. The system architecture is in place, core tools are tested, and the OpenAgents CLI is ready.

**Immediate next step**: Start the network with `openagents network start network.yaml` and verify agents can connect.

**Remember**: Always report key decisions to the user in Chinese, maintain the negative constraints, and document everything.

---

*Document prepared by: Antigravity AI Assistant*  
*Last updated: 2025-12-27 11:21*
