from fastapi import APIRouter, Header, HTTPException, BackgroundTask, Depends
from domain.mpesa.schemas import MpesaCallbackPayload
from domain.mpesa.services import mpesa_service
from domain.odoo.connector import odoo_sync
import logging

router = APIRouter(prefix="/payments", tags=["Fintech"])
logger = logging.getLogger("uvicorn")

@router.post("/mpesa/stkpush")
async def trigger_payment(phone: str, amount: int, reference: str):
    """Initiate an STK Push to a client's phone."""
    try:
        result = await mpesa_service.trigger_stk_push(phone, amount, reference)
        return {"status": "requested", "checkout_id": result.get("CheckoutRequestID")}
    except Exception as e:
        logger.error(f"STK Push Failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Payment initiation failed")

@router.post("/mpesa/callback")
async def mpesa_callback(payload: MpesaCallbackPayload, background_tasks: BackgroundTask):
    """
    Production-grade webhook handler for M-Pesa.
    Uses BackgroundTasks to sync with Odoo so the webhook returns 200 OK immediately.
    """
    # 1. Validate Transaction
    result_code = payload.Body.stkCallback.ResultCode
    merchant_id = payload.Body.stkCallback.MerchantRequestID
    
    if result_code == 0:
        logger.info(f"Payment Successful for {merchant_id}")
        
        # 2. Trigger async Odoo reconciliation
        # This keeps the API responsive and avoids timeout issues with Safaricom
        background_tasks.add_task(
            odoo_sync.reconcile_transaction, 
            payload.Body.stkCallback.CallbackMetadata
        )
    else:
        logger.warning(f"Payment Cancelled/Failed for {merchant_id}")

    return {"ResultCode": 0, "ResultDesc": "Success"}
