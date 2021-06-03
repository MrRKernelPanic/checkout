class Checkout:
    def __init__(self):
        self.basket = {}    

    def scan(self, items):
        running_total = 0
        
        for item in items:
            self._add_to_basket(item)    
            if item == "Apple":
                running_total += 0.3
            elif item == "Banana":
                running_total += 0.25
            elif item == "Steak Pie":
                running_total += 2.50
            elif item == "Milk":
                running_total += 1.50
            else:
                running_total += 4.75
        return running_total

    def _add_to_basket(self, item):
        if item in self.basket:
            self.basket[item] += 1
        else:
            self.basket[item] = 1
        
    def check_basket(self, basket_items):
        return self.basket.get("Apple")
        