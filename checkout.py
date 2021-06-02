def scan(item_name):
    running_total = 0
    for item in item_name:
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