## Vending Machine

Imagine you have a simple vending machine that handles dispensing items and managing states (e.g., no coin, has coin, item dispensed).

In the `original.py`
- The VendingMachine class handles all states and transitions internally, leading to a complex and hard-to-maintain code structure.
- Adding new states or changing existing ones would require modifying the VendingMachine class significantly, violating the **Open/Closed Principle (OCP)**. 

In the `refactored.py`, the vending machine uses the **State** design pattern to represent different states and transitions. Each state is a separate class that encapsulates its behavior and transitions. 
- Single Responsibility Principle (SRP) is adhered to by separating the behavior of each state into its own class.
- Open/Closed Principle (OCP) allows adding new states without modifying existing code.
- State transitions are managed through polymorphism, allowing the vending machine to change states dynamically.