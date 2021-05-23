class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    
    # methods

    def deposit(self, amount):
        self.amount += amount
        print("Amount of {} added to {}".format(amount, self.category))

    def balance(self):
        return self.amount

    def check_balance(self, amount):
        if self.amount < amount:
            return False

        return True

    def withdraw(self, amount):
        if self.check_balance:
            self.amount -= amount
            print("insufficient funds")
        else:
            return "Transaction failed"

    def transfer(self, amount, category):
        if not self.check_balance(amount):
            return "Not successful"

        self.amount -= amount
        category.amount += amount
        return "Transfer successful"
        

    
Instance = Category("Food", 500)
Instance1 = Category("Car", 400)

Instance.deposit(600)
print("Your balance is " + str(Instance.balance()))
Instance.transfer(400, Instance1)
