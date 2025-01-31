# Guessing the jackpot number - if the user guesses the jackpot number, they win the jackpot
# Code will help to reach to the jackpot number by incrementing or decrementing the value

import random 
val = random.randint(1,100)
# print(val)

guess = int(input("Guess the jackpot number"))
count = 1
while guess != val:
    if guess<val:
        print("Guess higher")
        
    else:
        print("Guess lower")

    guess = int(input("Guess a jackpot number"))
    count += 1

print("You have reached the jackpot number")  
# This line will be printed when the user guesses
print("Guessing took",count,"attempt")