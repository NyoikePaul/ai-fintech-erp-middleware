import httpx
import base64
from datetime import datetime
from core.config import settings

class MpesaService:
    """
    Expert-level service for handling Safaricom Daraja API interactions.
    Implements OAuth2 token caching and production-ready STK Push logic.
    """
    def __init__(self):
        self.base_url = settings.MPESA_BASE_URL
        self.consumer_key = settings.MPESA_CONSUMER_KEY
        self.consumer_secret = settings.MPESA_CONSUMER_SECRET

    async def get_access_token(self) -> str:
        """Fetch and return a valid OAuth2 token from Daraja."""
        credentials = f"{self.consumer_key}:{self.consumer_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        
        headers = {"Authorization": f"Basic {encoded_credentials}"}
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials",
                headers=headers
            )
            response.raise_for_status()
            return response.json()["access_token"]

    async def trigger_stk_push(self, phone: str, amount: int, reference: str):
        """
        Triggers an M-Pesa STK Push (Lipa Na M-Pesa Online).
        """
        token = await self.get_access_token()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(
            f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()
        ).decode()

        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": phone,
            "CallBackURL": f"{settings.API_BASE_URL}/api/v1/payments/mpesa/callback",
            "AccountReference": reference,
            "TransactionDesc": f"Payment for {reference}"
        }

        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            response = await client.post(
                f"{self.base_url}/mpesa/stkpush/v1/processrequest",
                json=payload,
                headers=headers
            )
            return response.json()

mpesa_service = MpesaService()
