# AI-Fintech ERP Middleware ⚡

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI-Fintech ERP Middleware** is a high-performance bridge designed to connect African Fintech gateways (M-Pesa, Stripe) and Enterprise Resource Planning (ERP) systems (Odoo v16/v17) via intelligent AI agents.

## 🎯 Project Vision
Traditional ERP integrations in emerging markets are often brittle and manual. This middleware provides a production-ready, automated lifecycle: from **M-Pesa STK Push** triggers to automated ledger reconciliation in **Odoo**, supercharged by a **RAG (Retrieval-Augmented Generation)** agent for natural language financial reporting.

## 🚀 Core Features
* **Fintech Gateway:** Idempotent M-Pesa Daraja API integration (STK Push, C2B) with automated webhook verification.
* **ERP Synchronization:** Bi-directional XML-RPC connector for Odoo ledger reconciliation.
* **AI Financial Assistant:** Embedded LangChain agent using `pgvector` to query transaction history in natural language.
* **Enterprise Architecture:** Domain-Driven Design (DDD) with strict Pydantic v2 validation and JWT security.
* **DevOps Ready:** Built for cloud-native deployment with multi-stage Docker builds.

## 🛠 Tech Stack
* **Core:** Python 3.11, FastAPI
* **Database:** PostgreSQL with `pgvector`
* **AI/LLM:** LangChain, OpenAI GPT-4
* **ERP:** Odoo v16/v17 (XML-RPC)
* **Infrastructure:** Docker, Makefile automation

## ⚡ Quick Start

### Prerequisites
* Docker & Docker Compose
* Python 3.11+

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/NyoikePaul/ai-fintech-erp-middleware.git](https://github.com/NyoikePaul/ai-fintech-erp-middleware.git)
    cd ai-fintech-erp-middleware
    ```
2.  **Environment Setup:**
    ```bash
    cp .env.example .env
    # Configure your M-Pesa and Odoo credentials in .env
    ```
3.  **Launch Services:**
    ```bash
    make docker-up
    ```

## 🗺 Roadmap
- [ ] KRA eTIMS compliance automation for Kenyan markets.
- [ ] Stripe Payment Intent integration.
- [ ] Multi-tenant support for BiasharaOS scale-out.

## 🤝 Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.
