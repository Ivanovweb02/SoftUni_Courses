class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        self.product = product
        if len(Storage.storage) < self.capacity:
            Storage.storage.append(self.product)

    def get_products(self):
        return Storage.storage


current_capacity = int(input())
storage = Storage(current_capacity)

while len(storage.storage) < current_capacity:
    current_product = input()
    storage.add_product(current_product)

print(storage.get_products())
