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

COIN_MAPPING = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

isFinish = False
acc_money = 0


def show_report():
    for resource in resources:
        unit = 'ml'
        if resource == 'coffee':
            unit = 'g'
        print(f"{resource.capitalize()}: {resources[resource]}{unit}")

    print(f"Money: ${acc_money}")


def check_resources(drink: str):
    ingredients = MENU.get(drink).get("ingredients")
    for ingredient in ingredients:
        if resources.get(ingredient) < ingredients.get(ingredient):
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def deduct_resources(drink: str):
    global resources
    ingredients = MENU.get(drink).get("ingredients")
    for ingredient in ingredients:
        resources[ingredient] -= ingredients.get(ingredient)


def trade(drink: str):
    global acc_money
    cost = MENU.get(drink).get('cost')
    current = 0

    for coin in COIN_MAPPING:
        amount = input(f"How many {coin}({COIN_MAPPING.get(coin)})?:")
        current = round(current + int(amount) * COIN_MAPPING.get(coin), 2)
        print(current)

    difference = current - cost
    result = difference >= 0

    if result:
        acc_money += cost
    else:
        print("Sorry that's not enough money. Money refunded.")

    if difference > 0:
        print(f"Here is ${round(current - cost, 2)} dollars in change.")

    return result


def start():
    global isFinish
    prompt = input("What would you like? (espresso/latte/cappuccino):")

    if prompt == "off":
        isFinish = True

    elif prompt == "report":
        show_report()

    elif prompt in MENU.keys():
        deduct_resources(prompt)

    else:
        print("Not valid input")


while not isFinish:
    start()

