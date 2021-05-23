import ProceduralMachine
from coffeeMaker import CoffeeMaker
from moneyHandler import MoneyMachine
from menu import MenuItem, Menu

ProceduralMachine.print_menu()

cashier = MoneyMachine()
drink_menu = Menu()
coffee_machine = CoffeeMaker()

while True:
    user_choice = input("What would you like? Or type menu to see costs (espresso/ latte/ cappuccino) : ").lower()
    if user_choice == "off":
        break
    elif user_choice == "report":
        coffee_machine.report()
        cashier.report()
        continue
    elif user_choice == "menu":
        ProceduralMachine.print_menu()
        continue

    drink = drink_menu.find_drink(user_choice)
    if drink is None:
        print("Please try again later")
        continue

    enough_resource = coffee_machine.is_resource_sufficient(drink)
    if not enough_resource:
        continue

    payment_done = cashier.make_payment(drink.cost)

    if not payment_done:
        continue

    coffee_machine.make_coffee(drink)


