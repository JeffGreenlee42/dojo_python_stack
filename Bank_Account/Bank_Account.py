class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # add account to Class accounts
        BankAccount.addAccount(self)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}\n"
        f"Account Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def addAccount(cls, account):
        cls.accounts.append(account)


account_1 = BankAccount(0.09, 0)

account_2 = BankAccount(0.11, 0)

account_1.deposit(1050).deposit(200).deposit(1000).withdraw(1000).yield_interest().display_account_info()
account_2.deposit(500.00).deposit(700).withdraw(10).withdraw(100).withdraw(300).withdraw(400).yield_interest().display_account_info()

print(BankAccount.accounts)




