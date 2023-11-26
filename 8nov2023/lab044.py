class BankAccount:
    def __init__(self):
        self.balance = 0  # Instance variable (you can access via object ref.)

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount):
        self.balance -= amount

    def __showbalance(self):
        print("Your balance:", self.balance)

    def IS_Auth_True_show_balance(self, isAuth):
        if isAuth:
            self.__showbalance()
        else:
            print("You are not Auth")

    def do_withdraw_by_user(self, amount):
        self._withdraw(amount=amount)


jp_chase = BankAccount()
jp_chase.deposit(1000)
# jp_chase._withdraw(499) #not good practice

jp_chase.IS_Auth_True_show_balance(True)
jp_chase.do_withdraw_by_user(400)
# print("show balance after withdraw:",\
jp_chase.IS_Auth_True_show_balance(True)
