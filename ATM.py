class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details : ")
        print(f"Name: {self.name} , Age: {self.age} , Gender: {self.gender}")

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Account balance has been updated : {self.balance} Rupay")

    def withdraw(self, amount):
        self.amount = amount
        if self.balance < self.amount:
            print(f"Insuffficient funds ! Balance available : {self.balance} Rupay")
        else:
            self.balance -= self.amount
            print(f"Account balance has been updated : {self.balance} Rupay")

    def view_balance(self):
        self.show_details()
        print(f"Account balance : {self.balance} Rupay")

user1 = Bank("sachin", 22, "Male")
user1.deposit(100)
user1.withdraw(20)
user1.view_balance()