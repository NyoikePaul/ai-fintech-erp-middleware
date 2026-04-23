from pydantic import BaseModel, Field
from typing import List, Optional

class CallbackItem(BaseModel):
    Name: str
    Value: Optional[str | int] = None

class CallbackMetadata(BaseModel):
    Item: List[CallbackItem]

class StkCallback(BaseModel):
    MerchantRequestID: str
    CheckoutRequestID: str
    ResultCode: int
    ResultDesc: str
    CallbackMetadata: Optional[CallbackMetadata] = None

class CallbackBody(BaseModel):
    stkCallback: StkCallback

class MpesaCallbackPayload(BaseModel):
    """
    Strict validation schema for Safaricom M-Pesa STK Push callbacks.
    Ensures type safety for all incoming financial data.
    """
    Body: CallbackBody
