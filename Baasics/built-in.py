# Built-in functions
a = 5
val = pow(2,-3)
print(val)
print(pow(13,3))
print(min([3,5,6,8,4,2]))
print(max([3,5,6,8,4,2]))
print(max("kolkata"))
print(min("kolkata"))

print(round(22/7,2)) # gives the value by rounding off
print(divmod(10,3)) #gives two values 1st - integer value and 2nd is - modulus value
print(bin(50))
print(oct(50))
print(hex(50))
print(id(a)) # gives the memory location of the variable
print(ord('c')) # getting the ASCII values
print(len("delhi"))
print(sum([1,2,3,4,5,10]))
# help("modules")

# Built-in modules
import math
print(math.pi**2)
print(math.e)
print(math.factorial(5))
print(math.ceil(6.6))
print(math.floor(6.6))
print(math.acos(-1))
print(math.degrees(math.pi/2))
print(math.radians(90))
print(math.cbrt(64))
print(math.comb(5,2))
print(math.copysign(5.67,-10))
print(math.cos(1.57))
print(math.degrees(1)) # converting from radian to degree
print(math.exp(1))

import random
print("Random module")
print(random.randint(1,100)) # random value between 1 to 100
a = ([1,2,3,4,5,6,7,8])
# print(random.choice([1,2,3,4,5,6,7,8]))
random.shuffle(a)
print(a) # shuffling the list
print(random.random())
print(random.uniform(1.5,5.5))
colors = ['red','blue','green','yellow','pink','orange']
print(random.choice(colors))
print(random.sample(colors,3)) # random sample of 3 from the list
# print(random.choices(colors ,weights=[10,],k=2))
print(random.sample(a,k=4))
# print(random.seed(wre))

import time
print(time.time()) # gives the current time in seconds since 1st Jan 1970
print(time.ctime())
print("Hello")
# time.sleep(1)
print("World")
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import os
print(os.getcwd())
print(os.listdir())
# print(os.chmod())