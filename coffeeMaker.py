from menu import MenuItem


class CoffeeMaker:
    """Coffee machine class"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        for resource in self.resources:
            print(f"{resource} : {self.resources[resource]} ml/g")

    def is_resource_sufficient(self, drink):
        for resource in self.resources:
            if self.resources[resource] < drink.ingredients[resource]:
                print (f"Sorry there is not enough {resource}")
                return False
        return True

    def make_coffee(self, order):
        for resource in self.resources:
            self.resources[resource] -= order.ingredients[resource]
        print(f"Here's your {order.name}. Enjoy!😀")


