class VendingMachine:
    def __init__(self):
        self.state = "no_coin"

    def insert_coin(self):
        if self.state == "no_coin":
            self.state = "has_coin"
            print("Coin inserted.")
        elif self.state == "has_coin":
            print("Coin already inserted.")
        elif self.state == "item_dispensed":
            print("Please take your item first.")

    def select_item(self):
        if self.state == "no_coin":
            print("Insert coin first.")
        elif self.state == "has_coin":
            self.state = "item_dispensed"
            print("Item dispensed.")
        elif self.state == "item_dispensed":
            print("Please take your item first.")

    def take_item(self):
        if self.state == "no_coin":
            print("No item to take.")
        elif self.state == "has_coin":
            print("Please select an item first.")
        elif self.state == "item_dispensed":
            self.state = "no_coin"
            print("Item taken. Ready for next customer.")


# Usage
vending_machine = VendingMachine()
vending_machine.insert_coin()
vending_machine.select_item()
vending_machine.take_item()
