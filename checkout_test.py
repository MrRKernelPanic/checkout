import pytest

from checkout import scan

def test_scan_item_apple():
    assert scan("Apple") == 0.30

def test_scan_item_banana():
    assert scan("Banana") == 0.25

def test_scan_item_steak_pie():
    assert scan("Steak Pie") == 2.50

def test_scan_item_milk():
    assert scan("Milk") == 1.50

def test_scan_item_washing_powder():
    assert scan("Washing Powder") == 4.75