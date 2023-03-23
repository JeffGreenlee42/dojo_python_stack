from Bank_Account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.4, 0)
        self.accounts = {"Checking": self.account}

    def display_info(self):
        print(f"Name: {self.name}\n"
            f"Email: {self.email}\n")
        return self

    def make_deposit(self, amount, account_name):
        if not account_name in self.accounts.keys():
            print("Invalid Accounts name")
        else:
            self.accounts[account_name].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_name):
        if not account_name in self.accounts.keys():
            print("Invalid Accounts name")
        else:
            self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"The Account balance(s) for {self.name} is:")
        for key, val in self.accounts.items():  
            print(f"{key}: {val.balance}")
        return self

    def add_account(self, account_name):
        if account_name in self.accounts.keys():
            print("New account name already exists: Please use a different name.")
        else:
            self.accounts[account_name] = BankAccount(0.04, 0)
        return self

    def transfer_money(self, amount, other_user):
        if other_user:
            self.make_withdrawal(amount, "Checking")
            other_user.make_deposit(amount, "Checking")
        else:
            print("Other_User does not exist")

bob = User("Bob Godhead", "god1@gmail.com")
nancy = User("Nancy Goofball", "ngoofball@clownuniversity.edu") 

bob.make_deposit(1000, "Checking")
nancy.make_deposit(3000, "Checking")


bob.display_info()
bob.display_user_balance()

nancy.display_info()
nancy.display_user_balance()

bob.transfer_money(100, nancy)

bob.display_user_balance()
nancy.display_user_balance()

# user1.make_deposit(20, "Checking")
# user1.make_withdrawal(5, "Checking")
# user1.display_user_balance()



