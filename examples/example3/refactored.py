from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount: float):
        pass


class PayPalPaymentProcessor(PaymentProcessor):

    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through PayPal.")


class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through Stripe.")


class SquarePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through Square.")


class PaymentService:

    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def make_payment(self, amount: float):
        self.payment_processor.process_payment(amount)


paypal_payment_processor = PayPalPaymentProcessor()
payment_service = PaymentService(paypal_payment_processor)
payment_service.make_payment(100.0)
