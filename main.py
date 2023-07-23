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


def check_resources(drink: str):
    target = MENU.get(drink)
    if not target:
        return False

    ingredients = target.get("ingredients")
    for p in ingredients:
        if resources.get(p) < ingredients.get(p):
            return False
    return True


isFinish = False


def start():
    global isFinish
    prompt = input("What would you like? (espresso/latte/cappuccino):")

    if prompt == "off":
        isFinish = True

    elif prompt == "report":
        show_report()

    elif prompt in MENU.keys():
        print(check_resources(prompt))

    else:
        print("Not valid input")


while not isFinish:
    start()

