# Thesis Engineering System

**Write your thesis with Pull Requests. Make AI your research partner.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[中文](README.md) | [Architecture](ARCHITECTURE.md)

---

## ✨ Highlights

- 🔀 **PR-Driven** — Every change is traceable. No more "why did I write it this way?"
- 🧠 **AI with Memory** — Remembers your literature, preferences, and research progress
- 📚 **Literature-Grounded** — No fabrication. Every argument needs a source
- ⚡ **Slash Commands** — Standardized workflows: `/create-pr`, `/deep-read`, etc.

---

## 🎯 What Problem Does This Solve?

Ever experienced these while writing a thesis?

- Changed a paragraph, forgot why you wrote it that way
- Asked AI for help, got generic advice disconnected from your research
- Literature piling up, unsure what's actually relevant

This system combines **version control** with **AI memory**. Every change is a PR. AI understands your entire project.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/thesis-project.git

# 2. Set API key (for PDF conversion)
export DATALAB_API_KEY=your_key

# 3. Convert your PDF literature
cp *.pdf Reference/PDF-MD/pdfs/
python Reference/PDF-MD/convert_api.py

# 4. Start using
# In your AI IDE, type /start to load context
```

---

## 📖 Usage Examples

**Create a modification request:**
```
/create-pr
```
AI asks what you want to change and why, then generates a structured PR file.

**Deep read literature:**
```
/deep-read Reference/PDF-MD/output_api/some_paper.md
```
Outputs structured notes: core arguments, methods, relevance to your research.

**Query academic AI:**
```
/ask-academic-ai
```
Uses a four-part template (background, question, expectation, constraints) for precise answers.

---

## 📁 Project Structure

```
├── Target/Draft.md      # Thesis text (modified via PR)
├── Reference/           # Literature library (PDF → Markdown)
├── PR/                  # Modification request records
├── Consensus/           # Academic discussion records
├── MEMORY.md            # AI memory (preferences, insights)
└── .agent/              # AI rules and workflows
```

---

## 🛠️ Development Journey

### Origin

This project started with a simple question: **Why did software engineering abandon linear development long ago, while academic writing still insists on "write from start to finish, then revise"?**

In December 2025, I started experimenting with bringing version control and code review to thesis writing. The first version only had basic PR system and literature conversion.

### Problems Encountered

Through actual use, I discovered several core pain points:

**1. The Memory System Was the Biggest Pitfall**

The original `MEMORY.md` required manual maintenance. AI didn't remember what it should, and remembered what it shouldn't. Later, I introduced the Mem0 vector memory system, letting AI decide what's worth remembering.

**2. Literature Search Was Too Shallow**

Asked AI "does the literature mention X?", it said no, but actually yes. The reason was lack of hierarchical indexing—it should work like humans: first skim abstracts → then locate specific sections → then deep read paragraphs.

**3. Information Silos Between Layers**

PR, Consensus, Reference were all static files. They didn't know about each other's existence. Change one place, others don't sync automatically. This is exactly what Multi-Agent architecture can solve—each Agent handles one layer, Agents can communicate.

**4. "Partial Compliance" Problem**

AI sometimes only executed part of a workflow, forgetting later steps. Especially noticeable in long conversations. Later added `/sync` and `/reflect` workflows, forcing evaluation of "is this worth doing" first.

### Core Design Principles

**Negative Constraints Matter More Than Positive Guidance**

Rather than telling AI "what to do," explicitly define "what never to do":
- ❌ Never edit Draft.md directly
- ❌ Never fabricate literature
- ❌ Never give conclusions without granularity

These prohibitions in `.agent/rules/` are more effective than lengthy positive instructions.

**Literature is Truth, Discussion is Central**

All arguments must trace back to specific literature in `Reference/`. All insights come from conversation records. Fabrication is forbidden.

### An Interesting Discovery

This project itself is an instance of the phenomenon it studies.

My thesis researches: How Gen Z employees, by mastering AI literacy as a "scarce resource," gain perceived resource advantages and influence their supervisors upward.

My process of building this project: By mastering "engineered academic production" as a scarce resource (most students don't do thesis this way), I gained a perceived resource advantage, thereby influencing my supervisor's definition of "what good academic work looks like."

**This self-referential nature was an unexpected harvest.**

### Lessons Learned

Pitfalls documented in `MEMORY.md`:

- Simple, direct questions often work better than elaborate prompts
- Easy to miss references when merging PRs—added mandatory checklist later
- Thesis modifications can't be isolated; new content must echo existing citations
- Not every paper needs downloading; identification matters more than collection
- AI memory doesn't "happen automatically"—needs mechanisms to know what's worth remembering

---

## 🔮 Future Directions

- **Open Source**: Clean up sensitive info and publish
- **Multi-Agent**: Use OpenAgents for automatic coordination between layers
- **Traceability**: Link each argument to specific paragraphs in source literature
- **Interactive Thesis**: Turn the thesis into an interactive web version

---

## 🤝 Contributing

- Found a problem? [Open an Issue](../../issues)
- Have ideas? Fork and submit a PR
- Find it useful? Give it a ⭐

---

## 📜 License

MIT
