from store import Store

class Shop(Store):

    def __init__(self, limit = 5):
        # self.capacity = capacity
        # self.items = {}
        super().__init__()
        self.items = {}
        self.capacity = 20
        self._limit = limit

    @property
    def _get_limit(self):
        return self._limit

    def add(self, name, quantity):
        response = ""
        if self._get_unique_items_count() > self._get_limit:
            response += f"Too many different goods already!\n"
        else:
            response += super().add(name, quantity)
        return response