from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_running = True
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_running:
    choices = menu.get_items()
    choice = input(f"What would you like? ({choices}): ")
    if choice == 'off':
        machine_running = False
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(choice):
            drink = menu.find_drink(choice)
            cost = drink.cost
            enough_resources = coffe_maker.is_resource_sufficient(drink)
            if enough_resources and money_machine.make_payment(cost):
                coffe_maker.make_coffee(drink)
        else:
            continue






