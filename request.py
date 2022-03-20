

class Request():

    def __init__(self, line):
        words = line.split(" ")
        self.from_address = words[4]
        if len(words) < 6:
            self.to_address = words[-1]
        else:
            self.to_address = "магазин"
        self.amount = words[1]
        self.product = words[2]

    @property
    def _get_product(self):
        return self.product

    @property
    def _get_amount(self):
        return int(self.amount)

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_address} в {self.to_address}"
