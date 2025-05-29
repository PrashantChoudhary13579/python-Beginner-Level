# string
name ="Tony Stark"
print(name.upper())
print(name.lower())
print(name.find('t'))
print(name.count('t'))

print("stark" in name)

# Arithmetic operator +,-,*,/,%, // - remove the value after decimal
# ** power
print(5**4 )
# precedence , +,*, -, /.
result = 5*10/6
print(result)

# Comments- two types - 
# here is a comment
"""
This is also a comment
"""
# Comparision operator
print(4>3)
print(4>=3)
print(4<3)
print(4<=3)

age = 13
if age>= 18:
    print("You are an adult")
    print("You can vote")
elif age<18 and age> 3:
    print("you are in school")
else:
    print("You are a kid")
print("Thank you")