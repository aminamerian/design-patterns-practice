## Payment Processing System

This example contains a basic payment processing system.

In the `original.py`
- The `PaymentService` class is tightly coupled to the `PayPalPaymentProcessor` class. 
- Adding new payment processors would require modifying the `PaymentService` class, violating the **Open/Closed Principle (OCP)**. 

The refactored version in `refactored.py` introduces an abstract interface for payment processors and implements concrete payment processors for different gateways. This decouples the PaymentService class from specific payment processor implementations.