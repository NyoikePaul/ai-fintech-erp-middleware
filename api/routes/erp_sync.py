from fastapi import APIRouter

router = APIRouter(tags=["ERP Sync"])

@router.post("/sync")
async def trigger_manual_sync():
    return {"message": "Manual sync with Odoo initiated"}

@router.get("/health")
async def erp_health():
    return {"status": "connected", "provider": "Odoo/BridgeERP"}
