import pytest

from checkout import Checkout

def test_scan_item():
    checkout = Checkout()
    checkout.scan(["Apple"])
    assert checkout.basket["Apple"] == 1

def test_scan_multiple_items():
    checkout = Checkout()
    checkout.scan(["Milk", "Apple"])
    assert checkout.basket["Apple"] == 1 and checkout.basket["Milk"] == 1

def test_check_basket():
    checkout = Checkout()
    checkout.scan(["Apple", "Banana", "Apple"])
    assert checkout.check_basket("Apple") == 2

def test_total_price():
    checkout = Checkout()
    checkout.scan(["Apple", "Banana", "Apple"])
    assert checkout.total_price() == 0.85
