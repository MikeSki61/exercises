"""
mk_core.py
This file is the core file that provides the functions for the app.
It includes the ability to add, remove, edit, and export the list.

Functions are:
- add_items(): Add items to the list.
-remove_items(): Removes items from the list.
-edit_items(): Edits any item within the list. Any value can be edited.
-export_items(): Able to export the list.

Author: Mike Kwiatkowsky
Version:1.0.0
"""
# The grocery_list is a list of items showing the keywords and values of each.
# Also this shows the type of item within the list ex: "name" is a string, 
# cost is a float, priority is an integer and buy is a boolean.-True or False.
grocery_list: list[dict[str, float | int | bool | str]] = [
    {
        "name": "milk",
        "store": "Walmart",
        "cost": 6.47,
        "amount": 2,
        "priority": 1,
        "buy": True,
        "date": "Nov",
        "category": "dairy",
    },
    {
        "name": "bread",
        "store": "Wal-Mart",
        "cost": 4.50,
        "amount": 2,
        "priority": 1,
        "buy": True,
        "date": "Nov",
        "category": "dairy",
    },
    {
        "name": "eggs",
        "store": "Wal-Mart",
        "cost": 5.0,
        "amount": 1,
        "priority": 1,
        "buy": True,
        "date": "Nov",
        "category": "dairy",
    },
    {
        "name": "peanut butter",
        "store": "Costco",
        "cost": 12.5,
        "amount": 1,
        "priority": 3,
        "buy": True,
        "date": "Nov",
        "category": "snack",
    },
    {
        "name": "chicken",
        "store": "Costco",
        "cost": 25,
        "amount": 1,
        "priority": 2,
        "buy": True,
        "date": "Nov",
        "category": "poultry",
    },
]

"""
The add items() function is to be able to add new items to the 
current grocery_list app.
Any keyword and value can be added.
The grocery_list.append() will add the item to the existing list.

"""
# Add items to the list
def add_item(name: str, store: str, cost: float, 
            amount: int, priority: int, buy: bool, 
            date: str, category: str):
    item = {
        "name": name,
        "store": store,
        "cost": cost,
        "amount": amount,
        "priority": priority,
        "buy": True,
        "date": date,
        "category": category,
    }
    grocery_list.append(item)

"""
The remove_items() function will provide the user the ability 
to remove any item from the list.
The grocery_lst.pop() function will do that.
"""
# Remove items from the list
def remove_item(name: str) -> str:
    index = get_index_from_name(name)

    grocery_list.pop(index)

"""
The edit_items() function allows the user to edit(change) any item 
in the list.
"""
# Edit items
def edit_item(name: str, store: str, cost: float, 
            amount: int, priority:int, buy: bool, 
            date: str, category: str):
    index = get_index_from_name(name)

    old_item = grocery_list[index]

    item = {
        "name": name,
        "store": store,
        "cost": cost,
        "amount": amount,
        "priority": priority,
        "buy": True,
        "date": date,
        "category": category,
    }

    if not store:
        store = item["store"]

    if not cost:
        cost = item["cost"]

    if not amount:
        amount = item["amount"]

    if not priority:
        priority = item["priority"]

    if not buy:
        buy = item["buy"]

    if not date:
        date = item["date"]

    if not category:
        date = item["category"]

    grocery_list[index] = item

"""
The export_items() function will export the items that may have
been edited, removed or  added to the list, 
creating a new list called the buy_list.

"""
def export_items():
    buy_list = []

    for item in grocery_list: # Iterate over the grocery list.
        if item["buy"]:
            buy_list.append(item) # If item is found, add to the grocery list.

    if buy_list:
        for item in buy_list: # Iterates over buy_list
            print(
                f"name: {item['name']} -store: {item['store']} -"
                f"cost: ${item['cost']} -amount: {item['amount']} -"
                f"priority: {item['priority']} -date: {item['date']} -"
                f"category:{item['category']}"
                )

        total_cost = calculate_total_cost(buy_list, round_cost=True)

        print(f"The total cost is ${total_cost: float}:")

"""
The get_index_from_name(name) function 
will return the name of the item.

"""
def get_index_from_name(name):
    index = 0

    for item in grocery_list:
        if item["name"] == name: # If item is equal to name, returns the value.
            return index
        else:
            index += 1 # Adds the item increases the count by one.
"""
The list_items() function will list / print the items.
"""
def list_items()-> str:
    for item in grocery_list:
        print(item)
""" 
The calculate_total_cost() function will calculate the 
total cost of the items in the list.
By showing the name of the item as a string, then rounding the cost to 
a whole dollar amount, and multiplying that by the tax rate, 
which will give the total cost of each item.
Then the cost with the tax of each item will be added 
together giving the total cost of the list.

"""

def calculate_total_cost(grocery_list: str, round_cost=False, tax= 0.8):
    total_cost = 0
    
    for item in grocery_list:
        cost = item["amount": int] * item["cost": float]
        total_cost += cost

    if round_cost:
        total_cost = round(total_cost)

    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost

    return total_cost


# export_items()
