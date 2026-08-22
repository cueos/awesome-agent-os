# Awesome Agent OS [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> What an agent needs to live and work on its own.

An agent that answers questions needs a model. An agent that *works* needs
more than that, and the pieces are scattered across projects that do not think
of themselves as related: something to run the loop, a computer to run it on,
memory that survives the session, skills that reach past the chat window, a way
to reach the person it works for, an identity of its own, and — increasingly —
a way to pay for what it uses.

This list is organised by those needs rather than by product category, because
the need is the part that stays true while the tools churn.

**Every entry is checked.** A weekly job re-reads each repository through the
GitHub API and fails the build on anything gone, archived, or unpushed for a
year. Star counts are refreshed by the same job, so they are approximately
right rather than a snapshot of the day someone added the line.

## Contents

- [Runtimes](#runtimes) — the loop that thinks and acts
- [A computer of its own](#a-computer-of-its-own) — sandboxes, machines, computer use
- [Memory](#memory) — what survives the session
- [Skills and tools](#skills-and-tools) — what it can actually do
- [Reach](#reach) — how it reaches a person
- [Identity and presence](#identity-and-presence) — an account of its own
- [Money](#money) — paying and being paid
- [Protocols](#protocols) — how the pieces talk to each other
- [Watching the work](#watching-the-work) — observability and evals
- [Contributing](#contributing)

---

## Runtimes

*The loop that thinks and acts. Everything else on this list is something a
runtime reaches for.*

- **[openclaw](https://github.com/openclaw/openclaw)** — Always-on personal agent you message from any device; runs tools and chores on your own machines. `⭐ 387k`
- **[hermes-agent](https://github.com/NousResearch/hermes-agent)** — A long-running personal agent that accumulates memory and skills instead of resetting every conversation. `⭐ 234k`
- **[opencode](https://github.com/anomalyco/opencode)** — Terminal coding agent that reads, edits, and runs your codebase with whichever model you point at it. `⭐ 200k`
- **[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)** — The original goal-to-task autonomous loop, now a platform for building and running continuous agents. `⭐ 186k`
- **[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)** — Plugin-shaped agent runtime; every capability, tool, and model swap is an installable piece. `⭐ 184k`
- **[gemini-cli](https://github.com/google-gemini/gemini-cli)** — Terminal agent from Google: chat, file edits, shell commands, and tool calls driven by Gemini models. `⭐ 106k`
- **[pi](https://github.com/earendil-works/pi)** — Agent toolkit and coding CLI: a reusable loop, a unified model API, and a terminal interface. `⭐ 95.5k`
- **[OpenHands](https://github.com/OpenHands/OpenHands)** — Sandboxed software-engineering agent that browses, writes code, and runs commands to close real issues. `⭐ 84.8k`
- **[deer-flow](https://github.com/bytedance/deer-flow)** — Long-horizon agent harness with sandboxes, memory, subagents, and skills for tasks lasting hours. `⭐ 80.6k`
- **[cline](https://github.com/cline/cline)** — Autonomous coding agent you can embed as an SDK, an editor extension, or a CLI. `⭐ 66.7k`
- **[crewAI](https://github.com/crewAIInc/crewAI)** — Assign roles to several agents and let them hand work between each other toward one goal. `⭐ 57.5k`
- **[goose](https://github.com/aaif-goose/goose)** — Extensible local agent that installs, runs, edits, and tests on your machine with any model. `⭐ 53.3k`
- **[aider](https://github.com/Aider-AI/aider)** — Pairs with you in the terminal, editing files and committing to git as it works. `⭐ 48.4k`
- **[nanobot](https://github.com/HKUDS/nanobot)** — Lightweight self-hosted personal agent with a web UI, memory, MCP tools, and chat-app connections. `⭐ 47.3k`
- **[CowAgent](https://github.com/zhayujie/CowAgent)** — Self-evolving assistant that plans tasks and runs skills, reachable across many chat channels. `⭐ 46.6k`
- **[agno](https://github.com/agno-agi/agno)** — Framework for agents with memory, knowledge, and tools that ships them as a running service. `⭐ 41.8k`
- **[langgraph](https://github.com/langchain-ai/langgraph)** — Graph-based runtime for agent loops that need branching, checkpoints, and recovery after failure. `⭐ 40.2k`
- **[smolagents](https://github.com/huggingface/smolagents)** — Small library for agents that write Python to call tools instead of emitting JSON tool calls. `⭐ 28.9k`
- **[openai-agents-python](https://github.com/openai/openai-agents-python)** — Minimal primitives — agents, handoffs, guardrails — for multi-agent work without a heavy framework. `⭐ 28.9k`
- **[intentkit](https://github.com/crestalnetwork/intentkit)** — Self-hosted server that runs and schedules a team of agents with shared skills. `⭐ 6.5k`

## A computer of its own

*An agent that can only emit text is a chat box. These give it somewhere to run
commands, open a browser, and keep a filesystem.*

- **[browser-use](https://github.com/browser-use/browser-use)** — Drives a real browser for an agent: clicks, types, and reads pages from plain instructions. `⭐ 110k`
- **[Daytona](https://github.com/daytonaio/daytona)** — Spins up isolated cloud environments where an agent runs generated code without touching your machine. `⭐ 71.9k`
- **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** — Exposes a real Chrome and its DevTools to an agent for navigating, debugging, and measuring pages. `⭐ 49.6k`
- **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** — Desktop stack letting a vision model see the screen and operate apps with mouse and keyboard. `⭐ 38.7k`
- **[Firecracker](https://github.com/firecracker-microvm/firecracker)** — The microVM most sandbox vendors build on: boots a locked-down virtual machine in milliseconds. `⭐ 36.2k`
- **[Lightpanda](https://github.com/lightpanda-io/browser)** — Headless browser built for machines rather than people, so constant agent browsing stays cheap. `⭐ 34.2k`
- **[Stagehand](https://github.com/browserbase/stagehand)** — Browser SDK mixing written code with natural-language steps, so an agent reasons when selectors break. `⭐ 24.0k`
- **[Skyvern](https://github.com/Skyvern-AI/skyvern)** — Runs multi-step browser workflows like logins and form filling that would otherwise need brittle scripts. `⭐ 22.8k`
- **[cua](https://github.com/trycua/cua)** — Gives an agent full macOS, Linux, and Windows machines to drive, plus benchmarks for grading it. `⭐ 21.8k`
- **[gVisor](https://github.com/google/gvisor)** — Kernel written in userspace that contains untrusted code; the isolation layer under many agent sandboxes. `⭐ 19.1k`
- **[OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** — Sandbox runtime built for agent workloads: start a container, run code, keep the session alive. `⭐ 14.6k`
- **[Coder](https://github.com/coder/coder)** — Self-hosted remote workspaces on your own infrastructure that both developers and their agents work inside. `⭐ 14.2k`
- **[E2B](https://github.com/e2b-dev/E2B)** — Hosted sandboxes an agent calls over an SDK to run code and keep files between steps. `⭐ 13.5k`
- **[Agent-S](https://github.com/simular-ai/Agent-S)** — Research framework where an agent plans, looks at the screen, and operates a computer like a person. `⭐ 12.2k`
- **[microsandbox](https://github.com/superradcompany/microsandbox)** — Local-first microVM runtime, so untrusted agent code runs on your laptop with real hardware isolation. `⭐ 7.9k`
- **[Steel Browser](https://github.com/steel-dev/steel-browser)** — Browser-as-an-API with sessions, proxies, and captcha handling so you never run browser infrastructure. `⭐ 7.5k`
- **[agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox)** — Kubernetes primitives for giving each agent its own stateful, isolated sandbox on a cluster. `⭐ 3.6k`

## Memory

*The difference between an assistant you re-brief every morning and one that
knows you. Storage is the easy half; deciding what is worth keeping is the
other one.*

- **[mem0](https://github.com/mem0ai/mem0)** — Stores what a user said and surfaces it back later; the most-used memory layer for agents. `⭐ 63.8k`
- **[MemPalace](https://github.com/MemPalace/mempalace)** — Benchmark-led memory system that decides what is worth keeping and returns it on the next session. `⭐ 58.6k`
- **[Graphiti](https://github.com/getzep/graphiti)** — Builds a knowledge graph tracking when facts were true, so an agent can reason over changes. `⭐ 30.2k`
- **[cognee](https://github.com/topoteretes/cognee)** — Turns documents and conversations into a queryable graph an agent searches instead of re-reading raw text. `⭐ 30.2k`
- **[agentmemory](https://github.com/rohitg00/agentmemory)** — Persistent memory aimed at coding agents, benchmarked on whether recall actually improves the next session. `⭐ 27.3k`
- **[Letta](https://github.com/letta-ai/letta)** — Agent server whose memory lives outside the context window: editable, inspectable, and durable across sessions. `⭐ 24.4k`
- **[memvid](https://github.com/memvid/memvid)** — Packs a whole memory store into one portable file, replacing a retrieval pipeline with something copyable. `⭐ 16.4k`
- **[Memori](https://github.com/MemoriLabs/Memori)** — Records what an agent did and learned and feeds it back, model- and framework-agnostic. `⭐ 16.2k`
- **[EverOS](https://github.com/EverMind-AI/EverOS)** — Portable memory kept as plain Markdown you own, shared across whichever agent tools you use. `⭐ 12.3k`
- **[MemOS](https://github.com/MemTensor/MemOS)** — Treats memory as an operating-system layer with scheduling, retrieval, and reuse across separate tasks. `⭐ 10.9k`
- **[Honcho](https://github.com/plastic-labs/honcho)** — Library for agents that model the person they are talking to and keep that model between sessions. `⭐ 6.8k`
- **[engram](https://github.com/Gentleman-Programming/engram)** — Single Go binary with SQLite giving any coding agent persistent memory over MCP or HTTP. `⭐ 6.1k`
- **[basic-memory](https://github.com/basicmachines-co/basic-memory)** — Keeps the agent's memory as Markdown notes on your disk, so you can read and edit what it knows. `⭐ 3.7k`

## Skills and tools

*What the agent can actually do. The interesting problem has moved from calling
a tool to discovering, packaging, and trusting one.*

- **[superpowers](https://github.com/obra/superpowers)** — Skills framework handing an agent working methods for software development instead of one-off prompts. `⭐ 276k`
- **[anthropics/skills](https://github.com/anthropics/skills)** — The official Agent Skills repository: folders of instructions and scripts an agent loads when relevant. `⭐ 171k`
- **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** — The big directory of MCP servers; the fastest way to find a tool an agent needs. `⭐ 92.7k`
- **[MCP servers](https://github.com/modelcontextprotocol/servers)** — Reference servers for filesystem, fetch, git and more, plus the pattern to copy for your own. `⭐ 89.8k`
- **[agent-skills](https://github.com/addyosmani/agent-skills)** — Engineering skills for coding agents covering testing, review, performance, and other everyday development work. `⭐ 89.1k`
- **[wshobson/agents](https://github.com/wshobson/agents)** — Marketplace of subagents and plugins that works across several different coding harnesses. `⭐ 39.0k`
- **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** — Gives an agent Playwright over MCP, driving pages by accessibility tree rather than screenshots. `⭐ 36.4k`
- **[github-mcp-server](https://github.com/github/github-mcp-server)** — GitHub's own MCP server, so an agent reads issues, opens pull requests, and manages repositories. `⭐ 32.4k`
- **[awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** — Curated pile of a thousand-plus agent skills, sorted by domain and portable across harnesses. `⭐ 30.9k`
- **[Composio](https://github.com/ComposioHQ/composio)** — Authenticated connections to a thousand SaaS tools, plus tool search so the agent's context stays small. `⭐ 29.8k`
- **[agentskills](https://github.com/agentskills/agentskills)** — The Agent Skills specification: how a skill folder is structured so any harness can load it. `⭐ 24.6k`
- **[mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** — MCP server for databases, handling pooling and auth so an agent can query them safely. `⭐ 16.2k`
- **[mcp-use](https://github.com/mcp-use/mcp-use)** — Connects any model to any MCP server in a few lines, without tying you to one vendor's client. `⭐ 10.5k`
- **[Klavis](https://github.com/Klavis-AI/klavis)** — Hosted MCP servers with OAuth handled, so an agent gets authenticated tools without a server to run. `⭐ 5.8k`
- **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** — Gateway in front of many MCP servers and REST APIs, exposing them to agents as one endpoint. `⭐ 4.4k`
- **[mcp-gateway](https://github.com/docker/mcp-gateway)** — Runs MCP servers as containers behind one gateway, so tools are isolated and centrally managed. `⭐ 1.5k`

## Reach

*An agent nobody can hear is an agent nobody uses. These put it in the channels
people already have open.*

- **[novu](https://github.com/novuhq/novu)** — Fan-out layer for agent messages: email, SMS, push, chat, and in-app from one call. `⭐ 39.6k`
- **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** — Runs one agent across many messaging platforms at once, with plugins and per-channel handling. `⭐ 39.5k`
- **[ntfy](https://github.com/binwiederhier/ntfy)** — Send a phone or desktop notification with a plain HTTP request; no account needed. `⭐ 33.7k`
- **[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)** — Mature Python wrapper for the Telegram Bot API, the usual way agents reach people there. `⭐ 29.4k`
- **[discord.js](https://github.com/discordjs/discord.js)** — The standard JavaScript library for putting a bot, and therefore an agent, into Discord. `⭐ 26.8k`
- **[whatsapp-web.js](https://github.com/wwebjs/whatsapp-web.js)** — Drives a real WhatsApp account through the web client, so an agent can message contacts. `⭐ 22.5k`
- **[LangBot](https://github.com/langbot-app/LangBot)** — Builds agent-backed bots for Discord, Slack, Telegram, WeChat, Lark, and more from one config. `⭐ 17.5k`
- **[apprise](https://github.com/caronc/apprise)** — One notification call that fans out to a hundred-odd services without writing per-service code. `⭐ 17.1k`
- **[gotify/server](https://github.com/gotify/server)** — Self-hosted push server with its own Android app, for notifications that never leave your infrastructure. `⭐ 15.8k`
- **[Baileys](https://github.com/WhiskeySockets/Baileys)** — WhatsApp over websockets with no browser, the lighter way for an agent to hold that channel. `⭐ 10.8k`
- **[whatsmeow](https://github.com/tulir/whatsmeow)** — Go library speaking the WhatsApp multi-device protocol directly, used where reliability matters. `⭐ 7.1k`
- **[signal-cli](https://github.com/AsamK/signal-cli)** — Command-line and JSON-RPC access to Signal, letting an agent send and receive encrypted messages. `⭐ 4.9k`
- **[bolt-js](https://github.com/slackapi/bolt-js)** — Slack's own framework for apps that listen in channels and reply, including agent-backed ones. `⭐ 2.9k`
- **[lark-coding-agent-bridge](https://github.com/zarazhangrui/lark-coding-agent-bridge)** — Drives a local coding agent from Feishu or Lark chat, with streaming replies per conversation. `⭐ 2.3k`
- **[mautrix/whatsapp](https://github.com/mautrix/whatsapp)** — Bridges WhatsApp into Matrix, so an agent speaks one protocol and reaches several networks. `⭐ 1.9k`
- **[agentapi](https://github.com/coder/agentapi)** — Puts an HTTP API in front of a terminal coding agent so other software can drive it. `⭐ 1.5k`
- **[bluebubbles-server](https://github.com/BlueBubblesApp/bluebubbles-server)** — Forwards iMessage to and from a Mac over an API, opening the hardest channel. `⭐ 1.1k`

## Identity and presence

*An account of its own, rather than operating yours: somewhere to publish, a
name other agents can find, and a way to prove which agent is speaking.*

- **[Bindu](https://github.com/GetBindu/Bindu)** — Gives an agent a persistent identity, a way to reach other agents, and a payment channel. `⭐ 8.7k`
- **[OASIS](https://github.com/camel-ai/oasis)** — Runs up to a million agents posting, following, and arguing on a simulated social platform. `⭐ 5.0k`
- **[OrgKernel](https://github.com/MetapriseAI/OrgKernel)** — Issues each agent a signing key and scoped token, then hash-chains a record of what it did. `⭐ 2.7k`
- **[MCP Agent Mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** — Gives coding agents named inboxes so they message each other and claim files without colliding. `⭐ 2.1k`
- **[Commonly](https://github.com/Team-Commonly/commonly)** — A shared chat room where each agent joins as a named member with its own memory and workstation. `⭐ 1.3k`
- **[Verified Agent Identity](https://github.com/BillionsNetwork/verified-agent-identity)** — Lets an agent mint a decentralized identifier and prove it owns that identity with a signature. `⭐ 755`
- **[h5i](https://github.com/h5i-dev/h5i)** — Turns a Git repository into a message board where each agent posts from its own sandbox. `⭐ 538`
- **[Registry Broker Skills](https://github.com/hashgraph-online/registry-broker-skills)** — Lets an agent search a cross-protocol directory of other agents, and register itself to be found. `⭐ 402`
- **[ai-sns](https://github.com/ai-sns/ai-sns)** — A social network where agents from different runtimes hold public conversations on a shared map. `⭐ 339`
- **[ERC-8004 Contracts](https://github.com/erc-8004/erc-8004-contracts)** — On-chain registry giving an agent a permanent identifier plus reputation records anyone can read. `⭐ 232`
- **[web-bot-auth](https://github.com/cloudflare/web-bot-auth)** — Lets an agent sign its HTTP requests so a website can tell which bot is calling. `⭐ 148`
- **[Clawstr](https://github.com/clawstr/clawstr)** — A public feed on Nostr where agents post under their own keys with no central server. `⭐ 53`

## Money

*An agent that can buy the thing it needs — a search, a compute hour, another
agent's output — without a human in the loop for every purchase.*

- **[ClawRouter](https://github.com/BlockRunAI/ClawRouter)** — Routes an agent's model calls through one wallet, paying each provider per request in stablecoin. `⭐ 6.6k`
- **[x402](https://github.com/x402-foundation/x402)** — Revives HTTP 402 so an agent pays for an API call and retries with proof of payment. `⭐ 6.5k`
- **[Internet Court](https://github.com/internet-court/internet-court-skill)** — Holds funds in escrow between two trading agents and settles the dispute when delivery goes wrong. `⭐ 4.4k`
- **[AP2](https://github.com/google-agentic-commerce/AP2)** — Spec for mandates proving a human authorized what the agent is about to buy. `⭐ 3.1k`
- **[Solana Pay CLI](https://github.com/solana-foundation/pay)** — One command line for an agent to make and test payments across several competing payment protocols. `⭐ 1.8k`
- **[Agentic Commerce Protocol](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)** — Open checkout standard letting an agent buy from a merchant directly rather than through a browser. `⭐ 1.5k`
- **[AgentKit](https://github.com/coinbase/agentkit)** — Gives an agent a real crypto wallet plus tools to check balances, send, and swap. `⭐ 1.3k`
- **[Helix](https://github.com/usehelix/helix)** — Retries and repairs agent payments that fail mid-flight, so a spend does not silently drop. `⭐ 826`
- **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** — Extension letting one agent charge another for a task and settle inside the A2A conversation. `⭐ 552`
- **[AgentPay SDK](https://github.com/worldliberty/agentpay-sdk)** — Lets an agent hold funds and move money across chains under spending policy and human approval. `⭐ 461`

## Protocols

*How the pieces above talk to each other without each pair inventing its own
handshake.*

- **[FastMCP](https://github.com/PrefectHQ/fastmcp)** — The most-used Python way to write an MCP server or client without hand-rolling the wire format. `⭐ 27.3k`
- **[A2A](https://github.com/a2aproject/A2A)** — Spec for agents built on different stacks to find each other and delegate tasks over HTTP. `⭐ 25.5k`
- **[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)** — Official Python library for exposing tools, resources, and prompts to any MCP-speaking agent. `⭐ 24.1k`
- **[AG-UI](https://github.com/ag-ui-protocol/ag-ui)** — Event stream letting an agent drive a front end — tokens, tool calls, and shared state. `⭐ 15.5k`
- **[MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)** — Official TypeScript library for building MCP servers and clients over stdio or streaming HTTP. `⭐ 13.2k`
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)** — Visual debugger for an MCP server: call its tools by hand and see exactly what it returns. `⭐ 10.7k`
- **[MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol)** — The written standard and schema for how agents connect to tools, data, and prompts. `⭐ 9.0k`
- **[mcp-go](https://github.com/mark3labs/mcp-go)** — Community Go implementation of MCP, widely used for shipping tool servers as single binaries. `⭐ 9.0k`
- **[MCP Registry](https://github.com/modelcontextprotocol/registry)** — Community index an agent can query to discover published MCP servers and where to reach them. `⭐ 7.2k`
- **[Agent Client Protocol](https://github.com/agentclientprotocol/agent-client-protocol)** — Lets any code editor drive any coding agent through one shared request and streaming format. `⭐ 4.0k`
- **[a2a-python](https://github.com/a2aproject/a2a-python)** — Official Python SDK for publishing an agent card and serving or calling A2A tasks. `⭐ 2.1k`
- **[Agent Network Protocol](https://github.com/agent-network-protocol/AgentNetworkProtocol)** — Identity-first spec for agents to discover, describe, and negotiate with each other across the open web. `⭐ 1.4k`
- **[Agent Protocol](https://github.com/langchain-ai/agent-protocol)** — Framework-neutral HTTP API for running an agent, keeping its threads, and storing long-term memory. `⭐ 657`

## Watching the work

*An autonomous agent fails quietly by default. These make the failure loud, and
tell you whether a change made it better or only different.*

- **[Langfuse](https://github.com/langfuse/langfuse)** — Records every model call and tool step of a run, then scores them against saved datasets. `⭐ 33.6k`
- **[promptfoo](https://github.com/promptfoo/promptfoo)** — Declarative test suite for prompts and agents, plus attack generation to probe them in CI. `⭐ 24.5k`
- **[Opik](https://github.com/comet-ml/opik)** — Traces agent runs and grades them with automated judges you can also run in production. `⭐ 21.5k`
- **[openai/evals](https://github.com/openai/evals)** — The long-standing framework and public registry for writing model and agent evaluations. `⭐ 19.2k`
- **[DeepEval](https://github.com/confident-ai/deepeval)** — Writes agent quality checks as unit tests — hallucination, tool choice, task completion. `⭐ 17.8k`
- **[iFixAi](https://github.com/ifixai-ai/iFixAi)** — Audits an agent against what it was supposed to do and returns a score in minutes. `⭐ 11.2k`
- **[Phoenix](https://github.com/Arize-ai/phoenix)** — OpenTelemetry-native tracing UI for agent runs, with evaluation and dataset tools built alongside. `⭐ 11.1k`
- **[garak](https://github.com/NVIDIA/garak)** — Scans a model or agent for jailbreaks, leaks, and injection weaknesses before you ship. `⭐ 8.9k`
- **[OpenLLMetry](https://github.com/traceloop/openllmetry)** — Emits agent and model calls as standard OpenTelemetry spans any existing tracing backend can read. `⭐ 7.4k`
- **[guardrails](https://github.com/guardrails-ai/guardrails)** — Validates and corrects what an agent outputs before it reaches a user or another system. `⭐ 7.3k`
- **[NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)** — Puts programmable rails around an agent so it refuses topics and tool calls you disallow. `⭐ 7.0k`
- **[AgentOps](https://github.com/AgentOps-AI/agentops)** — Drop-in session recorder showing what an agent did, how long it took, and what it cost. `⭐ 5.8k`
- **[SWE-bench](https://github.com/SWE-bench/SWE-bench)** — The standard test of whether a coding agent can close real GitHub issues in real repositories. `⭐ 5.7k`
- **[Harbor](https://github.com/harbor-framework/harbor)** — Runs agents against containerized task suites and reports where they fail. `⭐ 4.5k`
- **[Logfire](https://github.com/pydantic/logfire)** — Tracing for production agents, built on OpenTelemetry with typed queries over spans. `⭐ 4.4k`
- **[Inspect](https://github.com/UKGovernmentBEIS/inspect_ai)** — Harness from the UK AI Safety Institute for writing repeatable agent evaluations with sandboxed tools. `⭐ 2.6k`

---

## Contributing

Pull requests welcome — the bar and the entry format are in
[CONTRIBUTING.md](CONTRIBUTING.md). Removing something that no longer earns its
line is as welcome as adding something that does.

```sh
python3 scripts/check.py            # verify every entry
python3 scripts/check.py --update   # refresh star counts
```

## Who made this list

This list is kept by the people building [Cue OS](https://cueos.ai), which
gives an agent what it needs to live and work — an identity, a computer,
memory, reach, and a wallet. Cue OS is not open source and so is not an entry
here; the sections above exist because we had to solve each of those problems
and went looking for what already existed.

Everything listed is here because it earned the line.

## Licence

[MIT](LICENSE). The list itself is [CC0](https://creativecommons.org/publicdomain/zero/1.0/) —
take it, fork it, argue with it.
