<div align="center">

# Riteish Nikhoria

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&pause=1000&color=2F81F7&center=true&vCenter=true&width=820&height=55&lines=Senior+Backend+%26+Platform+Engineer;Rust+%C2%B7+Go+%C2%B7+Node.js+%C2%B7+Kubernetes+%C2%B7+Claude%2FMCP;Architecture+through+deployment+and+on-call" alt="Senior Backend & Platform Engineer" />

</div>

## Hi there 👋

I'm Riteish, a **Senior Backend & Platform Engineer** with 7+ years spanning backend systems, platform/infrastructure, and AI agent development. I build production LLM agent infrastructure such as agent harnesses, memory and knowledge systems, and retrieval and summarization pipelines, and I integrate the Claude API and Model Context Protocol into developer and product workflows.

My foundation is deep backend work in Rust (Tokio, Axum), Go, and Node.js: event-driven microservices, gRPC/REST/WebSocket APIs, and high-throughput data pipelines on PostgreSQL, Redis, and MongoDB. I own platform and reliability end to end across Kubernetes (GKE and EKS), Terraform infrastructure-as-code, multi-cloud CI/CD with zero-downtime rollouts, and Prometheus/Grafana observability with SRE-grade alerting. I'm comfortable owning systems from architecture through deployment and on-call. I also ship across EVM and Solana smart contracts, account abstraction (ERC-4337), and DeFi protocols.

