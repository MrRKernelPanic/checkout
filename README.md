
![Basket](https://www.materialui.co/materialIcons/action/shopping_basket_black_192x192.png)

# Checkout

This is a checkout system that can handle prices and special offers.  The system has several products hard coded into an dictionary.

Inputs can be supplied via the console using the Scan command passing a number of products in list format.

Outputs the system output the total cost of products factoring in deals

---
## Requirements
Implement a checkout system that handles both one-off pricing schemes as well as special offers.

The checkout needs to be able to scan items one by one or in groups and give a total price taking into account any special offers. Our products have Stock Keeping Units (**SKUs**), individual prices, and multi-buy rates.

Here is the stock list:

|Item            | SKU | Unit Price | Special Price  |
| -------------- | --- | ---------- | -------------- |
| Apple          | A   | £0.30      | 6 for $1.50    |
| Banana         | B   | £0.25      | 5 for £1.00    |
| Steak Pie      | C   | £2.50      | 2 for £4.50    |
| Milk           | D   | £1.50      |                |
| Washing Powder | E   | £4.75      | 2 for £9.00    |

---
## Approach
A TTD approach was taken to solve this scenario.
- A series of test were generated to scan a single item and return the appropriate price.
- Next the system was able to take in multiple items in a list format (not taking into account special offers)
- The system was then modified to take into account deal prices based on a count of each item.
- A refactor was then implemented that introduced a Class Based system that included both the supplied product details and orders in a dictionary.
- The system has the limited product information internally hardcoded, however in a real world scenario this information would be looked up from a stores database containing all the pertinent information.
-The system should be refactored around pence rather than pounds as the base unit to avoid errors and loosing data with large orders.

---
## Dependencies
The system was created and run and tested on Python 3.7+ using Pytest which can easily be installed using ```apt install python3-pytest``` or via pip using ```pip install -U pytest```

## Getting Started
- Clone this repo
- Navigate to the directory

## Usage
- import the checkout.py ```from checkout import Checkout```
- Create an instance of the checkout ```ckout = Checkout()```
- use the scan([list of comma seperated products as strings]) to add items to the basket, ```ckout.scan(["Apple"])```
- Use ```ckout.total_price()``` to see the total basket value taking into account deals.

---
## Testing
There were 4 final tests left remaining.
- A single product scanned returns the number of that product
- Multiple products added to the basket and returns the number of each product added.
- A test to check the total of price of prdoducts is returned.
- A test to check if the deal prices are taken into account returing the price of the current basket.

---
## Reflections
Intially the use of simple functions sufficed for single item but required the passing of parameters and global variables.

A Class based approach simplied the process and the amount of code required to fufill the task.  Considering the checkout as an object and having basket as a dictinary store of the products in a basket again made things more manageable and scalable.

The system only deals with a limited number of products (in this case 5), however as this is represented as a dictionary lookup this information could be initally loaded in, or even looked up from an external source such as a textfile (CSV) or from a external database/data source.

Products could then be looked up from the dictionary using either the SKU, or perhaps the barcode of a product for automation.  Currently the basket is simply a dictionary of product names and quantities.