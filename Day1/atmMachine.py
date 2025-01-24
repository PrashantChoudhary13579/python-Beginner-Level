# Making atm software

class Atm:
    #  functions inside the class -> methods

    # This __init__ is a constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        print(id(self))
    
    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed ?
               1. Enter 1 to create pin
               2. Enter 2 to deposit
               3. Enter 3 to withdraw
               4. Enter 4 to check balance 
               5. Enter 5 to exit""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            self.exit()
    
    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set Successfully")

    def deposit(self):
        self.temp = input("Enter your pin")
        if self.temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        self.temp = input("Enter your pin")
        if self.temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw"))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw Successfully")
            else:
                print("Insufficient balance")
        else:
            print("Invalid Pin")

    def check_balance(self):
        self.temp = input("Enter your pin")
        if self.temp == self.pin :
            print(f"Total Balance: {self.balance} ")
        else:
            print("Invalid Pin")
    
    def exit(self):
        return
sbi = Atm()