📍 New Delhi, India (GMT +5:30) &nbsp;·&nbsp; [Email](mailto:riteishnikhoria@gmail.com) &nbsp;·&nbsp; [LinkedIn](https://linkedin.com/in/web3-dev-riteish) &nbsp;·&nbsp; [Telegram](https://t.me/Riteish29)

## What I work with

- **Languages:** Rust, Go, TypeScript, JavaScript, Python, Solidity
- **Backend & Systems:** distributed systems, microservices, event-driven architecture, REST, gRPC, WebSockets, message queues, pub/sub, caching, idempotency, horizontal scaling, fault tolerance, concurrency (Tokio, goroutines, async/await), zero-copy parsing, connection pooling, Axum, Actix, Express.js, Gin
- **Platform & DevOps:** Kubernetes (GKE, EKS), Docker, Terraform, GitHub Actions CI/CD, AWS, GCP, zero-downtime and rolling deploys, automated rollback, Prometheus, Grafana, structured logging, distributed tracing, SLOs, incident response
- **Agentic Engineering:** Claude, Anthropic SDK, Model Context Protocol (MCP), agent harnesses, memory and knowledge systems, canonicalization, chunking, retrieval and summarization pipelines, vector databases, LLM-assisted testing and code review, Claude Code, Codex
- **Data Stores:** PostgreSQL, Redis, MongoDB, SQLite, time-series stores, query optimization, indexing, connection pooling
- **On-chain:** Solidity, EVM and Solana, account abstraction (ERC-4337), DeFi protocols, ethers.js, viem, Foundry, Hardhat, Anchor

## Experiences

### Backend & Systems

- Built Go backend services for protocol indexing, position tracking, and APY computation, using concurrent worker pools to sync on-chain state into low-latency client-facing APIs without state drift across millions of daily events.
- Developed Node.js/TypeScript services exposing REST and WebSocket APIs for real-time position and liquidation data, backed by PostgreSQL with structured logging and metrics.
- Built high-throughput Rust services on Tokio and Axum: async event listeners and indexing pipelines streaming upstream data into client backends, tuned with zero-copy parsing, connection pooling, and bounded concurrency for sustained low latency.
- Implemented a Rust relayer/keeper coordinating submission, retries, and nonce sequencing across redundant endpoints for reliable exactly-once execution under load.
- Exposed gRPC and REST APIs from goroutine-based Go microservices on PostgreSQL, with Prometheus instrumentation and structured logging baked in from day one.
- Established modular, upgradeable service architectures enabling extensibility and zero-downtime evolution of long-running systems.

### Platform & Reliability

- Owned the platform stack: provisioned Kubernetes workloads on GKE/EKS with Terraform, ran GitHub Actions CI/CD with rolling deploys and automated rollback, and kept services available through breaking upgrades.
- Stood up delivery pipelines for Dockerized Go and Rust services with Kubernetes deploys and Terraform-managed infrastructure across GCP and AWS for repeatable zero-downtime releases.
- Hardened reliability with SLO-backed alerting on latency and error budgets, cutting time-to-detect on failed executions through proactive monitoring rather than user reports.

### AI Agent Infrastructure

- Contributed 50+ merged PRs to OpenHuman, a Rust + TypeScript open-source AI agent harness, across the Rust core, Tauri desktop app, and developer tooling.
- Designed the agent's memory tree and knowledge base in the Rust core, including the canonicalization, chunking, and summarization pipeline that turns raw context into retrievable long-term memory, backed by embedded SQLite storage.
- Built typed tool interfaces and OAuth-connector flows that let the agent invoke external services safely, shipping the integration layer end to end across the Rust core and TypeScript desktop app.
- Drove an agent-driven development workflow using Claude Code and Codex to scaffold, review, and test changes, matching the project's own dogfooding model.

### Blockchain & DeFi

- Designed and optimized AMMs (Automated Market Makers), with a deep understanding of liquidity pools, token-swap logic, fee distribution, and DEX dynamics.
- Worked on lending and borrowing design heavily influenced by the concentrated-liquidity mechanism of Uniswap V3, enabling more efficient capital utilization.
- Integrated ERC-4337 account abstraction with session keys, enabling smart-account collateral management, Paymaster-sponsored gasless transactions, and pre-approved keeper actions.
- Developed a Solana OFT via LayerZero for Base to Solana transfers, with Token2022 tax-enabled tokens and Raydium CLMM pools using solana-web3.js.
- Developed Solana programs in Rust with Anchor using the SPL Token program, PDAs, and CPIs, and built SPL token and vault programs with mint/transfer authorities and Borsh serialization.
- Automated multi-chain deployment with Hardhat scripts across Ethereum, Linea, zkSync, Optimism, and Manta for consistent, repeatable release workflows.
- Built Node.js services with Chainlink oracle pipelines to index events, serve off-chain data, and keep pricing and risk metrics in sync with on-chain state. Oracles worked with: Chainlink, Pyth, TWAP, RedStone.
- Developed and deployed ERC-20, ERC-721, ERC-1155, and ERC-2535 (Diamond) contracts to tokenize in-game rewards, merchandise, and collectibles, plus staking contracts for platform-token rewards.
- Created a transparent on-chain betting settlement contract, optimizing the settlement algorithm to cut computation time by 40%.
- Designed upgradeable contracts using Transparent and UUPS proxy patterns, with EIP-1155/2535/777 integration for modularity and extended token functionality.
- Chains worked on: Ethereum, Binance, Polygon, Arbitrum, opBNB, Linea, zkSync, Optimism, Manta, Solana.

## What I'm Building

Currently contributing to **OpenHuman** (TinyHumans), a Rust + TypeScript open-source AI agent harness, with 50+ merged PRs across the Rust core, Tauri desktop app, and developer tooling. I designed the agent's memory tree and knowledge base in the Rust core, including the canonicalization, chunking, and summarization pipeline that turns raw context into retrievable long-term memory, backed by embedded SQLite. I also built typed tool interfaces and OAuth-connector flows that let the agent invoke external services safely, and I drive an agent-driven development workflow using Claude Code and Codex to scaffold, review, and test changes.

Alongside this I build protocol tooling such as **[MantissaFi](https://github.com/obchain/MantissaFi)**, a fully on-chain European options protocol computing Black-Scholes pricing and Greeks entirely in Solidity (gas-optimized with PRBMath SD59x18), with an on-chain implied-volatility surface, verified with Foundry fuzz/invariant tests and Certora/Halmos formal proofs.

## Protocol Contributions

- **[mahaxyz/contracts](https://github.com/mahaxyz/contracts)** &nbsp;·&nbsp; Solidity &nbsp;·&nbsp; 37 stars, 8 forks. Smart contracts for the maha.xyz protocol.
- **[mahaxyz/solana-contracts](https://github.com/mahaxyz/solana-contracts)** &nbsp;·&nbsp; Rust. Solana programs for the maha.xyz protocol.
- **[MantissaFi](https://github.com/obchain/MantissaFi)** &nbsp;·&nbsp; Solidity. Fully on-chain European options protocol implementing Black-Scholes-Merton pricing entirely in Solidity.
- **[agent-contracts](https://github.com/obchain/agent-contracts)** &nbsp;·&nbsp; Solidity. Smart contracts for an AI agent framework.
- **[gmx-v2-lens](https://github.com/obchain/gmx-v2-lens)** &nbsp;·&nbsp; Solidity. A lens contract that aggregates market analytics data from the GMX V2 decentralized exchange.
