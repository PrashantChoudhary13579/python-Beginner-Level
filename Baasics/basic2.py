# Type conversion
# implicit - done by the external user 
# explicit - done by the compiler automatically 

print(5+ 6+7j)
print( 4+6.7)

# for explicit type conversion we are having some fn to convert it's data type
print(int('45'))
print(float('45'))
s = 45
print(str(s))  # converting integer to string
print(type(str(s)))
print(list('Hello'))

# type conversion is not a permanent change 
# type casting is the permanent change

# Literal - assigning the values to the variables

a = 0b1010  # works in raspberry pi 
print(a)
b = 0x2a
c = 0o510
print(b)
print(c)

float_1  = 10.5
print(float_1)  # 10.5
float_2 = 1.5e2
float_3 = 1.7e-3
print(float_2)
print(float_3)

x = 5+ 33.14j
print(x)  # 33.14j
print(x.imag, x.real)
print(type(x.imag))

# String
unicode = u"\U0001F600\U0001F923"
raw_str = r"raw \n string"
print(unicode)
print(raw_str)

# boolean
a = True + 4
b = False +10
print("a :",a )
print("b :",b)

# special
a = None
print(a)

c = 45+45
print(c)
asb = None # for variable declaration
print(asb)

# Operator
# Arithmetic Operators
x = 5 
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)# integer division

# comparison operators
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)

# logical operators
x = True
y = False
print(x and y)
print(x or y)
print(not y)

# Bitwise operators - works upon binary values
x = 20
y = 30
print(x & y)
print(x | y)
print(x >> 2)
print(x << 2)
print(~x)

# Assignment operators
a = 3
print(a)
a += 3
print(a)
a -= 2
print(a)
a *= 10
print(a)
a **= 1
print(a)
a &= 30
print(a)


# Identity operators - tells whether 2 things are on the same memory location or not
a = 3
b = 3
print( a is b )

a = [1,2,3]
b = [1,2,3]
print(a is b)

# Membership operators - tell us whether it(word/letter) is present in the string/file/dict/list etc
x = "Delhi"
print("D" in x)
print("D" not in x)
