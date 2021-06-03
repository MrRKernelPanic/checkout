class Checkout:
    def __init__(self):
        self.basket = {}    

    def scan(self, items):
        for item in items:
            self._add_to_basket(item)    

    def _add_to_basket(self, item):
        if item in self.basket:
            self.basket[item] += 1
        else:
            self.basket[item] = 1
        
    def total_price(self):
        running_total=0
        for product, amount in self.basket.items():
            if product == "Apple":
                running_total += (amount // 6 * 1.5) + (amount % 6 * 0.3)
            elif product == "Banana":
                running_total += (amount // 5 * 1.0) + (amount % 5 * 0.25)
            elif product == "Steak Pie":
                running_total += (amount // 2 * 4.5) + (amount % 2 * 2.5)
            elif product == "Milk":
                running_total += 1.50 * amount
            elif product == "Washing Powder":
                running_total += (amount // 2 * 9) + (amount % 2 * 4.75)
        return running_total