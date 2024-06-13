from abc import ABC, abstractmethod


# State pattern: Abstract State Interface
class VendingMachineState(ABC):

    @abstractmethod
    def insert_coin(self, vending_machine):
        pass

    @abstractmethod
    def select_item(self, vending_machine):
        pass

    @abstractmethod
    def take_item(self, vending_machine):
        pass


# State pattern: Concrete States
class NoCoinState(VendingMachineState):

    def insert_coin(self, vending_machine):
        vending_machine.set_state(vending_machine.has_coin_state)
        print("Coin inserted.")

    def select_item(self, vending_machine):
        print("Insert coin first.")

    def take_item(self, vending_machine):
        print("No item to take.")


class HasCoinState(VendingMachineState):

    def insert_coin(self, vending_machine):
        print("Coin already inserted.")

    def select_item(self, vending_machine):
        vending_machine.set_state(vending_machine.item_dispensed_state)
        print("Item dispensed.")

    def take_item(self, vending_machine):
        print("Please select an item first.")


class ItemDispensedState(VendingMachineState):

    def insert_coin(self, vending_machine):
        print("Please take your item first.")

    def select_item(self, vending_machine):
        print("Please take your item first.")

    def take_item(self, vending_machine):
        vending_machine.set_state(vending_machine.no_coin_state)
        print("Item taken. Ready for next customer.")


# State pattern: Context
class VendingMachine:

    def __init__(self):
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.item_dispensed_state = ItemDispensedState()

        self.state = self.no_coin_state

    def set_state(self, state: VendingMachineState):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin(self)

    def select_item(self):
        self.state.select_item(self)

    def take_item(self):
        self.state.take_item(self)


# Usage
vending_machine = VendingMachine()
vending_machine.insert_coin()
vending_machine.select_item()
vending_machine.take_item()
