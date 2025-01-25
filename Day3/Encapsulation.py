# Instance variable are those variables whose values are different for each object.

# Making the class data as private by using double underscore before the variable name.
# We can access those variables in class methods but not outside the class



class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
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
        self.__pin = int(input("Enter your pin"))
        print("Pin created successfully")
        

    def deposit(self):
        self.temp = int(input("Enter your pin"))
        if (self.temp == self.__pin):
            amount = int(input("Enter deposit amount"))
            self.__balance += amount
            print("Amount deposited Successfully ")
        else:
            print("Invalid pin")
        
    
    def withdraw(self):
        self.temp = int(input("Enter your pin"))
        if(self.temp == self.__pin):
            amount = int (input("Enter withdraw amount"))
            self.__balance -= amount
            print("Amount withdraw Successfully")
        else:
            print("Invalid pin")
        
    
    def check_balance(self):
        self.temp = int(input("Enter your pin"))
        if(self.temp == self.__pin):
            print(f"Balance amouont : {self.__balance}")
        else:
            print("Invalid pin")
        
    
    def exiting(self):
        print("Exiting the system")
        exit()


sbi = Atm()
