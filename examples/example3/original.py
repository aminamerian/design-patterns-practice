class PayPalPaymentProcessor:
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through PayPal.")


class PaymentService:
    def __init__(self):
        self.payment_processor = PayPalPaymentProcessor()

    def make_payment(self, amount: float):
        self.payment_processor.process_payment(amount)


# Usage
payment_service = PaymentService()
payment_service.make_payment(100.0)
