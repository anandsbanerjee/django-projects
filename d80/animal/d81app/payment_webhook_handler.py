class PaymentWebhookHandler:
    def __init__(self, order_id):
        self.order_id = order_id
        self.payment_status = "Pending"

    def listen_for_webhook(self, data):
        if data is None:
            self.payment_status = "Unknown"
            return

        if(self.order_id == data.get("order_id")):
            self.update_order_status(data)

    def update_order_status(self, data):
        if data is None:
            return

        status = data.get("status")

        if status is None:
            self.payment_status = "Unknown"
            return

        if status is status == "Paid":
           self.payment_status = "Paid"
        elif status is status == "Failed":
            self.payment_status = "Failed"
        else:
            self.payment_status = "Unknown"