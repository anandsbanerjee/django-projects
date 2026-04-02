
class Payment:
    def __init__(self, payment_id: str, amount: float, status: str):
        """
            Initialize a payment object.
        """
        self.payment_id = payment_id
        self.amount = amount
        self.status = status

# Global in-memory storage for payments
payments = []

def initiate_payment(payment: Payment):
    """
    Simulate sending a payment request.
    Add payment to in-memory storage.
    """
    payments.append(payment)
    #pmt_id = payment.payment_id
    #payments[pmt_id] = payment

    #raise NotImplementedError

def callback(payment_id: str, status: str):
    """
    Update payment status based on callback.
    """
    for payment in payments:
        if payment.payment_id == payment_id:
            payment.status = status
            #payments.append(payment)

def get_payment_status(payment_id: str):
    """
    Return the current status of a payment.
    """
    for payment in payments:
        if payment.payment_id == payment_id:
            return payment.status
    #raise NotImplementedError
payment = Payment('1', 20.0, 'Pending')
initiate_payment(payment)
print("Payment Initiated ", payments)

pmt_status = get_payment_status(payment.payment_id)
print("Payment Status for the payment ID {} is {}".format(payment.payment_id, pmt_status))

callback(payment.payment_id, 'Completed')
print("Payment Status for the payment ID {} is {}".format(payment.payment_id, payment.status))