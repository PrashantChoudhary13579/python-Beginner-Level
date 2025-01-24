# Developing the atm machine again

class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):

        choice = int(input ("""Hello , How would you like to proceed ?
               1. Enter 1 to create pin
               2. Enter 2 to deposit 
               3. Enter 3 to withdraw
               4. Enter 4 to check balance
               5. Enter 5 to exit \n"""))
        
        if(choice == 1):
            self.create_pin()
        elif(choice == 2):
            self.deposit()
        elif(choice == 3):
            self.withdraw()
        elif(choice == 4):
            self.check_balance()
        elif(choice == 5):
            self.exiting()
        else:
            print("Invalid choice , please try again")
            # self.menu()

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin created successfully")
        self.menu()

    def deposit(self):
        self.temp = input("Enter your pin")
        if (self.temp == self.pin):
            amount = int(input("Enter deposit amount"))
            self.balance += amount
            print("Amount deposited Successfully ")
        else:
            print("Invalid pin")
        self.menu()
    
    def withdraw(self):
        self.temp = input("Enter your pin")
        if(self.temp == self.pin):
            amount = int (input("Enter withdraw amount"))
            self.balance -= amount
            print("Amount withdraw Successfully")
        else:
            print("Invalid pin")
        self.menu()
    
    def check_balance(self):
        self.temp = input("Enter your pin")
        if(self.temp == self.pin):
            print(f"Balance amouont : {self.balance}")
        else:
            print("Invalid pin")
        self.menu()
    
    def exiting(self):
        print("Exiting the system")
        exit()


sbi = Atm()

# now it is working proper.
# If you want to get the python idle format then 
# Enter any number except those which are having certain application
#