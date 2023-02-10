INITIAL_WATER = 300
INITIAL_MILK = 200
INITIAL_COFFEE = 100


class CoffeeMachine:
    coffee_list = {
        "espresso": {
            "price": 1.0,
            "water_ml": 50,
            "coffee_mg": 15,
            "milk_ml": 0,
        },
        "latte": {
            "price": 1.80,
            "water_ml": 200,
            "coffee_mg": 24,
            "milk_ml": 150,
        },
        "cappuccino": {
            "price": 1.50,
            "water_ml": 250,
            "coffee_mg": 24,
            "milk_ml": 100,
        },
    }

    def __init__(
        self,
        water: int = INITIAL_WATER,
        coffee: int = INITIAL_COFFEE,
        milk: int = INITIAL_MILK,
    ):
        self.water_ml = water
        self.coffee_mg = coffee
        self.milk_ml = milk
        self.money = 0

    def refill(self):
        self.water_ml = INITIAL_WATER
        self.coffee_mg = INITIAL_COFFEE
        self.milk_ml = INITIAL_MILK

    def print_report(self):
        print(f"Water:  {self.water_ml} ml")
        print(f"Coffee: {self.coffee_mg} mg")
        print(f"Milk:   {self.milk_ml} ml")
        print(f"Money:  ${self.money:.2f}")

    def get_coffee_option(self, option: str) -> dict:
        return self.coffee_list[option]

    def enough_resources(self, coffee_option: dict):
        if coffee_option["water_ml"] > self.water_ml:
            return "water"
        elif coffee_option["coffee_mg"] > self.coffee_mg:
            return "coffee"
        elif coffee_option["milk_ml"] > self.milk_ml:
            return "milk"

    def enough_money(self, option: str, money: float):
        return self.coffee_list[option]["price"] <= money

    def make_coffee(self, option: str):
        coffee = self.coffee_list[option]

        self.money += coffee["price"]

        self.water_ml -= coffee["water_ml"]
        self.coffee_mg -= coffee["coffee_mg"]
        self.milk_ml -= coffee["milk_ml"]


coffee_machine = CoffeeMachine()

while True:
    option = input("What would you like? (espresso/latte/cappuccino): ")

    if option == "off":
        exit()

    if option == "report":
        coffee_machine.print_report()
        continue

    if option == "refill":
        coffee_machine.refill()
        continue

    if not (coffee_option := coffee_machine.get_coffee_option(option)):
        print(f"There is no such option.")

    if insufficient := coffee_machine.enough_resources(coffee_option):
        print(f"Sorry, there is not enough {insufficient}")
        continue

    money = int(input("How many quarters? ")) * 0.25
    money += int(input("How many dimes? ")) * 0.1
    money += int(input("How many nickels? ")) * 0.05
    money += int(input("How many pennies? ")) * 0.01

    if money < coffee_option["price"]:
        print(f"Sorry, there is not enough money. Money refunded.")
        continue

    if change := (money - coffee_option["price"]):
        print(f"Here is ${change:.2f} in change.")

    coffee_machine.make_coffee(option)

    print(f"Here is your {option}. Enjoy!")
