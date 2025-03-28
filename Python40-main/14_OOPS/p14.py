from abc import ABC, abstractmethod


# abs class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# concrete class
class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using credit card")


# concrete class
class PayPalPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using paypal")


# object
payment1 = CreditCardPayment()
payment2 = PayPalPayment()

payment1.pay(100)
payment2.pay(200)


# client code
def process_payment(payment_method, amount):
    payment_method.pay(amount)


process_payment(payment1, 1000)

process_payment(payment2, 2000)
