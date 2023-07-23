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
}


def show_report():
    for p in resources:
        print(f"{p.capitalize()}: {resources[p]}")


# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
isFinish = False

while not isFinish:
    prompt = input("What would you like? (espresso/latte/cappuccino):")

    if prompt == "off":
        isFinish = True

    elif prompt == "report":
        show_report()

    elif prompt == "espresso":
        print("espresso")
    elif prompt == "latte":
        print("latte")
    elif prompt == "cappuccino":
        print("cappuccino")

    else:
        print("Not valid input")
