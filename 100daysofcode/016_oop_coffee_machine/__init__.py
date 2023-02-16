from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    option = input(f"What would you like? ({menu.get_items()}): ")

    if option == "off":
        break

    if option == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    drink = menu.find_drink(option)

    if (
        drink is not None
        and coffee_maker.is_resource_sufficient(drink)
        and money_machine.make_payment(drink.cost)
    ):
        coffee_maker.make_coffee(drink)
