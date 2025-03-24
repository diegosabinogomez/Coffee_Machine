import time

PEN = 0.01
NICK = 0.05
DIM = 0.1
QUA = 0.25

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
    "water": 250,
    "milk": 250,
    "coffee": 100,
    "Pennies": 200 ,
    "Nickels": 200,
    "Dimes": 200,
    "Quarters": 200,

}

# Coffee Machine Program Requirements are passed as "To Dos"
# todo 3: Print report.
def report():
    """prints the consumables and money"""
    money = resources["Pennies"] * PEN + resources["Nickels"] * NICK + resources["Dimes"] * DIM + resources["Quarters"] * QUA
    print(f"there are {resources['water']} ml of water\nThere are {resources['milk']} ml of milk\nThere are {resources['coffee']} g of coffe\nThere are {resources['Pennies']} Pennies\nThere are {resources['Nickels']} Nickels\nThere are {resources['Dimes']} Dimes\nThere are {resources['Quarters']} Quarters\nThere are {money} dollars")
    return

# todo 4: Check resources sufficient?
def check_resources(sort):
    """Checks if there are enough consumables"""
    if sort == "espresso":
        if MENU[sort]["ingredients"]["water"] <= resources["water"] and MENU[sort]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            print("Sorry, an ingredient or more are missing, we cannot prepare the drink")
            return False
    else:
        if MENU[sort]["ingredients"]["water"] <= resources["water"] and MENU[sort]["ingredients"]["coffee"] <= resources["coffee"] and MENU[sort]["ingredients"]["milk"] <= resources["milk"]:
            return True
        else:
            print("Sorry, an ingredient or more are missing, we cannot prepare the drink")
            return False

# todo 5: Process coins.
def insert_coins():
    """takes the coins and updates the dictionary resources"""
    # units = [Pennies, Nickels, Dimes, Quarters]
    units = [int(input("How many Pennies do you insert?\n")), int(input("How many Nickels do you insert?\n")),
             int(input("How many Dimes do you insert?\n")), int(input("How many Quarters do you insert?\n"))]
    resources["Pennies"] += units[0]
    resources["Nickels"] += units[1]
    resources["Dimes"] += units[2]
    resources["Quarters"] += units[3]
    return units

def refund(back):
    """manages the refund"""
    resources["Pennies"] -= back[0]
    resources["Nickels"] -= back[1]
    resources["Dimes"] -= back[2]
    resources["Quarters"] -= back[3]
    print("Your credit was not enough. Here you have your refund")
    return

# todo 7: Make Coffee.
def make_coffee(kind):
    """updates the dictionary resources due to consumables"""
    resources["water"] = resources["water"]-MENU[kind]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[kind]["ingredients"]["coffee"]
    if kind != "espresso":
        resources["milk"] = resources["milk"] - MENU[kind]["ingredients"]["milk"]
    print(f"Here is your {kind}. Enjoy!")

def process(coffee_type):
    """main process for the machine"""
    if check_resources(coffee_type):
        coins = insert_coins()
        credit = coins[0] * PEN + coins[1] * NICK + coins[2] * DIM + coins[3] * QUA
        print(f"You have inserted {credit} $")
        if credit < MENU[coffee_type]["cost"]:
            refund(coins)
            time.sleep(15)  # Sleep for 15 seconds
            return
        else:
            make_coffee(coffee_type)
            change = float(credit-MENU[coffee_type]["cost"])
            print(f"Your change is {round(change, 2)} $")
            time.sleep(15)
            return
    else:
        time.sleep(15)
        return

# todo 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

# todo 2: Turn off the Coffee Machine by entering “ off ” to the prompt.

# todo 6: Check transaction successful?
off = False # Machine is turned on
while not off:
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if choice.lower() == "off":
        print("Machine turns down")
        time.sleep(15)  # Sleep for 15 seconds
        off = True
    elif choice.lower() == "report":
        report()
        time.sleep(15)  # Sleep for 15 seconds
        choice = input("What would you like? (espresso/latte/cappuccino):\n")
    else:
        if choice.lower() in ["espresso", "latte", "cappuccino"]:
            print(f"Resources before transaction {resources}")
            process(choice)
            print(f"Resources after transaction {resources}")
        else:
            print("We dont have your selection, please choose anything else")
            time.sleep(15)

