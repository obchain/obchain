# Hey, I'm Riteish 🧱

> Full-stack engineer building DeFi protocols, AI agents, and Rust systems.

---

I work across three stacks: smart contracts in Solidity, AI agents and LLM tooling in Python with Claude and MCP, and performance-critical backends in Rust and Go. The systems I ship handle real liquidity, real users, and real money, so I write software that survives adversarial conditions.

On the **DeFi side**, my flagship is **[MantissaFi](https://github.com/obchain/MantissaFi)**, a fully on-chain European options protocol that implements **Black-Scholes-Merton pricing entirely in Solidity**. At **[@mahaxyz](https://github.com/mahaxyz)** I work on the core protocol: stablecoin mechanics, governance, and the Solana expansion. The core [contracts repo](https://github.com/mahaxyz/contracts) has **37+ stars** and active production deployments. I have built AMMs, perpetual DEXs, lending markets influenced by Uniswap V3 concentrated liquidity, and cross-chain governance with **LayerZero** and **Chainlink CCIP**.

On the **AI side**, I design on-chain agent frameworks ([agent-contracts](https://github.com/obchain/agent-contracts)) and contribute to LLM-native developer tooling at **[@tinyhumansai](https://github.com/tinyhumansai)**: planner sandboxes around composio meta-tools, ambient runtime injection into system prompts, and weekly-review aggregation pipelines. I work fluently with Claude and Anthropic SDKs, MCP servers, prompt evaluations, and agent orchestration.

On the **systems side**, I build in Rust. **[Charon](https://github.com/obchain/Charon)** is a multi-chain flash-loan-backed liquidation bot that monitors under-collateralized DeFi positions and atomically liquidates them through Aave, Venus, and PancakeSwap. It uses concurrent scanners, Prometheus metrics, gas-aware profit gating, and EIP-1559 nonce management. I also use Go for backend services and infrastructure tooling.

Currently freelancing on protocol design, smart-contract engineering, AI agent infrastructure, and Rust systems for teams that need security-first execution.

---

## 🔨 What I'm Building

| Project | What it does | Stack |
| :--- | :--- | :--- |
| **[MantissaFi](https://github.com/obchain/MantissaFi)** | Fully on-chain European options with Black-Scholes-Merton pricing in Solidity | Solidity · Foundry |
| **[agent-contracts](https://github.com/obchain/agent-contracts)** | Smart contracts powering an AI Agent Framework | Solidity |
| **[gmx-v2-lens](https://github.com/obchain/gmx-v2-lens)** | Market analytics aggregator for the GMX V2 perpetual DEX | Solidity |
| **[Charon](https://github.com/obchain/Charon)** | Multi-chain flash-loan-backed liquidation bot with atomic Aave, Venus, and PancakeSwap flow | Rust · Foundry |
| **[streamed-cache-rust](https://github.com/obchain/streamed-cache-rust)** | High-performance streaming temperature cache | Rust · Tokio |
| **[ferros-vault](https://github.com/obchain/ferros-vault)** | Institutional-grade tokenized USDC yield vault | Solidity · ERC-4626 |
| **[xyz-bridge](https://github.com/obchain/xyz-bridge)** | Cross-chain bridge with relayer service | Solidity · TypeScript |

---

## 🌐 Protocol Contributions

> Auto-updated from public PR data. See [`.github/workflows/update-readme.yml`](.github/workflows/update-readme.yml).

<!-- PROTOCOL_CONTRIBUTIONS:START -->

<details>
<summary><strong>🟡 TinyHumansAI · OpenHuman</strong>: Personal AI assistant: cron, planner, weekly review, install · <em>33 PRs</em></summary>

<br>

**[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)** &nbsp;·&nbsp; ⭐ 27883 · 2580 forks

| # | Title | Status |
|---|-------|--------|
| [#2444](https://github.com/tinyhumansai/openhuman/pull/2444) | fix(memory/ingestion): bound the job channel + reject submits at cap (#2442) | `merged` |
| [#2302](https://github.com/tinyhumansai/openhuman/pull/2302) | fix(jsonrpc): narrow SessionExpired to backend-boundary signal (#2286) | `closed` |
| [#2289](https://github.com/tinyhumansai/openhuman/pull/2289) | fix(memory-workspace): toast + Reveal Folder fallback for View Vault (#2281) | `merged` |
| [#2181](https://github.com/tinyhumansai/openhuman/pull/2181) | fix(composio): collect Dynamics 365 org name via required-fields registry (#2127) | `merged` |
| [#2179](https://github.com/tinyhumansai/openhuman/pull/2179) | fix(onboarding): raise snapshot timeout + staged still-working UI (#2156) | `merged` |
| [#2101](https://github.com/tinyhumansai/openhuman/pull/2101) | fix(integrations): strip inference path from backend URL (#2075) | `merged` |
| [#2087](https://github.com/tinyhumansai/openhuman/pull/2087) | feat(migration): OpenClaw import surface + unblock unified-core Apply | `merged` |
| [#2056](https://github.com/tinyhumansai/openhuman/pull/2056) | fix(meet): guard orchestrator handoff against transcript prompt injection | `merged` |
| [#1821](https://github.com/tinyhumansai/openhuman/pull/1821) | feat(voice): configurable mascot voice with ElevenLabs picker | `merged` |
| [#1812](https://github.com/tinyhumansai/openhuman/pull/1812) | feat(conversations): dedicated worker-thread UI surface (#1624) | `merged` |
| [#1735](https://github.com/tinyhumansai/openhuman/pull/1735) | fix(composio): default singleEvents + timeZone for googlecalendar list (#1714) | `merged` |
| [#1712](https://github.com/tinyhumansai/openhuman/pull/1712) | fix(providers): user-actionable hint when model_fallbacks unconfigured (#1596) | `merged` |
| [#1708](https://github.com/tinyhumansai/openhuman/pull/1708) | fix(composio): retry once on post-OAuth auth-error gap (#1688) | `merged` |
| [#1636](https://github.com/tinyhumansai/openhuman/pull/1636) | fix(credentials): recover from stale auth-profiles.lock | `merged` |
| [#1536](https://github.com/tinyhumansai/openhuman/pull/1536) | fix(accounts): reset transient webview status on rehydrate | `merged` |
| [#1488](https://github.com/tinyhumansai/openhuman/pull/1488) | feat(orchestrator): collapse per-integration delegation into one tool (#1335) | `merged` |
| [#1483](https://github.com/tinyhumansai/openhuman/pull/1483) | feat(human): toggle voice recording with spacebar (#1471) | `merged` |
| [#1474](https://github.com/tinyhumansai/openhuman/pull/1474) | perf(composio/gmail): cut redundant fetches on incremental sync (#1404) | `merged` |
| [#1473](https://github.com/tinyhumansai/openhuman/pull/1473) | feat(orchestrator): expose update_check + update_apply tools (#1435) | `merged` |
| [#1367](https://github.com/tinyhumansai/openhuman/pull/1367) | fix(agent/triage): tiered cloud → retry → local → defer fallback | `merged` |
| [#1363](https://github.com/tinyhumansai/openhuman/pull/1363) | fix(memory_tree/jobs): scrub credentials from worker error logs | `merged` |
| [#1362](https://github.com/tinyhumansai/openhuman/pull/1362) | test(proxy): drop env-leaking runtime_proxy assertion in clear test | `merged` |
| [#1298](https://github.com/tinyhumansai/openhuman/pull/1298) | fix(stt): rewrite stale-sidecar voice error + e2e registration guard | `merged` |
| [#1209](https://github.com/tinyhumansai/openhuman/pull/1209) | fix(channels): managed-DM credentials surface as connected to chat | `merged` |
| [#1181](https://github.com/tinyhumansai/openhuman/pull/1181) | chore(tauri-shell): retire embedded Gmail webview-account flow | `merged` |
| [#1177](https://github.com/tinyhumansai/openhuman/pull/1177) | feat(learning): privilege explicit user reflections in agent context | `merged` |
| [#1047](https://github.com/tinyhumansai/openhuman/pull/1047) | feat(agent): orchestrator dedicated worker threads via spawn_subagent dedicated_thread flag | `merged` |
| [#1042](https://github.com/tinyhumansai/openhuman/pull/1042) | docs(config): finish #933 — kill BACKEND_URL stragglers + document runtime precedence | `merged` |
| [#1026](https://github.com/tinyhumansai/openhuman/pull/1026) | fix(cron): route reminders from origin channel, gate announce by allowed_users | `merged` |
| [#959](https://github.com/tinyhumansai/openhuman/pull/959) | feat(morning_briefing): inject ambient runtime + user + datetime into system prompt | `merged` |
| [#914](https://github.com/tinyhumansai/openhuman/pull/914) | ci(weekly-review): aggregator + workflow + runbook for #459 | `merged` |
| [#904](https://github.com/tinyhumansai/openhuman/pull/904) | feat(planner): read-only sandbox gate on composio meta-tools | `merged` |
| [#877](https://github.com/tinyhumansai/openhuman/pull/877) | fix(install.sh): dry-run exits 0 when platform asset missing | `merged` |

</details>

<details>
<summary><strong>⚪ NethermindEth</strong> · <em>11 PRs</em></summary>

<br>

**[NethermindEth/nethermind](https://github.com/NethermindEth/nethermind)** &nbsp;·&nbsp; ⭐ 1558 · 701 forks

| # | Title | Status |
|---|-------|--------|
| [#11743](https://github.com/NethermindEth/nethermind/pull/11743) | fix(sync): accept receipts with zero bloom from peers | `merged` |
| [#11742](https://github.com/NethermindEth/nethermind/pull/11742) | test(jsonrpc): fix flaky TransactionReceiptsSubscription tests | `closed` |
| [#11705](https://github.com/NethermindEth/nethermind/pull/11705) | chore(ci): bump remaining actions/create-github-app-token to v3 | `merged` |
| [#11703](https://github.com/NethermindEth/nethermind/pull/11703) | fix(trie): rate-limit "Unable to completely prune persisted nodes" warning | `merged` |
| [#11667](https://github.com/NethermindEth/nethermind/pull/11667) | perf(kute): compile JSON-RPC method filter regex once | `merged` |
| [#11640](https://github.com/NethermindEth/nethermind/pull/11640) | fix(blockchain): defer main-chain events until write batch is flushed | `merged` |
| [#11618](https://github.com/NethermindEth/nethermind/pull/11618) | perf(blockchain): make ChainHeadSpecProvider lock-free | `merged` |
| [#11610](https://github.com/NethermindEth/nethermind/pull/11610) | feat(runner): add --logging-format CLI for structured console logs | `merged` |
| [#11570](https://github.com/NethermindEth/nethermind/pull/11570) | feat(rpc): expose debug_getFirstFullStateBlock (#1999) | `closed` |
| [#11553](https://github.com/NethermindEth/nethermind/pull/11553) | feat(chainspec): support shanghai/cancun/prague/osaka hardfork labels | `merged` |
| [#11523](https://github.com/NethermindEth/nethermind/pull/11523) | feat(config): show non-default values on startup | `merged` |

</details>

<details>
<summary><strong>⚪ domcyrus</strong> · <em>7 PRs</em></summary>

<br>

**[domcyrus/rustnet](https://github.com/domcyrus/rustnet)** &nbsp;·&nbsp; ⭐ 4004 · 176 forks

| # | Title | Status |
|---|-------|--------|
| [#318](https://github.com/domcyrus/rustnet/pull/318) | feat(ui): direct-jump tab shortcuts (1-5) and bracket cycle aliases | `open` |
| [#317](https://github.com/domcyrus/rustnet/pull/317) | refactor(dpi/quic): drop redundant `dcid.clone()` in short-header path | `merged` |
| [#303](https://github.com/domcyrus/rustnet/pull/303) | refactor(dpi/http): drop dead inner `parts.len() >= 3` check | `merged` |
| [#301](https://github.com/domcyrus/rustnet/pull/301) | refactor(dpi/http): case-fold header name without allocating | `merged` |
| [#296](https://github.com/domcyrus/rustnet/pull/296) | refactor(dpi/ssh): collapse dead conditional around `parse_kexinit_algorithms` | `merged` |
| [#294](https://github.com/domcyrus/rustnet/pull/294) | refactor(dpi/mqtt): include UNSUBSCRIBE in flag-validation match | `merged` |
| [#292](https://github.com/domcyrus/rustnet/pull/292) | refactor(link_layer/pktap): drop no-op byte-order conversions | `merged` |

</details>

<details>
<summary><strong>⚪ ag2ai</strong> · <em>6 PRs</em></summary>

<br>

**[ag2ai/ag2](https://github.com/ag2ai/ag2)** &nbsp;·&nbsp; ⭐ 4601 · 641 forks

| # | Title | Status |
|---|-------|--------|
| [#2882](https://github.com/ag2ai/ag2/pull/2882) | fix(claude-review): support forked PRs via pull_request_target + optional PAT | `open` |
| [#2881](https://github.com/ag2ai/ag2/pull/2881) | fix(captainagent): drop top_p from default LLM config to avoid temperature/top_p conflict | `open` |
| [#2880](https://github.com/ag2ai/ag2/pull/2880) | fix(guardrails): strip stray guardrail field when parsing LLM JSON | `open` |
| [#2807](https://github.com/ag2ai/ag2/pull/2807) | fix(fast_depends): keep positional args out of **kwargs when passed by name | `open` |
| [#2806](https://github.com/ag2ai/ag2/pull/2806) | fix(interop/langchain): use arun for async langchain tools | `merged` |
| [#2800](https://github.com/ag2ai/ag2/pull/2800) | fix(beta/policies): pair tool calls/results after history trim | `merged` |

</details>

<details>
<summary><strong>⚪ gitleaks</strong> · <em>6 PRs</em></summary>

<br>

**[gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)** &nbsp;·&nbsp; ⭐ 27287 · 2068 forks

| # | Title | Status |
|---|-------|--------|
| [#2126](https://github.com/gitleaks/gitleaks/pull/2126) | feat(detect): add --log-ignored to surface suppressed findings | `open` |
| [#2125](https://github.com/gitleaks/gitleaks/pull/2125) | fix(rules): allowlist keyboard chord secrets in generic-api-key | `open` |
| [#2116](https://github.com/gitleaks/gitleaks/pull/2116) | chore(gitignore): drop stale config paths | `open` |
| [#2114](https://github.com/gitleaks/gitleaks/pull/2114) | feat(dir): add --source-relative-paths for git/dir fingerprint parity | `open` |
| [#2109](https://github.com/gitleaks/gitleaks/pull/2109) | fix(rules): require sourcegraph context for bare 40-char hex tokens | `open` |
| [#2108](https://github.com/gitleaks/gitleaks/pull/2108) | fix(rules): tighten square-access-token to cut base64 FPs | `open` |

</details>

<details>
<summary><strong>🔵 Digital Asset · DAML</strong>: stdlib docs + `damlc` build inference (official DAML smart contract language) · <em>5 PRs</em></summary>

<br>

**[digital-asset/daml](https://github.com/digital-asset/daml)** &nbsp;·&nbsp; ⭐ 897 · 256 forks &nbsp;·&nbsp; Official DAML smart contract language

| # | Title | Status |
|---|-------|--------|
| [#22989](https://github.com/digital-asset/daml/pull/22989) | docs: document short-circuit evaluation for &&, \|\|, when, unless | `open` |
| [#22963](https://github.com/digital-asset/daml/pull/22963) | docs: document `hiding` and selective import forms | `open` |
| [#22955](https://github.com/digital-asset/daml/pull/22955) | docs(stdlib): fix `Template` constraint claim on internal typeclasses | `closed` |
| [#22953](https://github.com/digital-asset/daml/pull/22953) | docs(stdlib): clarify DA.List.group groups consecutive elements | `open` |
| [#22943](https://github.com/digital-asset/daml/pull/22943) | feat(damlc): infer --all for daml build with only multi-package.yaml | `merged` |

</details>

<details>
<summary><strong>⚪ sentient-agi</strong> · <em>5 PRs</em></summary>

<br>

**[sentient-agi/OpenDeepSearch](https://github.com/sentient-agi/OpenDeepSearch)** &nbsp;·&nbsp; ⭐ 3825 · 340 forks

| # | Title | Status |
|---|-------|--------|
| [#60](https://github.com/sentient-agi/OpenDeepSearch/pull/60) | fix: drop markdown_v2 access in BasicWebScraper.extract | `open` |
| [#58](https://github.com/sentient-agi/OpenDeepSearch/pull/58) | fix: declare wolframalpha as a project dependency | `open` |
| [#55](https://github.com/sentient-agi/OpenDeepSearch/pull/55) | perf: lazy-load fasttext quality model in context_scraping.utils | `open` |
| [#52](https://github.com/sentient-agi/OpenDeepSearch/pull/52) | fix: use crawl4ai result.markdown instead of removed markdown_v2 | `open` |
| [#51](https://github.com/sentient-agi/OpenDeepSearch/pull/51) | fix: replace removed litellm.utils.set_provider_config call | `open` |

</details>

<!-- PROTOCOL_CONTRIBUTIONS:END -->

<details>
<summary><strong>⚡ Energi Core</strong> · EVM L1 · scalability and security infrastructure</summary>

<br>

Worked with the Energi Core EVM chain on scalability and security infrastructure across the protocol.

</details>

---

## 🛠 Stack

**Languages**
![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat&logo=solidity&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000?style=flat&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)

**AI & LLM Tooling**
![Claude](https://img.shields.io/badge/Claude-D97757?style=flat&logo=anthropic&logoColor=white)
![Anthropic SDK](https://img.shields.io/badge/Anthropic_SDK-191919?style=flat)
![MCP](https://img.shields.io/badge/MCP-7C3AED?style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![Composio](https://img.shields.io/badge/Composio-000?style=flat)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white)

**Smart Contracts**
![Foundry](https://img.shields.io/badge/Foundry-1C1C1C?style=flat)
![Hardhat](https://img.shields.io/badge/Hardhat-FFF100?style=flat&logo=hardhat&logoColor=000)
![OpenZeppelin](https://img.shields.io/badge/OpenZeppelin-4E5EE4?style=flat&logo=openzeppelin&logoColor=white)
![Anchor](https://img.shields.io/badge/Anchor-512BD4?style=flat)
![Slither](https://img.shields.io/badge/Slither-000?style=flat)
![Certora](https://img.shields.io/badge/Certora-FF6B35?style=flat)

**Systems & Backend**
![Tokio](https://img.shields.io/badge/Tokio-000?style=flat)
![Axum](https://img.shields.io/badge/Axum-000?style=flat)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)

**Protocols & Infra**
![LayerZero](https://img.shields.io/badge/LayerZero-000?style=flat)
![Chainlink](https://img.shields.io/badge/Chainlink-375BD2?style=flat&logo=chainlink&logoColor=white)
![CCIP](https://img.shields.io/badge/CCIP-375BD2?style=flat)
![GMX](https://img.shields.io/badge/GMX-2D42FC?style=flat)
![Uniswap](https://img.shields.io/badge/Uniswap-FF007A?style=flat&logo=uniswap&logoColor=white)
![Pyth](https://img.shields.io/badge/Pyth-7C3AED?style=flat)
![Tenderly](https://img.shields.io/badge/Tenderly-7B3FE4?style=flat)
![Subgraph](https://img.shields.io/badge/Subgraph-6747ED?style=flat)

**Frontend**
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=000)
![Next.js](https://img.shields.io/badge/Next.js-000?style=flat&logo=nextdotjs&logoColor=white)
![ethers.js](https://img.shields.io/badge/ethers.js-2535A0?style=flat)
![viem](https://img.shields.io/badge/viem-FFC517?style=flat)

**Chains:** Ethereum · Arbitrum · Polygon · BNB · opBNB · Base · Solana

---

## 📬 Let's Connect

[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Riteish29)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:riteishnikhoria@gmail.com)

Open to freelance and contract work on protocol design, smart-contract engineering, and security audits.
