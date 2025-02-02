# String is a collection of characters which are joined together to interact with the users
# This is done basically for the user interaction
# String is not found in C/C++ languages because these do not interact with the user they interact with the hardware where we don't need to have such things.
# Machines only understand the binary codes.

# Creating Strings
c = 'Hello'
print(c)
d = "It's raining outside"
print(d)
e ="""Learning something
which is amazing in python
so what do you thing it is good to learn or not?"""
print(e)
c = str('Learning Python')
print(c)

# Accessing Strings

# Indexing
# Positive indexing
print(c[0])
print(c[1])
print(c[2])
print(c[3])
# Negative indexing
print(c[-1])
print(c[-2])
print(c[-3])
print(c[-4])
print(len(c))

# slicing  - getting a range from the string
print(c[:5])
print(c[5:])
print(c[:])
print(c[0:15:2])
print(c[0:15:3])
print(c[-15:-1:2])
print(c[::-1]) # reversing the string
print(c[-1:-(len(c)+1):-1])
print(c[-1])
print(c[-8:])
print(c[:-8])
print(c[:])
print(c[-9:-2])
# Adding Chars to Strings
print("\n")
# Editing Strings
s = "Prashant"
print(s)
# s[0] ="X"
# Strings are immutable in python
s = "Choudhary"
print(s)
# we can reassign the string in python but we can't further add on to the string

# Deleting Strings
del s
# print(s)

s = "hello"
print(s)
# del s[0]
print(s)
# we can't delete the single character from the string as string are immutable 


# Operations on Strings

# Arithmetic operations (+,*)
a = "Prashant"
b = "Choudhary"
print(a+" - "+b)
print("*/*%"*5)

# Relational operations
print( a == b)
print("Prashant" == a)
print(a != b)
print("Mumbai" > "Pune") # comparison is done with the help of Lexiographically (acc. to the dictionary)
print("Goa"<"goa") # capital letter phele aate h 

# Logical operations

#    "" -> False      and     "fdsiofs" -> True
print(bool(""))
print(bool("asdfjkl;"))
print("Prashant" and "Choudhary")   # 1 and 1 
# then it become true and it print last value of 1
print("" and "Choudhary") # 0 and 1 -> 0
print("Prashant" and "") # 1 and 0 -> 0
print("Prashant" or "Choudhary")
print("" or "Choudhary")
print("Prashant" or "")
print(not "Prashant")
print(not "")

# Loops
c = "Nikhil Mishra"
for i in c:
    print(i)
for i in c[::-1]:
    print(i)

# membership operator
print("sh" in c)
print("ant" not in c)


# String Functions

# Common functions - len, max, min, sorted
c = "What have you learn till now"
print(len(c))
print(max(c))
print(min(c))
print(sorted(c,reverse=True))
print(sorted(c))

d = "Here we are learning python"
print(d.capitalize())
print(d.title()) # each word letter is capital
print(d.upper())
print(d.lower())
e = "PrAShaNT"
print(e.swapcase())
print(d.count('e'))
print(d.find('k')) # return -1
print(d.find('p')) 
print(d.index('r'))
# print(d.index('p')) # gives an error 

print(d.endswith('ur'))
print(d.endswith('nt'))
print(e.startswith('pr'))
print(e.startswith('Pr'))

# format
y = "Hello my name is {} and I am {}"
print(y.format("Prashant",20))
# Used in profile where the name of the user comes after login

# changing the index
y = "Hello my name is {1} and I am {0}"
print(y.format("Prashant",20))
# changing through variables
y = "Hello my name is {name} and I am {age}"
print(y.format(name = "PRashant", age = 20))
