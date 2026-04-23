from fastapi import FastAPI
from api.routes.payments import router as payments_router
from api.routes.ai_chat import router as ai_chat_router
from api.routes.erp_sync import router as erp_sync_router

app = FastAPI(title="BiasharaOS API")

# Mount routers with clean, logical prefixes
app.include_router(payments_router, prefix="/api/v1/payments")
app.include_router(ai_chat_router, prefix="/api/v1/ai")
app.include_router(erp_sync_router, prefix="/api/v1/erp")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
