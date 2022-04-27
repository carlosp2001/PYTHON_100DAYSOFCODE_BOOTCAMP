from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    user_item = input(f"What would you like to to order {menu.get_items()}? ").lower()
    if user_item == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_item == 'off':
        is_on = False
    else:
        user_item = menu.find_drink(user_item)
        if coffee_maker.is_resource_sufficient(user_item):
            if money_machine.make_payment(user_item.cost):
                coffee_maker.make_coffee(user_item)



