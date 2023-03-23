from Bank_Account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.4, 0)

    def display_info(self):
        print(f"Name: {self.name}\n"
            f"Email: {self.email}\n")
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)


user1 = User("Jeff", "banjo1@gmail.com")

user1.make_deposit(20)
user1.make_withdrawal(5)
print(user1.account.balance)


