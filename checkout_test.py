import pytest

from checkout import Checkout

def test_scan_item_apple():
    checkout = Checkout()
    assert checkout.scan(["Apple"]) == 0.30

def test_scan_item_banana():
    checkout = Checkout()
    assert checkout.scan(["Banana"]) == 0.25

def test_scan_item_steak_pie():
    checkout = Checkout()
    assert checkout.scan(["Steak Pie"]) == 2.50

def test_scan_item_milk():
    checkout = Checkout()
    assert checkout.scan(["Milk"]) == 1.50

def test_scan_item_washing_powder():
    checkout = Checkout()
    assert checkout.scan(["Washing Powder"]) == 4.75

def test_scan_multiple_items():
    checkout = Checkout()
    assert checkout.scan(["Milk", "Apple"]) == 1.80

def test_check_basket():
    checkout = Checkout()
    checkout.scan(["Apple", "Banana", "Apple"])
    assert checkout.check_basket("Apple") == 2
