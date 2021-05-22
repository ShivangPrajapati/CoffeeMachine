class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.money_received = 0
        self.coins = {
            "quarter": 0.25,
            "dime": 0.10,
            "nickle": 0.05,
            "pennie": 0.01
        }

    def report(self):
        print(f"Money : $ {self.profit}")

    def make_payment(self, cost):
        for coin in self.coins:
            self.money_received += self.coins[coin]*int(input(f"How many {coin}? "))

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is your ${change} change")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            self.money_received = 0
            print("Sorry, that's not enough money. Please try again")
            return False
