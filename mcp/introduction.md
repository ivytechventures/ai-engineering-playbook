# Model Context Protocol (MCP)

## Overview

MCP (Model Context Protocol) is an open standard, introduced by Anthropic in November 2024, for connecting AI models to external tools, data sources, and systems. Before MCP, every AI application that wanted to talk to Gmail, Slack, a database, or a file system had to write a custom integration for that specific pairing of model and tool. MCP replaces that N×M integration problem with a single protocol: any MCP-compatible client (a "host" like Claude Desktop, an IDE, or a custom agent) can talk to any MCP-compatible server (Gmail, Postgres, GitHub, a proprietary internal API) without bespoke glue code.

At its core, MCP is a client-server protocol built on JSON-RPC 2.0. It defines how a host application discovers what a server can do, and how it invokes those capabilities in a structured, model-friendly way.

## Why it exists

Two failures motivated MCP:

1. **The integration explosion.** If you have M models/agents and N tools, naive integration requires building and maintaining M×N connectors. Every new tool means updating every agent framework that wants to use it, and vice versa. This is the same problem USB solved for peripherals, or LSP (Language Server Protocol) solved for editors and language tooling — MCP is explicitly modeled on LSP's success.

2. **Context is the bottleneck, not intelligence.** As models got better at reasoning, the limiting factor for real usefulness became: does the model actually know what's happening in this codebase, this ticketing system, this customer record? Prompt-stuffing (copy-pasting data into the context window) doesn't scale and goes stale immediately. Models needed a standard way to *reach out* and pull live, structured context — and to *act* on the world — rather than only working from what a human pasted in.

MCP exists to make "connect my AI to my stuff" a solved, boring problem instead of a bespoke integration project every time.

## Core Concepts

- **Host** — the AI application the user interacts with (Claude Desktop, Claude.ai, an IDE, a custom agent). The host embeds an MCP client.
- **Client** — lives inside the host, maintains a 1:1 stateful connection to a single MCP server, and handles the protocol-level negotiation.
- **Server** — a lightweight process that exposes capabilities to clients. A server can be local (spawned as a subprocess, talking over stdio) or remote (a hosted service, talking over HTTP).
- **Tools** — model-callable functions with a defined input schema. This is the "let the model *do* something" primitive (send an email, run a query, create a ticket). Tools are model-controlled: the LLM decides when to invoke them based on the conversation.
- **Resources** — read-only, addressable data the host can attach to context (a file, a database row, a webpage). Resources are typically application-controlled: the host or user decides when to pull them in, not the model autonomously.
- **Prompts** — reusable, parameterized prompt templates a server exposes, so common workflows ("summarize this ticket," "review this PR") don't have to be reinvented per client. These are user-controlled — usually surfaced as slash commands or menu options.
- **Sampling** — a more advanced capability that lets a server ask the *client's* LLM to generate a completion, effectively borrowing the host's model instead of running its own. Used sparingly, mostly for agentic servers that need their own reasoning step.
- **Capability negotiation** — on connection, client and server exchange what they each support, so both sides only use features the other understands.

## Architecture

![MCP Architecture](/img/mcparchitecture.png)

Key architectural facts:
- The relationship is always **1 client : 1 server**. A host that talks to five servers runs five clients internally — there's no fan-out multiplexing at the client layer.
- Transport is pluggable: **stdio** for local servers (simplest, no auth needed, process lives and dies with the host), or **Streamable HTTP** for remote servers (needs auth, typically OAuth 2.1, and supports multiple concurrent client connections).
- Message format is **JSON-RPC 2.0** throughout — requests, responses, and notifications, all with the same envelope regardless of transport.
- Servers are intentionally "dumb and honest": they declare a schema for each tool/resource, and it's the client/host's job to decide what the model sees and when.

## Analogy

MCP is a USB-C port for AI applications. Before USB-C (and USB generally), every peripheral needed its own proprietary port and cable — your printer, your mouse, your external drive, all different connectors, all requiring different drivers. USB standardized the *plug*, so any USB peripheral works with any USB host, and manufacturers only had to build to one spec instead of one spec per device they wanted to support.

MCP does the same thing for models and tools: build your tool as an MCP server once, and it works with Claude, or any other MCP-compatible host, without custom wiring. Build your agent as an MCP host once, and it can plug into any MCP server — Slack, GitHub, a vector DB, your own internal system — without custom wiring on that side either.

## Example

A minimal MCP server exposing one tool, in Python using the official SDK:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
def get_forecast(city: str) -> str:
    """Get the weather forecast for a given city."""
    # in reality, call a weather API here
    return f"Sunny and 75°F in {city}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

A host (like Claude Desktop) configured to spawn this server would, on startup, ask it "what tools do you have?" — the server responds with the `get_forecast` schema — and from then on, if a user asks "what's the weather in Little Rock," the model can decide to call `get_forecast(city="Little Rock")` and get a real answer back instead of guessing.

## Real-world Use Cases

- **IDE agents** — Claude Code, Cursor, and similar tools use MCP servers to give the model access to git, the filesystem, and language servers without hardcoding those integrations into the agent itself.
- **Enterprise data access** — companies expose internal databases, CRMs, or ticketing systems (Salesforce, Jira, internal APIs) as MCP servers so any approved AI client in the org can query them consistently, with a single place to enforce auth and permissions.
- **Personal productivity** — connecting Gmail, Google Calendar, and Google Drive to Claude.ai so it can read and act on a user's own data during a conversation, as opposed to the user manually copy-pasting content in.
- **Chat agents** — an MCP server can wrap a scheduling system or CRM so a chat agent's LLM layer can look up or create appointments mid-conversation instead of just talking.
- **Dev tooling and CI** — servers wrapping test runners, deployment pipelines, or observability dashboards, so an agent can be asked to "check why the build failed" and actually go look.

