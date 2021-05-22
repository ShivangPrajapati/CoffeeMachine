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

machine_money = 0.00


def print_menu():
    for drink in MENU:
        print(f"{drink} : $ {MENU[drink]['cost']}")


def print_report():
    for resource in resources:
        print(f"{resource} : {resources[resource]} ml/g")
    print(f"Money : $ {machine_money}")


def is_enough_resources(drink):
    resources_needed = MENU[drink]["ingredients"]
    for resource in resources_needed:
        if resources_needed[resource] > resources[resource]:
            print(f"Sorry there is not enough {resources[resource]}")
            return False
    return True


def count_total(quarter_c, dime_c, nickle_c, pennies_c):
    total = 0.00
    total = 0.25*quarter_c + 0.10*dime_c + 0.05*nickle_c + 0.01*pennies_c
    return round(total, 2)


def is_enough_money(drink, paid_amount):
    if paid_amount >= MENU[drink]["cost"]:
        return True
    else:
        return False


def calculate_change(drink, paid_amount):
    change = paid_amount - MENU[drink]["cost"]
    return round(change, 2)


def make_drink(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]

def start_machine():
    global machine_money
    while True:
        user_choice = input("What would you like? Or type menu to see costs (espresso/ latte/ cappuccino) : ").lower()
        if user_choice == "off":
            break
        elif user_choice == "report":
            print_report()
            continue
        elif user_choice == "menu":
            print_menu()
            continue
        elif user_choice != "espresso" and user_choice != "latte" and user_choice != "cappuccino":
            print("Please enter proper drink")
            continue

        enough_resources = is_enough_resources(user_choice)
        if not enough_resources:
            continue
        quarter = int(input("How many quarters? "))
        dime = int(input("How many dimes? "))
        nickle = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        total_amount = count_total(quarter, dime, nickle, pennies)

        enough_money = is_enough_money(user_choice, total_amount)

        if not enough_money:
            print("Sorry that's not enough money. Money refunded. Please try again")
            continue

        change = calculate_change(user_choice, total_amount)
        machine_money = machine_money + total_amount - change
        if change > 0:
            print(f"Here's your $ {change} change")

        make_drink(user_choice)

        print(f"Here's your {user_choice}. Enjoy!!😀")
    return


