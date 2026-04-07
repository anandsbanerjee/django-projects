
# TODO FILE

class Payment:
    def __init__(self, payment_id: str, amount: float, status: str):
        self.payment_id = payment_id
        self.amount = amount
        self.status = status

# Global in-memory storage for payments
payments = []

def receive_webhook(event: dict):
    """
    Process webhook event and update in-memory payment.
    Event contains:
        - payment_id
        - status
    """
    payment_id = event["payment_id"]
    status = event["status"]

    for payment in payments:
        if payment.payment_id == payment_id:
            payment.status = status
    #raise NotImplementedError
    # If payment not found, create a new one
    payments.append(Payment(payment_id=payment_id, amount=0.0, status=status))

def get_summary():
    """
    Return list of all payments as dictionaries with keys:
        payment_id, status
    """
    summary = []
    #evt_status = {}
    for payment in payments:
        evt_status = {"payment_id": payment.payment_id, "status": payment.status}
        summary.append(evt_status)
    return summary

    #raise NotImplementedError
