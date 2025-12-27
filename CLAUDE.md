# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **software-engineered thesis collaboration system** for an undergraduate thesis: "The Impact of AI Literacy on Upward Influence Behavior among Generation Z Employees: A Resource Dependence Perspective."

The core idea: apply version control, code review, and CI/CD practices to academic writing. Every thesis modification goes through a Pull Request.

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `Target/` | Thesis output (`Draft.md`) |
| `Reference/` | Literature library with PDF→Markdown conversions |
| `Consensus/` | Q&A records with academic AI (Consensus) |
| `PR/` | Modification requests (Pull Requests) |
| `.agent/rules/` | AI behavior constraints |
| `.agent/workflows/` | Operation workflows |
| `academic_network/` | Multi-agent collaboration system (OpenAgents) |
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
| `/sync` | Synchronize system state |
| `/reflect` | Extract insights after discussion |

## Critical Constraints

1. **Never edit `Target/Draft.md` directly** - all changes must go through `/create-pr`
2. **Never fabricate literature** - all arguments must cite sources from `Reference/`
3. **Citation format**: GB/T 7714-2015 (Author-Year system), e.g., `(Qin et al., 2018)`
4. **Thesis language**: English for main text, Chinese for discussions/notes
5. **PR merge rule**: Never overwrite detailed PR content; only update status and checkboxes

## PDF to Markdown Conversion

```bash
# Set API key
set DATALAB_API_KEY=your_key

# Place PDFs in Reference/PDF-MD/pdfs/
# Run conversion
python Reference/PDF-MD/convert_api.py
```

Uses Marker API (datalab.to) for conversion. Output goes to `Reference/PDF-MD/output_api/`.

## Academic Network (Multi-Agent System)

Built on OpenAgents framework. Located in `academic_network/`.

```bash
# Install dependencies
pip install -r academic_network/requirements.txt

# Start network (HTTP: 8700, gRPC: 8600)
# Requires OpenAgents CLI
```

Agent roles:
- **facilitator**: Coordinator, dispatches tasks
- **literature-agent**: Literature analysis
- **critical-thinker**: Critical evaluation
- **pr-manager**: Change control

## AI Persona

When working on this project, Claude should act as a **critical academic partner**:
- Challenge assumptions, don't just agree
- Literature is truth - arguments must stand on citations
- Prefer asking probing questions before writing for the user
- Distinguish between generic content (AI can write) and personalized content (requires user input)

## Memory Behavior

Update `MEMORY.md` when:
- User states preferences: "I prefer...", "Don't..."
- User corrects AI assumptions
- Important insights emerge
- User says "remember this"

## Context Loading (at conversation start)

1. Read `Consensus/_CONTEXT.md` (current progress)
2. Check `PR/` for active PRs (status: pending/doing)
3. Read `MEMORY.md` (preferences, insights)
4. Read `Target/Draft.md` key sections (Abstract, Research objectives, Propositions)
