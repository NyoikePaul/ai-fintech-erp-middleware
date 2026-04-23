from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Union
import httpx
import base64
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(tags=["Payments"])

class StkPushRequest(BaseModel):
    phone: str
    amount: int
    account_ref: str
    description: str

def get_timestamp():
    return datetime.now().strftime('%Y%m%d%H%M%S')

def get_password(shortcode, passkey, timestamp):
    data_to_encode = shortcode + passkey + timestamp
    return base64.b64encode(data_to_encode.encode()).decode('utf-8')

@router.post("/mpesa/stkpush")
async def initiate_stk_push(req: StkPushRequest):
    # DARAJA SANDBOX DEFAULTS
    DARAJA_URL = "https://sandbox.safaricom.co.ke"
    # These are the standard Safaricom Sandbox test credentials
    CONSUMER_KEY = "pk_test_placeholder" # Use your real key from developer.safaricom.co.ke
    CONSUMER_SECRET = "sk_test_placeholder" # Use your real secret
    
    BUSINESS_SHORT_CODE = "174379"
    PASSKEY = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    # Change this to your ngrok URL for real testing!
    CALLBACK_URL = "https://your-domain.com/api/v1/payments/mpesa/callback"
    
    timestamp = get_timestamp()
    password = get_password(BUSINESS_SHORT_CODE, PASSKEY, timestamp)

    try:
        async with httpx.AsyncClient() as client:
            # 1. Get OAuth Token
            logger.info("Requesting OAuth token from Safaricom...")
            auth_res = await client.get(
                f"{DARAJA_URL}/oauth/v1/generate?grant_type=client_credentials",
                auth=(CONSUMER_KEY, CONSUMER_SECRET),
                timeout=15.0
            )
            
            if auth_res.status_code != 200:
                logger.error(f"Safaricom Auth Failed ({auth_res.status_code}): {auth_res.text}")
                return {"error": "Auth Failed", "safaricom_msg": auth_res.text}
            
            token = auth_res.json().get("access_token")

            # 2. Trigger STK Push
            headers = {"Authorization": f"Bearer {token}"}
            payload = {
                "BusinessShortCode": BUSINESS_SHORT_CODE,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": req.amount,
                "PartyA": req.phone,
                "PartyB": BUSINESS_SHORT_CODE,
                "PhoneNumber": req.phone,
                "CallBackURL": CALLBACK_URL,
                "AccountReference": req.account_ref,
                "TransactionDesc": req.description
            }
            
            stk_res = await client.post(
                f"{DARAJA_URL}/mpesa/stkpush/v1/processrequest", 
                json=payload, 
                headers=headers,
                timeout=15.0
            )
            return stk_res.json()
            
    except Exception as e:
        logger.error(f"STK Push Exception: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Middleware Error: {str(e)}")

@router.post("/mpesa/callback")
async def mpesa_callback(payload: dict, background_tasks: BackgroundTasks):
    logger.info(f"M-Pesa Callback: {payload}")
    return {"ResultCode": 0, "ResultDesc": "Success"}
