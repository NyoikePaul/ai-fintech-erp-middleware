import xmlrpc.client
from core.config import settings
import logging

logger = logging.getLogger("uvicorn")

class OdooSync:
    """
    Expert-level Odoo integration using XML-RPC.
    Handles authentication, searching for records, and transaction reconciliation.
    """
    def __init__(self):
        self.url = settings.ODOO_URL
        self.db = settings.ODOO_DB
        self.username = settings.ODOO_USERNAME
        self.password = settings.ODOO_PASSWORD
        self.common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        self.uid = None

    def _authenticate(self):
        """Authenticate with Odoo and cache the UID."""
        if not self.uid:
            self.uid = self.common.authenticate(self.db, self.username, self.password, {})
        return self.uid

    def reconcile_transaction(self, metadata: dict):
        """
        Synchronizes an M-Pesa transaction metadata into Odoo's accounting module.
        """
        try:
            uid = self._authenticate()
            models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")
            
            # Extracting M-Pesa data (example mapping)
            amount = next(item['Value'] for item in metadata['Item'] if item['Name'] == 'Amount')
            receipt = next(item['Value'] for item in metadata['Item'] if item['Name'] == 'MpesaReceiptNumber')
            phone = next(item['Value'] for item in metadata['Item'] if item['Name'] == 'PhoneNumber')

            # Create a payment record in Odoo
            payment_id = models.execute_kw(self.db, uid, self.password, 'account.payment', 'create', [{
                'amount': amount,
                'payment_type': 'inbound',
                'partner_type': 'customer',
                'communication': f"M-Pesa Receipt: {receipt}",
                'payment_method_line_id': 1, # Standard Manual ID, usually dynamic in production
                'memo': f"Auto-reconciled from M-Pesa {phone}"
            }])
            
            logger.info(f"Odoo Reconciliation Success: Payment ID {payment_id}")
            return payment_id

        except Exception as e:
            logger.error(f"Odoo Sync Failed: {str(e)}")
            return None

odoo_sync = OdooSync()
