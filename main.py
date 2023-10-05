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
    "coffee": 100
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

profit = 0


def insert_coins():
    """ returns the total amount coins inserted """

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = ((QUARTER * quarters) + (DIME * dimes) + (NICKLES * nickles) + (PENNIES * pennies))
    return total


def is_money_enough(payment, cost):
    """returns True when the payment is accepted, or False if money is insufficient"""
    global profit
    if cost >= payment:
        print(" Sorry that's not enough money. Money refunded.")
        return False
    else:
        profit += cost
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        return True


def resources_left(drink):
    """Returns amount of resources left after ordering a drink"""
    resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    return resources


def is_resource_sufficient(order_ingredients):
    """Return True when order can be made. False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there's not enough {item}")
            return False
    return True


thirsty = True
while thirsty:
    answer = input("what would you like? (espresso/latte/cappuccino): ").lower()

    if answer == "off":
        print(f"Coffee machine needs some rest. MACHINE {answer}")
        thirsty = False
    elif answer == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"money: ${profit}")
    else:
        if is_resource_sufficient(MENU[answer]["ingredients"]) and is_money_enough(insert_coins(), MENU[answer]["cost"]):
            resources_left(answer)
            print(f"Here is your {answer} Enjoy!")
