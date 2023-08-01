from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_finish = False

coffee_maker = CoffeeMaker()
money_store = MoneyMachine()
menu = Menu()


def start():
    global is_finish
    prompt = input("What would you like? (espresso/latte/cappuccino):")

    if prompt == "off":
        is_finish = True

    elif prompt == "report":
        coffee_maker.report()
        money_store.report()

    else:
        drink = menu.find_drink(prompt)

        if not drink:
            return
        if not coffee_maker.is_resource_sufficient(drink):
            return
        if not money_store.make_payment(drink.cost):
            return

        coffee_maker.make_coffee(drink)


while not is_finish:
    start()

