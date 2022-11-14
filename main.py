from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
a = Menu()

Coffee = CoffeeMaker()
Money = MoneyMachine()
items = Menu()
is_on = True
while is_on:
    user_choice = input("what would you like to order" + a.get_items())
    if user_choice == "report":
        Coffee.report()
        Money.report()
    elif user_choice == "off":
        is_on = False
    else:
        drink = items.find_drink(user_choice)
        if Coffee.is_resource_sufficient(drink):
            if Money.make_payment(drink.cost):
                Coffee.make_coffee(drink)



