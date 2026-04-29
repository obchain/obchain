# Hey, I'm Riteish 🧱

> I build DeFi protocols — on-chain options pricing, perpetual DEXs, and cross-chain governance.

---

I design and ship smart contracts that handle real liquidity on mainnet. My most interesting project is **[MantissaFi](https://github.com/obchain/MantissaFi)** — a fully on-chain European options protocol that implements **Black-Scholes-Merton pricing entirely in Solidity**.

At **[@mahaxyz](https://github.com/mahaxyz)**, I work on the core protocol: stablecoin mechanics, governance, and the Solana expansion. The core [contracts repo](https://github.com/mahaxyz/contracts) has **37+ stars** and active production deployments.

I've built AMMs, perpetual DEXs, lending markets influenced by Uniswap V3 concentrated liquidity, and cross-chain governance with **LayerZero** and **Chainlink CCIP**. I care about contracts that are gas-efficient, fuzz-tested, and built to survive adversarial environments — because in DeFi, production *is* the war zone.

Currently freelancing — building protocol infra, designing derivatives vaults, and shipping smart contracts for teams that need security-first engineering.

---

## 🔨 What I'm Building

| Project | What it does | Stack |
| :--- | :--- | :--- |
| **[MantissaFi](https://github.com/obchain/MantissaFi)** | Fully on-chain European options — Black-Scholes-Merton pricing in Solidity | Solidity · Foundry |
| **[agent-contracts](https://github.com/obchain/agent-contracts)** | Smart contracts powering an AI Agent Framework | Solidity |
| **[gmx-v2-lens](https://github.com/obchain/gmx-v2-lens)** | Market analytics aggregator for the GMX V2 perpetual DEX | Solidity |
| **[Charon](https://github.com/obchain/Charon)** | Multi-chain, flash-loan-backed liquidation bot — atomic Aave + Venus + PancakeSwap flow | Rust · Foundry |
| **[ferros-vault](https://github.com/obchain/ferros-vault)** | Institutional-grade tokenized USDC yield vault | Solidity · ERC-4626 |
| **[CrossChain-Bridge](https://github.com/obchain/CrossChain-Bridge)** | Cross-chain asset bridge experiments | Solidity |

---

## 🌐 Protocol Contributions

<details>
<summary><strong>🟣 MahaXYZ</strong> — Core contributor · stablecoin mechanics, governance, cross-chain expansion · <em>15 PRs</em></summary>

<br>

**[mahaxyz/contracts](https://github.com/mahaxyz/contracts)** &nbsp; ⭐ 37 · 8 forks &nbsp; — &nbsp; EVM core protocol

| # | Title | Status |
|---|-------|--------|
| [#42](https://github.com/mahaxyz/contracts/pull/42) | Deployment Script for LockerToken and OmnichainStaking Contracts | `merged` |
| [#43](https://github.com/mahaxyz/contracts/pull/43) | Modify ZapAerodromePoolUSDC to Accept Any Token via Odos | `merged` |
| [#44](https://github.com/mahaxyz/contracts/pull/44) | Add PSM Contract with ERC4626 Support and Yield Collection | `merged` |
| [#45](https://github.com/mahaxyz/contracts/pull/45) | MAHA Protocol Revenue Collector — USDe→USDC, Buyback & Burn | `merged` |
| [#46](https://github.com/mahaxyz/contracts/pull/46) | Multi-token support in ZapAerodromePoolUSDC via Odos API | `merged` |
| [#47](https://github.com/mahaxyz/contracts/pull/47) | Add MahaUIHelper Contract for User Staking and Locking Info | `open` |
| [#48](https://github.com/mahaxyz/contracts/pull/48) | MAHA Protocol Revenue Collector (WIP iteration) | `open` |
| [#49](https://github.com/mahaxyz/contracts/pull/49) | Multi-token ZapAerodromePoolUSDC fixes | `open` |
| [#54](https://github.com/mahaxyz/contracts/pull/54) | User Migration with Merkle Tree + Bonus System for MAHA Locker | `open` |
| [#59](https://github.com/mahaxyz/contracts/pull/59) | Deployment of MigratorContract & BuyBackBurn MAHA on Base | `open` |
| [#70](https://github.com/mahaxyz/contracts/pull/70) | ERC-4626 vault for MAHA accepting USDC as collateral | `open` |
| [#71](https://github.com/mahaxyz/contracts/pull/71) | Deployment for MahaUIHelper | `open` |
| [#72](https://github.com/mahaxyz/contracts/pull/72) | Unstake & Withdraw on OmnichainStaking Token contract on Base | `open` |

**[mahaxyz/solana-contracts](https://github.com/mahaxyz/solana-contracts)** &nbsp; — &nbsp; Anchor / Rust

| # | Title | Status |
|---|-------|--------|
| [#1](https://github.com/mahaxyz/solana-contracts/pull/1) | Solana Launchpad Contracts | `merged` |

**[mahaxyz/timelocks](https://github.com/mahaxyz/timelocks)** &nbsp; — &nbsp; Multi-chain timelock infrastructure

| # | Title | Status |
|---|-------|--------|
| [#1](https://github.com/mahaxyz/timelocks/pull/1) | Timelock script for Unstake & Withdraw OmnichainStaking on Base | `open` |

</details>

<details>
<summary><strong>🟠 MahaDAO</strong> — DAO governance contracts · <em>1 PR</em></summary>

<br>

**[MahaDAO/governance-contracts](https://github.com/MahaDAO/governance-contracts)**

| # | Title | Status |
|---|-------|--------|
| [#30](https://github.com/MahaDAO/governance-contracts/pull/30) | Merkle Tree Creation for MAHAX Locker Migration + Bonus MAHA Distribution | `open` |

</details>

<details>
<summary><strong>🟢 ZeroLend</strong> — Lending protocol · core, governance, oracles, timelocks · <em>9 PRs</em></summary>

<br>

**[zerolend/core-contracts-v1](https://github.com/zerolend/core-contracts-v1)**

| # | Title | Status |
|---|-------|--------|
| [#5](https://github.com/zerolend/core-contracts-v1/pull/5) | Integrate Venn Protocol into ZeroLend Core Contracts | `open` |
| [#6](https://github.com/zerolend/core-contracts-v1/pull/6) | Safety Pool with Aave-style Umbrella Module Functionality | `open` |
| [#7](https://github.com/zerolend/core-contracts-v1/pull/7) | ZeroLend Core Contract Liquid E-Mode | `open` |
| [#8](https://github.com/zerolend/core-contracts-v1/pull/8) | Pool Hypernative Firewall on Base | `open` |
| [#9](https://github.com/zerolend/core-contracts-v1/pull/9) | Hexagate Gator Pool | `open` |

**[zerolend/governance](https://github.com/zerolend/governance)**

| # | Title | Status |
|---|-------|--------|
| [#52](https://github.com/zerolend/governance/pull/52) | Airdrop Vesting Schedule — 6-month cliff, 1-month linear | `open` |
| [#54](https://github.com/zerolend/governance/pull/54) | Integrate veGovernance Voting Power with Omnichain Staking | `open` |

**[zerolend/oracles](https://github.com/zerolend/oracles)**

| # | Title | Status |
|---|-------|--------|
| [#5](https://github.com/zerolend/oracles/pull/5) | DIA Aggregator Oracle Contract — superOETH-USD on Base | `open` |

**[zerolend/timelocks](https://github.com/zerolend/timelocks)**

| # | Title | Status |
|---|-------|--------|
| [#1](https://github.com/zerolend/timelocks/pull/1) | Timelock script — Pool Implementation Upgrade on Base | `open` |

</details>

<details>
<summary><strong>🔵 Digital Asset · DAML</strong> — stdlib docs + <code>damlc</code> build inference · <em>3 PRs</em></summary>

<br>

**[digital-asset/daml](https://github.com/digital-asset/daml)** — official DAML smart contract language

| # | Title | Status |
|---|-------|--------|
| [#22943](https://github.com/digital-asset/daml/pull/22943) | feat(damlc): infer `--all` for `daml build` with only `multi-package.yaml` | `open` |
| [#22953](https://github.com/digital-asset/daml/pull/22953) | docs(stdlib): clarify `DA.List.group` groups consecutive elements | `open` |
| [#22955](https://github.com/digital-asset/daml/pull/22955) | docs(stdlib): fix `Template` constraint claim on internal typeclasses | `open` |

</details>

<details>
<summary><strong>🟡 TinyHumansAI · OpenHuman</strong> — personal AI assistant: cron, planner, weekly review, install · <em>5 PRs</em></summary>

<br>

**[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)**

| # | Title | Status |
|---|-------|--------|
| [#1026](https://github.com/tinyhumansai/openhuman/pull/1026) | fix(cron): route reminders from origin channel, gate announce by allowed_users | `merged` |
| [#959](https://github.com/tinyhumansai/openhuman/pull/959) | feat(morning_briefing): inject ambient runtime + user + datetime into system prompt | `merged` |
| [#914](https://github.com/tinyhumansai/openhuman/pull/914) | ci(weekly-review): aggregator + workflow + runbook for #459 | `merged` |
| [#904](https://github.com/tinyhumansai/openhuman/pull/904) | feat(planner): read-only sandbox gate on composio meta-tools | `merged` |
| [#877](https://github.com/tinyhumansai/openhuman/pull/877) | fix(install.sh): dry-run exits 0 when platform asset missing | `merged` |

</details>

<details>
<summary><strong>⚡ Energi Core</strong> — EVM L1 — scalability and security infrastructure</summary>

<br>

Worked closely with the Energi Core EVM chain on scalability and security infrastructure across the protocol.

</details>

---

## 🛠 Stack

**Smart Contracts**
![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat&logo=solidity&logoColor=white)
![Foundry](https://img.shields.io/badge/Foundry-1C1C1C?style=flat)
![Hardhat](https://img.shields.io/badge/Hardhat-FFF100?style=flat&logo=hardhat&logoColor=000)
![OpenZeppelin](https://img.shields.io/badge/OpenZeppelin-4E5EE4?style=flat&logo=openzeppelin&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000?style=flat&logo=rust&logoColor=white)
![Anchor](https://img.shields.io/badge/Anchor-512BD4?style=flat)

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
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=000)
![ethers.js](https://img.shields.io/badge/ethers.js-2535A0?style=flat)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)

**Chains:** Ethereum · Arbitrum · Polygon · BNB · opBNB · Solana

---

## 📬 Let's Connect

[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Riteish29)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:riteishnikhoria@gmail.com)

Open to freelance / contract work on protocol design, smart-contract development, and security-focused audits.

---

![Riteish's GitHub stats](https://github-readme-stats.vercel.app/api?username=obchain&show_icons=true&hide_border=true&theme=cobalt&include_all_commits=true&count_private=true)
