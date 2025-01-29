# printing different data types 
print("Hello  world")
print(5)
print(6.8)
print(False)
print("India","USA","Australia")
print("India","USA","Australia",sep = "/",end = " -  ")
print("India","USA","Australia")

# integer
print(1.7e308)
# boolean
print(True)
print(False)

# complex
print("Complex",4 +5j)

# printing in different quotes
print("India")
print('India')
print("""Inida""")


# list
print([1,2,3,4,5])

# tuple
print((1,4,3,2))

# sets
print({1,2,3,4,5})

# dictionary
print({
    "name" : "Rahul",
    "age" : 25,
    "city" : "India",
    "Gender": "Male"
})

# comments - two type - single line -- multi line

# Declaring variables
name = 'Prashant'
print(name)
age = 24
print(age)
Topper = False
print(Topper)
# Dynamic typing - no need to specify the data types the datatype of your variables 
# static typing - specifying the data types for your variable

print(name)
name = "Choudhary"
age = "Gujjar"
print(name, age)
# Dynamic Binding  - variable name can be changed at runtime (a variable can change it's value from int to string to float to boolean etc)
# Static Binding - variable name cannot be changed at runtime (a variable can't change it's datatype from int to string to float to boolean etc)

# special syntax
a = 5;b = 6; c = 7
print(a,b,c)
a , b, c = 1,2,3
print(a,b,c)
a = b= c = 10
print(a,b,c)

# keywords
# and, as, assert, break, class, continue, def, del, elif, else, etc.
#  there are 33 keywords
import keyword
print(keyword.kwlist)

name = "suraj"
_ladla = "Bhati"
next_level = "mukul"
print(name, _ladla, next_level)

first_num = int(input("Enter the first number : "))
second_num = int(input("Enter the second number : "))
print(first_num)
print(second_num)
print("Total sum ",first_num + second_num)
# by applying int in the starting we can get the data in integer else the data will come in the form of string

# Type 
print(type(4.5))
print(type(True))
print(type(6+7j))
print(type(3))
print(type("start"))
print(type("65"))
print(type([3,4,5]))
print(type((3,4,)))


print("Hello world")
val = input("Enter your name")
print(val)