## QA Perspective

MCP introduces a new integration boundary, and boundaries are exactly where QA earns its keep. A QA engineer coming to MCP for the first time can think of a server as an API with an unusual client: the caller isn't a human hitting "submit," it's a language model deciding, based on a natural-language description, whether and how to invoke a function. That shifts what "correct" means and adds failure modes that don't exist in traditional API testing.

**What's the same as testing any API:**
- Schema validation — does the tool's declared input schema match what the implementation actually accepts and returns?
- Contract testing — if the server changes a tool's parameters, does anything consuming it break silently?
- Error handling — malformed input, timeouts, rate limits, auth failures should all fail predictably, not hang or return ambiguous output.
- Idempotency and side-effect testing — especially important here, since a model may retry a tool call it thinks failed.

**What's different, and specific to MCP/LLM-driven systems:**
- **Description quality is a testable artifact.** A tool's name and docstring aren't just documentation — they're the only signal the model uses to decide whether to call the tool and how to fill its parameters. A vague or ambiguous description is a bug, not a style issue. Test that the model reliably picks the right tool given realistic user phrasing, not just that the tool works when called directly.
- **Non-deterministic invocation.** The same user request can lead the model to call a tool, skip it, or call the wrong one, because tool selection is a model decision, not a fixed code path. This means test suites need to check for *behavioral* correctness across many phrasings/seeds, not a single pass/fail run — closer to eval-style testing than classic unit testing.
- **Prompt injection via tool output.** If a tool returns untrusted content (an email body, a webpage, a database text field), that content re-enters the model's context and can attempt to manipulate subsequent behavior. QA should explicitly test tool responses containing adversarial text, not just "valid" data.
- **Permission and scope testing.** Since tools are model-invoked, a QA pass should include negative testing: can the model be talked into calling a tool it shouldn't (data exfiltration, destructive actions) via a cleverly worded user prompt? This is closer to security testing than functional testing, and it's a real gap area per current MCP security writeups (see References).
- **Resources vs. tools vs. prompts need different test strategies**, because they're controlled by different actors: tools are model-triggered (test for correct/incorrect invocation), resources are app-triggered (test that the host attaches the right data at the right time), prompts are user-triggered (test the template renders correctly across parameter variations).
- **Capability negotiation regressions.** If a server adds/removes a tool or changes its schema, a host that cached the old capability list can silently misbehave. Worth testing the reconnect/re-negotiation path explicitly, not just first-connection behavior.
- **Observability is part of the test surface.** Since failures can be "the model didn't call the tool it should have" rather than a thrown exception, logging/tracing of tool-call decisions (what was offered, what was chosen, why) matters for debugging in a way it doesn't in typical API testing — test that this observability actually exists and is usable, not just that the happy path works.

The short version for a QA reader: functional correctness of the server is necessary but not sufficient. The interesting bugs live in the gap between "the tool works" and "the model uses the tool correctly and safely," and that gap is where MCP-specific QA work actually lives.

## My Implementation

*(placeholder — fill in as you build against `projects/mcp-playground/`. Good things to capture here once you have them: which transport you chose and why, what tools/resources you exposed, any auth headaches, and what broke first when you actually pointed a real model at it.)*

## Common Interview Questions

- What problem does MCP solve that direct API integration doesn't?
- Walk through the MCP handshake: what happens between a client and server on connection?
- What's the difference between a tool, a resource, and a prompt in MCP terms — and who decides when each is used (model vs. application vs. user)?
- When would you choose stdio vs. HTTP transport for a server you're building?
- How does MCP handle authentication for remote servers?
- What is "sampling" in MCP, and why would a server want to use the client's model instead of calling its own?
- How is MCP different from function calling / tool use as implemented directly in a model API (e.g., the Anthropic Messages API `tools` parameter)?
- What are the security implications of connecting an LLM host to an MCP server with write access to production systems? How would you scope permissions?
- How would you test an MCP server in isolation, without a full host application?

## References

- Official MCP specification and docs: https://modelcontextprotocol.io
- Anthropic's announcement of MCP (Nov 2024): https://www.anthropic.com/news/model-context-protocol
- MCP GitHub organization: https://github.com/modelcontextprotocol
- Comparison reference point: Language Server Protocol (LSP), the design MCP explicitly borrows from

**Videos**
- Anthropic — official MCP introduction (short, from launch): https://www.youtube.com/watch?v=2B7_Y-6KBSQ
- Anthropic — "The Model Context Protocol" panel with Alex Albert, Theo Chu, and David Soria Parra (MCP co-creator); covers design rationale, launch story, ecosystem growth: https://www.youtube.com/watch?v=CQywdSdi5iA
- Anthropic — "Building Agents with Model Context Protocol," full workshop with Mahesh Murag; most hands-on of the group, builds a server live: https://www.youtube.com/watch?v=kQmXtrmQ5Zg
- Third-party — "MCP In 26 Minutes," fast non-Anthropic overview if you want an outside framing: https://www.youtube.com/watch?v=kOhLoixrJXo