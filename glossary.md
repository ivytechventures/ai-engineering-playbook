# Glossary

A personal AI/software engineering dictionary. Definitions here should be written in plain language — the test for a good entry is "would this make sense to me at 11pm with no other context." Organized by domain, alphabetical within each. Add to this as new terms come up in any other doc rather than letting them go undefined.

---

## Algorithms / DSA

**Big O notation** — shorthand for how an algorithm's time or space requirements grow as input size grows, describing the worst-case growth rate rather than an exact count of operations.

**Greedy algorithm** — an approach that makes the locally best choice at each step without reconsidering it later, trading guaranteed optimality for speed and simplicity; works only when the problem has the right structural properties (e.g. matroid or exchange-argument properties).

**Memoization** — caching the results of expensive function calls, keyed by their inputs, so repeated calls with the same inputs return instantly instead of recomputing.

---

## Software Engineering

**Idempotency** — a property of an operation where performing it multiple times has the same effect as performing it once; critical for safe retries in distributed and event-driven systems.

**Load-bearing** — informal term for a piece of code, config, or infrastructure that many other things quietly depend on, such that removing or changing it breaks things in non-obvious places.

---

## Machine Learning

**Drift** — when the statistical properties of production data (or the relationship between inputs and outputs) change over time relative to what a model was trained on, degrading performance even though the model itself hasn't changed.

**Feature engineering** — the process of transforming raw data into inputs (features) that make it easier for a model to find the relevant patterns.

**Overfitting** — when a model learns the training data too specifically, including its noise, and performs well on it but generalizes poorly to new data.

---

## AI Engineering

**Context window** — the maximum amount of text (measured in tokens) a model can consider at once, spanning both the input prompt and the output it generates.

**Embedding** — a numeric vector representation of text (or other data) positioned in a high-dimensional space such that semantically similar inputs end up close together, enabling similarity search.

**MCP (Model Context Protocol)** — an open standard for connecting AI models to external tools and data sources via a client-server protocol, replacing bespoke per-integration code with a single shared interface. *(see `06-ai-engineering/mcp/introduction.md`)*

**RAG (Retrieval-Augmented Generation)** — a pattern where a model's context is augmented at query time with relevant documents retrieved from an external store (often via embeddings + vector search), rather than relying solely on what was baked in during training.

**Tool calling / function calling** — a model capability where the model can request that a specific function be executed with specific arguments, receive the result, and incorporate it into its response, rather than only generating text.

**Tokenization** — the process of splitting text into the discrete units (tokens) a model actually operates on, which may be whole words, subwords, or characters depending on the tokenizer.

---

## AI Testing

**Benchmark dataset** — a fixed, standardized set of inputs (and often expected outputs) used to measure and compare model or system performance consistently over time.

**Hallucination** — when a model generates output that is fluent and confident but factually incorrect or unsupported by its input/context.

**Prompt regression** — a change in model or prompt behavior, usually caused by a prompt edit or model version change, that causes previously-passing test cases to fail; the LLM-era analog of a code regression.

---
