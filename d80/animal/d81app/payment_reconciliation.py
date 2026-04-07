from d80.animal.d81app.payment_webhook import Payment

class Payment:
    def __init__(self, payment_id, amount, status="pending"):
        self.payment_id = payment_id
        self.amount = amount
        self.status = status

    def reconcile_payments(local_payments, third_party_payments):
        report = {
            "matched": [],
            "missing_on_stripe": [],
            "unexpected_on_stripe": []
        }

        local_dict = {p.payment_id: p for p in local_payments}
        third_party_dict = {p.payment_id: p for p in third_party_payments}

        # Check local payments
        for payment_id, local_payment in local_dict.items():
            if payment_id in third_party_dict:
                third_payment = third_party_dict[payment_id]
                if local_payment.amount == third_payment.amount:
                    report["matched"].append(payment_id)
                else:
                    report["missing_on_stripe"].append(payment_id)
            else:
                report["missing_on_stripe"].append(payment_id)

        # Check extra third-party payments
        for payment_id in third_party_dict:
            if payment_id not in local_dict:
                report["unexpected_on_stripe"].append(payment_id)

        return report




    # Extra methods
    def reconcile_payments_by_id(local_payments, third_party_payments):
        report = []

        local_dict = {payment.payment_id: payment for payment in local_payments}
        third_party_dict = {payment.payment_id: payment for payment in third_party_payments}

        # Check local payments
        for payment_id, local_payment in local_dict.items():
            if payment_id in third_party_dict:
                third_party_payment = third_party_dict[payment_id]
                if local_payment.amount == third_party_payment.amount:
                    status = "matched"
                else:
                    status = "amount_mismatch"
            else:
                status = "missing_on_stripe"

            report.append({
                "payment_id": payment_id,
                "status": status
            })

        # Check extra payments in third party
        for payment_id in third_party_dict:
            if payment_id not in local_dict:
                report.append({
                    "payment_id": payment_id,
                    "status": "unexpected_on_stripe"
                })

        return report

