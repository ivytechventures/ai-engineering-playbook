# AI Engineer Playbook

A living, self-contained knowledge base for the transition from software/QA engineering into AI engineering, covering the algorithms and systems fundamentals, the modern GenAI stack, and how to actually test and evaluate AI systems once they're built.

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

## Doc template

Every topic doc in `algorithms/`, `software-engineering/`, `machine-learning/`, `ai-engineering/`, and `ai-testing/` follows the same structure, so any file can be read standalone:

```
Topic
Overview
Why it exists
Core Concepts
Architecture
Analogy
Example
Real-world Use Cases
QA Perspective
My Implementation
Common Interview Questions
References
```

## Current focus

See `learning-roadmap.md` for the active study plan and progress tracker. Day-to-day notes and reflections live in `journal.md`.