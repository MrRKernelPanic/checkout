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
        
    def check_basket(self, basket_items):
        return self.basket.get(basket_items)

    def total_price(self):
        running_total=0
        for product, amount in self.basket.items():
            if product == "Apple":
                running_total += 0.3 * amount
            elif product == "Banana":
                running_total += 0.25 * amount
            elif product == "Steak Pie":
                running_total += 2.50 * amount
            elif product == "Milk":
                running_total += 1.50 * amount
            else:
                running_total += 4.75 * amount
        return running_total