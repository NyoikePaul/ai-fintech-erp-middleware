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

## 🧱 Architecture Diagram
\`\`\`mermaid
graph TD
    A[Client Request] -->|STK Push| B(FastAPI Middleware)
    B -->|Async Task| C{Odoo Sync}
    B -->|Webhook| D[M-Pesa Gateway]
    D -->|Callback| B
    C -->|XML-RPC| E[Odoo ERP]
    B -->|Embeddings| F[(pgvector DB)]
    F -->|Context| G[AI RAG Agent]
    G -->|Response| A
\`\`\`

## 🛠 Usage Examples

### Trigger M-Pesa STK Push
\`\`\`bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/payments/mpesa/stkpush' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "phone": "2547XXXXXXXX",
  "amount": 1,
  "reference": "ORDER-101"
}'
\`\`\`

### Sample AI Query
**Query:** *"Show me all successful M-Pesa transactions above 5000 KES from last week."*
**Agent Logic:** The RAG agent converts this to SQL, queries the `pgvector` enabled database, and returns a natural language summary of the Odoo reconciliation status.

## 🧱 System Architecture
\`\`\`mermaid
graph TD
    User((Client/User)) -->|STK Push Request| API[FastAPI Middleware]
    API -->|Async Auth| MPESA[M-Pesa Daraja Gateway]
    MPESA -->|Webhook Callback| API
    API -->|Background Task| ODOO{Odoo Sync Service}
    ODOO -->|XML-RPC| ERP[Odoo ERP v16/17]
    API -->|Embeddings| VEC[(pgvector Database)]
    VEC -->|Context Retrieval| AI[LangChain RAG Agent]
    AI -->|Natural Language Insight| User
\`\`\`

## 🛠 Expert Usage Examples

### 1. Triggering an M-Pesa STK Push
Use this to initiate a real-time payment request to a customer's handset.
\`\`\`bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/payments/mpesa/stkpush' \
  -H 'Content-Type: application/json' \
  -d '{
  "phone": "2547XXXXXXXX",
  "amount": 1,
  "reference": "INV-2026-001"
}'
\`\`\`

### 2. Natural Language Financial Query (AI Agent)
Ask the middleware about your Odoo ledger data.
**Prompt:** *"Show me the total revenue reconciled from M-Pesa in the last 48 hours."*
**Agent Action:** The RAG agent queries the `pgvector` store, matches receipts to Odoo entries, and returns a formatted summary.

## 🧱 Enterprise Architecture
This middleware acts as the intelligent orchestration layer between fintech gateways and ERP ledgers.

\`\`\`mermaid
graph LR
    subgraph "External Systems"
    M[M-Pesa Daraja]
    O[Odoo ERP v16/17]
    end

    subgraph "Core Middleware"
    A[FastAPI Gateway]
    B[Background Tasks]
    C[(pgvector Store)]
    D[AI RAG Agent]
    end

    M -->|Webhooks| A
    A -->|Async Process| B
    B -->|XML-RPC| O
    A -->|Embeddings| C
    C -->|Context| D
    D -->|Insights| A
\`\`\`
<img width="1366" height="645" alt="image" src="https://github.com/user-attachments/assets/5d1054ba-1c98-46a1-8974-d8ea9f168d25" />
