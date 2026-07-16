# Learning Roadmap

Study plan and progress tracker for the AI Engineer Playbook. This is a living document — reorder, re-prioritize, and check things off as the actual learning path unfolds. It doesn't need to be followed linearly; pull from whichever phase is most relevant to what's being built or interviewed for at the time.

## How to use this file

- `[ ]` not started · `[~]` in progress · `[x]` done (docs filled out to at least Overview/Core Concepts/Example)
- Each item links to its intended file path in the repo.
- Revisit the **Status** section at the bottom periodically rather than trying to keep every checkbox perfectly current in real time.

---

## Phase 1 — Mathematics (01-mathematics/)

Goal: the mathematical foundations underneath both classical ML and modern GenAI. *(subtopics TBD — break this down further once the specific areas to cover are decided, e.g. linear algebra, probability/statistics, calculus.)*

- [ ] `01-mathematics/`

## Phase 2 — Computer Science (02-computer-science/)

Goal: solid enough DSA and interview patterns to not get blocked in interviews or in reading production AI infra code.

- [ ] `02-computer-science/arrays/`
- [ ] `02-computer-science/strings/`
- [ ] `02-computer-science/hash-maps/`
- [ ] `02-computer-science/linked-lists/`
- [ ] `02-computer-science/stacks-queues/`
- [ ] `02-computer-science/trees/`
- [ ] `02-computer-science/graphs/`
- [ ] `02-computer-science/heaps/`
- [ ] `02-computer-science/greedy/`
- [ ] `02-computer-science/dynamic-programming/`
- [ ] `02-computer-science/patterns/` (sliding window, two pointers, binary search variants, etc.)

## Phase 3 — Software Engineering (03-software-engineering/)

Goal: core backend and systems knowledge.

- [ ] `03-software-engineering/architecture/`
- [ ] `03-software-engineering/api-design/`
- [ ] `03-software-engineering/databases/`
- [ ] `03-software-engineering/caching/`
- [ ] `03-software-engineering/distributed-systems/`
- [ ] `03-software-engineering/event-driven/`
- [ ] `03-software-engineering/testing/`
- [ ] `03-software-engineering/security/`
- [ ] `03-software-engineering/ci-cd/`

## Phase 4 — Network Science (04-network-science/)

Goal: TBD — new addition to the path. *(fill in scope once decided, e.g. graph/network theory, distributed networking fundamentals, or social/information network analysis.)*

- [ ] `04-network-science/`

## Phase 5 — Machine Learning (05-machine-learning/)

Goal: enough traditional ML to understand what GenAI is built on top of, and to speak fluently about evaluation, drift, and production concerns — this is also where prior QA instincts transfer most directly.

- [ ] `05-machine-learning/fundamentals/`
- [ ] `05-machine-learning/supervised-learning/`
- [ ] `05-machine-learning/unsupervised-learning/`
- [ ] `05-machine-learning/feature-engineering/`
- [ ] `05-machine-learning/evaluation-metrics/`
- [ ] `05-machine-learning/drift/`
- [ ] `05-machine-learning/monitoring/`
- [ ] `05-machine-learning/experimentation/`
- [ ] `05-machine-learning/production/`

## Phase 6 — AI Engineering (06-ai-engineering/)

Goal: working understanding of the full LLM application stack, from raw model behavior up through agentic systems.

- [x] `06-ai-engineering/mcp/introduction.md`
- [ ] `06-ai-engineering/llms/transformers.md`
- [ ] `06-ai-engineering/llms/tokenization.md`
- [ ] `06-ai-engineering/llms/context-window.md`
- [ ] `06-ai-engineering/llms/inference.md`
- [ ] `06-ai-engineering/llms/prompting.md`
- [ ] `06-ai-engineering/prompt-engineering/`
- [ ] `06-ai-engineering/tool-calling/`
- [ ] `06-ai-engineering/mcp/architecture.md`
- [ ] `06-ai-engineering/mcp/host-client-server.md`
- [ ] `06-ai-engineering/mcp/tools-resources-prompts.md`
- [ ] `06-ai-engineering/mcp/transport.md`
- [ ] `06-ai-engineering/mcp/authentication.md`
- [ ] `06-ai-engineering/mcp/building-a-server.md`
- [ ] `06-ai-engineering/mcp/testing.md`
- [ ] `06-ai-engineering/mcp/debugging.md`
- [ ] `06-ai-engineering/mcp/production.md`
- [ ] `06-ai-engineering/rag/`
- [ ] `06-ai-engineering/embeddings/`
- [ ] `06-ai-engineering/vector-databases/`
- [ ] `06-ai-engineering/ai-agents/`
- [ ] `06-ai-engineering/memory/`
- [ ] `06-ai-engineering/orchestration/`

## Phase 7 — AI Testing (07-ai-testing/)

Goal: this is the specialization — treat it as the payoff phase where the QA background and the AI engineering knowledge from Phase 6 combine.

- [ ] `07-ai-testing/model-behavior/`
- [ ] `07-ai-testing/hallucinations.md`
- [ ] `07-ai-testing/prompt-regression.md`
- [ ] `07-ai-testing/evaluation-frameworks.md`
- [ ] `07-ai-testing/benchmark-datasets.md`
- [ ] `07-ai-testing/automation.md`
- [ ] `07-ai-testing/observability.md`
- [ ] `07-ai-testing/safety.md`
- [ ] `07-ai-testing/case-studies/`

## Phase 8 — System Design (08-system-design/)

Goal: promoted to its own phase (previously nested under Software Engineering). *(subtopics TBD.)*

- [ ] `08-system-design/`

## Phase 9 — Applied and ongoing

These don't follow the phase structure — they run continuously alongside whatever phase is active.

- [ ] `09-research/` — papers, notes, and experiments as they come up, not on a schedule
- [ ] `10-projects/` — applied implementations: Kaggle competitions/notebooks, a personal sandbox system for practicing ML/AI testing techniques (eval harnesses, drift simulation, hallucination detection), and any other applied builds worth documenting
- [ ] `11-interview/` — company-specific prep, pulled from whichever earlier-phase docs are relevant
- [ ] `12-resources/` — books, courses, papers, YouTube, newsletters worth revisiting
- [ ] `assets/` — diagrams, images, cheatsheets supporting the above

---
