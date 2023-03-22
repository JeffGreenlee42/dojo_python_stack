class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Email: {self.email}\n"
            f"Age: {self.age}\n"
            f"Is Rewards Member: {self.is_rewards_member}\n"
            f"Gold Card Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member:
            print(f"User {self.first_name} {self.last_name} is already an enrolled member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"The spend amount exceeds the available Gold Card Points for {self.first_name} {self.last_name}")
        return self

user_1 = User("John", "Doe", "john.doe@dead.com", 25)

user_1.display_info()

user_1.enroll()
print("--------------------------------------\n")
user_1.display_info()

user_2 = User("Susan", "Collins", "suecol@hotmail.com", 54)

user_3 = User("Micky", "Mouse", "mmouse@gmail.com", 85)

user_1.spend_points(50)

user_2.enroll()

user_2.spend_points(80)

user_1.display_info()
print("--------------------------------------\n")
user_2.display_info()
print("--------------------------------------\n")
user_3.display_info()
print("--------------------------------------\n")

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user
user_1.enroll()
# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
user_3.spend_points(40)

