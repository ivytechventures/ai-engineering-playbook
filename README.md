# AI Engineer Playbook

A living, self-contained knowledge base for my personal transition from software/QA engineering into AI engineering, covering the algorithms and systems fundamentals, the modern GenAI stack, and how to actually test and evaluate AI systems once they're built.

This isn't a course I'm following top to bottom. It's a working repository: each topic gets filled in as I study it, build against it, or hit it in the wild, and it stays self-contained so any single doc is useful on its own without needing the rest of the repo as context.

## Why this exists

Two things prompted this:

1. **Bridging QA and AI engineering.** 15 years in software engineering and QA gives a strong foundation in testing rigor, but "testing an AI system" is a different discipline than testing deterministic software — non-deterministic outputs, evaluation frameworks, drift, hallucinations, and adversarial inputs all need their own mental models. This repo is where that bridge gets built, deliberately, topic by topic.
2. **Documenting the climb, not just the destination.** A lot of AI engineering knowledge is scattered across papers, docs, tweets, and half-remembered conference talks. Writing it down in one consistent format — Overview, Why it exists, Core Concepts, Architecture, Analogy, Example, Real-world Use Cases, QA Perspective, My Implementation, Common Interview Questions, References — forces actual understanding instead of passive consumption, and leaves something reusable for interview prep, project work, or teaching someone else later.

## How this repo is organized

| Folder                    | Purpose                                           |
| ------------------------- | -------------------------------------------------- |
| **README.md**             | Introduction to the repository and current focus  |
| **learning-roadmap.md**   | Study plan and progress tracker                   |
| **glossary.md**           | Personal AI/software engineering dictionary       |
| **journal.md**            | Daily learning log and reflections                |
| **algorithms/**           | LeetCode, DSA, interview patterns                 |
| **software-engineering/** | Core backend and systems knowledge                |
| **machine-learning/**     | Traditional ML concepts and production ML         |
| **ai-engineering/**       | Modern GenAI stack (LLMs, MCP, RAG, Agents, etc.) |
| **ai-testing/**           | Evaluating and testing AI systems                 |
| **research/**             | Papers, notes, experiments                        |
| **projects/**             | Real implementations                              |
| **interview/**            | Company-specific preparation                      |
| **resources/**            | External references worth revisiting              |
| **assets/**               | Images, diagrams, architecture drawings           |

## Documentation Templates

The playbook uses different documentation templates depending on the type of content. This keeps explanations consistent while allowing each topic to be presented in the most effective way.

### Concept Template

Used for topics in:

- `software-engineering/`
- `machine-learning/`
- `ai-engineering/`
- `ai-testing/`

Each concept document generally follows this structure:

- Overview
- Why It Exists
- Core Concepts
- Architecture
- Analogy
- Example
- Real-world Use Cases
- Practical Notes
- Common Interview Questions
- References

---

### Algorithm Template

Used for problems in:

- `algorithms/`

Each algorithm document generally follows this structure:

- Understand the Problem
  - Restate
  - Assumptions
  - Input
  - Output
- Looking For
- Remember (State)
- Move
- Check / Update
- Initialization
- Brute Force
- Key Insight
- Algorithm
- Dry Run *(optional)*
- Solution
- Complexity
- Common Mistakes
- Pattern Recognition
- Related Problems
- Interview Tips

---

These templates are guidelines rather than strict rules. Some topics may omit or expand sections where appropriate, but the overall structure should remain consistent to make the playbook easy to navigate and learn from.

## Current focus

See `learning-roadmap.md` for the active study plan and progress tracker. Day-to-day notes and reflections live in `journal.md`.