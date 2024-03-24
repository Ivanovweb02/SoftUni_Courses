class Inventory:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self.capacity_value = self._capacity
        self.items = []

    def add_item(self, item: str):
        self.item = item
        if 0 < self._capacity:
            self.items.append(self.item)
            self._capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity_value

    def __repr__(self):
        self.left_capacity = self.capacity_value - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
