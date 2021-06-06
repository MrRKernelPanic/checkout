class Checkout:

    def __init__(self):
        self.basket = {}
        self.prices = {
            "Apple": {
                "price": 0.30,
                "sku": "A",
                "offer_amount": 6,
                "offer_price": 1.50
            },
            "Banana": {
                "price": 0.25,
                "sku": "B",
                "offer_amount": 5,
                "offer_price": 1.00
            },
            "Steak Pie": {
                "price": 2.5,
                "sku": "C",
                "offer_amount": 2,
                "offer_price": 4.50
            },
            "Milk": {
                "price": 1.50,
                "sku": "D",
                "offer_amount": 1,
                "offer_price": 1.50
            },
            "Washing Powder": {
                "price": 4.75,
                "sku": "E",
                "offer_amount": 2,
                "offer_price": 9.00
            }
        }    

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
            product_info = self.prices[product]
            product_deal = self._calculate_product_deal(product, amount)
            product_remainder = ((amount % product_info["offer_amount"]) * product_info["price"])
            print("product:"+ str(product))
            print("Amount:" + str(amount))
            print("Div:" + str(product_deal))
            print("Mod:" + str(product_remainder))
            print("offer amount:" + str(product_info["offer_amount"]))
            print("offer_price:" + str(product_info["offer_price"]))
            running_total += ( product_deal + product_remainder)
        return running_total

    def _calculate_product_deal(self, product, amount):
        product_info = self.prices[product]
        return ((amount // product_info["offer_amount"]) * product_info["offer_price"])
