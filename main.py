MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# TODO: ask the user what they would like (espresso/latte/cappuccino)

# TODO: when user inputs off the coffee machine should end execution

# TODO: when user enters 'report' a report should be generated

# TODO: check resources sufficient

# TODO: Process coins

# TODO: Check transaction successful

# TODO: Make coffee

QUARTER = 0.25
DIME = 0.10
NICKLES = 0.05
PENNIES = 0.01


def insert_coins(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = round(
        (((QUARTER * quarters) + (DIME * dimes) + (NICKLES * nickles) + (PENNIES * pennies)) - MENU[drink]["cost"]), 2)
    resources["money"] += total
    return total


order = True
while order:
    answer = input("what would you like? (espresso/latte/cappuccino): ").lower()

    if answer == "espresso":
        print(f"Here is ${insert_coins(answer)} in change. \nHere is your {answer} Enjoy!")
    elif answer == "latte":
        print(f"Here is ${insert_coins(answer)} in change. \nHere is your {answer} Enjoy!")
    elif answer == "cappuccino":
        print(f"Here is ${insert_coins(answer)} in change. \nHere is your {answer} Enjoy!")
    elif answer == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
    elif answer == "off":
        print(f"Coffee machine needs some rest. MACHINE {answer}")
        order = False
