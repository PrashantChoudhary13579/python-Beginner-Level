# Pass by reference

# we can pass object to the funtion as a parameter
# we can also return from the function

class Customer:
    def __init__(self, name,gender):
        self.name = name
        self.gender = gender
    
def greet(customer):
    if customer.gender == "Male":
        print(f"Hello , {customer.name} sir. " )
    else:
        print(f"Hello , {customer.name} ma'am. " )

cust = Customer("Nitish","Male")
custo = Customer("Manjali", "Female")
# print(cust.name)
greet(cust)
greet(custo)