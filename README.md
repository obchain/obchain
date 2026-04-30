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
<summary><strong>🟣 MahaXYZ</strong>: Core contributor · stablecoin mechanics, governance, cross-chain expansion · <em>15 PRs</em></summary>

<br>

**[mahaxyz/contracts](https://github.com/mahaxyz/contracts)** &nbsp;·&nbsp; ⭐ 37 · 8 forks &nbsp;·&nbsp; EVM core protocol

| # | Title | Status |
|---|-------|--------|
| [#72](https://github.com/mahaxyz/contracts/pull/72) | Unstake & Withdraw Feat on OmnichainStaking Token contract on Base | `open` |
| [#71](https://github.com/mahaxyz/contracts/pull/71) | Deployment for MahaUIHelper  | `open` |
| [#70](https://github.com/mahaxyz/contracts/pull/70) | Work on a 4626 vault for MAHA that takes USDC as Collateral | `open` |
| [#59](https://github.com/mahaxyz/contracts/pull/59) | Deployment of MigratorContract &  BuyBackBurn Maha on Base Chain  | `open` |
| [#54](https://github.com/mahaxyz/contracts/pull/54) | Implement User Migration with Merkle Tree and Bonus System for MAHA Locker | `open` |
| [#49](https://github.com/mahaxyz/contracts/pull/49) | Add support for multiple token types in ZapAerodromePoolUSDC contract using Odos API for swaps Fixes | `open` |
| [#48](https://github.com/mahaxyz/contracts/pull/48) | WIP: MAHA Protocol Revenue Collector Contract for USDe to USDC Conversion, Buyback & Burn, and Distribution to sUSDz Stakers | `open` |
| [#47](https://github.com/mahaxyz/contracts/pull/47) | Add MahaUIHelper Contract for User Staking and Locking Info | `open` |
| [#46](https://github.com/mahaxyz/contracts/pull/46) | Add support for multiple token types in ZapAerodromePoolUSDC contract using Odos API for swaps | `merged` |
| [#45](https://github.com/mahaxyz/contracts/pull/45) | WIP: MAHA Protocol Revenue Collector Contract for USDe to USDC Conversion, Buyback & Burn, and Distribution to sUSDz Stakers | `merged` |
| [#44](https://github.com/mahaxyz/contracts/pull/44) | Add PSM Contract with ERC4626 Support and Yield Collection Functionality | `merged` |
| [#43](https://github.com/mahaxyz/contracts/pull/43) | Modify ZapAerodromePoolUSDC to Accept Any Token as Input via Odos | `merged` |
| [#42](https://github.com/mahaxyz/contracts/pull/42) | Deployment Script for LockerToken and OmnichainStaking Contracts | `merged` |

**[mahaxyz/solana-contracts](https://github.com/mahaxyz/solana-contracts)** &nbsp;·&nbsp; 2 forks &nbsp;·&nbsp; Anchor / Rust

| # | Title | Status |
|---|-------|--------|
| [#1](https://github.com/mahaxyz/solana-contracts/pull/1) | Solana Launchpad Contracts | `merged` |

**[mahaxyz/timelocks](https://github.com/mahaxyz/timelocks)** &nbsp;·&nbsp; 1 fork &nbsp;·&nbsp; Multi-chain timelock infrastructure

| # | Title | Status |
|---|-------|--------|
| [#1](https://github.com/mahaxyz/timelocks/pull/1) | Added Timelock script for the Unstake & Withdraw OmnichainStaking Token on Base | `open` |

</details>

<details>
<summary><strong>🟢 ZeroLend</strong>: Lending protocol · core, governance, oracles, timelocks · <em>9 PRs</em></summary>

<br>

**[zerolend/core-contracts-v1](https://github.com/zerolend/core-contracts-v1)** &nbsp;·&nbsp; ⭐ 3 · 6 forks

| # | Title | Status |
|---|-------|--------|
| [#9](https://github.com/zerolend/core-contracts-v1/pull/9) | Hexagate Gator Pool  | `open` |
| [#8](https://github.com/zerolend/core-contracts-v1/pull/8) | Pool Hypernative Firewall on Base. | `open` |
| [#7](https://github.com/zerolend/core-contracts-v1/pull/7) | Zerolend Core Contract Liquid E-Mode | `open` |
| [#6](https://github.com/zerolend/core-contracts-v1/pull/6) | Implement Safety Pool with Aave-style Umbrella Module Functionality | `open` |
| [#5](https://github.com/zerolend/core-contracts-v1/pull/5) | Integrate Venn Protocol into ZeroLend Core Contracts | `open` |

**[zerolend/governance](https://github.com/zerolend/governance)** &nbsp;·&nbsp; ⭐ 15 · 13 forks

| # | Title | Status |
|---|-------|--------|
| [#54](https://github.com/zerolend/governance/pull/54) | Integrate veGovernance Voting Power with Omnichain Staking Contracts | `open` |
| [#52](https://github.com/zerolend/governance/pull/52) | Update Airdrop Vesting Schedule to 6-Month Cliff with 1-Month Linear Vesting | `open` |

**[zerolend/oracles](https://github.com/zerolend/oracles)** &nbsp;·&nbsp; 4 forks

| # | Title | Status |
|---|-------|--------|
| [#5](https://github.com/zerolend/oracles/pull/5) | Added DIA Aggregator Oracle Contract superOETH-USD on Base | `open` |

**[zerolend/timelocks](https://github.com/zerolend/timelocks)** &nbsp;·&nbsp; 3 forks

| # | Title | Status |
|---|-------|--------|
| [#1](https://github.com/zerolend/timelocks/pull/1) | Timelock script  Pool Implementation Upgrade on Base | `open` |

</details>

<details>
<summary><strong>🟡 TinyHumansAI · OpenHuman</strong>: Personal AI assistant: cron, planner, weekly review, install · <em>5 PRs</em></summary>

<br>

**[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)** &nbsp;·&nbsp; ⭐ 259 · 39 forks

| # | Title | Status |
|---|-------|--------|
| [#1026](https://github.com/tinyhumansai/openhuman/pull/1026) | fix(cron): route reminders from origin channel, gate announce by allowed_users | `merged` |
| [#959](https://github.com/tinyhumansai/openhuman/pull/959) | feat(morning_briefing): inject ambient runtime + user + datetime into system prompt | `merged` |
| [#914](https://github.com/tinyhumansai/openhuman/pull/914) | ci(weekly-review): aggregator + workflow + runbook for #459 | `merged` |
| [#904](https://github.com/tinyhumansai/openhuman/pull/904) | feat(planner): read-only sandbox gate on composio meta-tools | `merged` |
| [#877](https://github.com/tinyhumansai/openhuman/pull/877) | fix(install.sh): dry-run exits 0 when platform asset missing | `merged` |

</details>

<details>
<summary><strong>🔵 Digital Asset · DAML</strong>: stdlib docs + `damlc` build inference (official DAML smart contract language) · <em>3 PRs</em></summary>

<br>

**[digital-asset/daml](https://github.com/digital-asset/daml)** &nbsp;·&nbsp; ⭐ 888 · 255 forks &nbsp;·&nbsp; Official DAML smart contract language

| # | Title | Status |
|---|-------|--------|
| [#22955](https://github.com/digital-asset/daml/pull/22955) | docs(stdlib): fix `Template` constraint claim on internal typeclasses | `open` |
| [#22953](https://github.com/digital-asset/daml/pull/22953) | docs(stdlib): clarify DA.List.group groups consecutive elements | `open` |
| [#22943](https://github.com/digital-asset/daml/pull/22943) | feat(damlc): infer --all for daml build with only multi-package.yaml | `open` |

</details>

<details>
<summary><strong>🟠 MahaDAO</strong>: DAO governance contracts · <em>1 PR</em></summary>

<br>

**[MahaDAO/governance-contracts](https://github.com/MahaDAO/governance-contracts)** &nbsp;·&nbsp; 2 forks

| # | Title | Status |
|---|-------|--------|
| [#30](https://github.com/MahaDAO/governance-contracts/pull/30) | Implement Merkle Tree Creation for MAHAX Locker Migration and Bonus MAHA Distribution | `open` |

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
