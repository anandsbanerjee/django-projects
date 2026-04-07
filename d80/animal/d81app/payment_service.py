
class Payment:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount
        self.payment_status="Pending"

    def validate_amount(self, amount):
        if amount > 0:
            return True
        return False

    def initiate_payment(self, amount):
        if self.validate_amount(amount):
            self.amount = amount
            self.payment_status = "Pending"
            return "Payment initiated"
        else:
            self.payment_status = "Failed"
            raise Exception ("Payment Failed")

    def handle_payment_response(self, response):
        if response is None:
            self.payment_status = "Pending"
            return

        status = response.get("payment_status")


        if status == "Completed":
            self.payment_status = "Completed"

        elif status == "Failed":
            self.payment_status = "Failed"

        else:
            self.payment_status = "Pending"
