def scan(item_name):
    prices=[]
    for item in item_name:
        if item == "Apple":
            prices.append(0.3)
        elif item == "Banana":
            prices.append(0.25)
        elif item == "Steak Pie":
            prices.append(2.50)
        elif item == "Milk":
            prices.append(1.50)
        else:
            prices.append(4.75)
    return prices