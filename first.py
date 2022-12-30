# This script ram on a python machine
import os
# Determine which product is cheaper from a list of options

# create an empty dictionary
bids = {}
shopping_finished = False

def find_affordable_shop(shopping_record):
    """takes a dictionary of shopping records as an argument and determines which shop has the lowest price for a product"""
    lowest_price = price
    winner = ""
    for shop in shopping_record:
        bid_amount = shopping_record[shop]
        if bid_amount < lowest_price:
            lowest_price = bid_amount
            winner = shop
    os.system('clear')
    print(f"The most affordable is {winner} with a price of M{lowest_price}")

while not shopping_finished:
    name = input("Where to shop?: ")
    price = int(input(f"Price of a product in {name}?: "))
    bids[name] = price
    should_continue = input("Shop again? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        shopping_finished = True
        find_affordable_shop(bids)
    elif should_continue == "yes":

        os.system('clear')