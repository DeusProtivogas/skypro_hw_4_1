from storage import Storage

class Store(Storage):
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.items = {}

    def _get_items(self):
        # for name, quan in self.items.items():
        #     print(f"{name}: {quan}")
        return self.items

    def _get_unique_items_count(self):
        return len(self.items)

    def _get_free_space(self):
        return self.capacity - sum(self.items.values())

    def add(self, name, quantity):
        response = ""
        if quantity <= self._get_free_space():
            self.items[name] = int(self.items.get(name, 0)) + quantity
            response += f"Added {quantity} of {name}\nFree space left: {self._get_free_space()}\n"
        else:
            # quantity = int(self.items.get(name, 0)) + self._get_free_space()
            response += f"Not enough free space left to add {name}\n"
            # print(f"Added {self._get_free_space()} of {name} (There was not enough free space for everything)")
            # self.items[name] = int(self.items.get(name, 0)) + self._get_free_space()
            # print(f"Free space left: {self._get_free_space()}")
        return response

    def remove(self, name, quantity):
        response = ""
        if name in self.items.keys():
            if int(self.items.get(name)) >= quantity:
                self.items[name] = int(self.items.get(name)) - quantity
                response += f"Removed {quantity} of {name}\nFree space left: {self._get_free_space()}\n"
            else:
                response += f"Not enough {name} is left\n"
                # print(f"Removed {self.items[name]} of {name} (There were no more items)")
                # self.items[name] = 0
                # print(f"Free space left: {self._get_free_space()}")
        else:
            response += f"No item {name}\n"
        return response