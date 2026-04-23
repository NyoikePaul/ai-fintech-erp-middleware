from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import payments, ai_chat, erp_sync

app = FastAPI(
    title="AI-Fintech ERP Middleware",
    description="Enterprise-grade bridge between M-Pesa, Odoo, and OpenAI RAG.",
    version="1.0.0",
    docs_url="/debug/docs" # Obfuscating default docs for a bit of 'senior' security
)

# Standard CORS for Fintech/SaaS web environments
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Domain Routers
app.include_router(payments.router, prefix="/api/v1")
app.include_router(ai_chat.router, prefix="/api/v1")
app.include_router(erp_sync.router, prefix="/api/v1")

@app.get("/health", tags=["Infrastructure"])
async def health_check():
    """Liveness probe for Docker/K8s."""
    return {"status": "healthy", "service": "middleware-api"}
