# while loop

# num = int(input("Enter a number"))
# i = 1
# while i<11:
#     print(num *i)
#     i +=1

# for loop
# start, stop, step(gap)
# print(list(range(11,-12,-2)))

for i in range(1,11,2):
    print(i)

for i in "Uttarakhand":
    print(i)

for i in [1,2,3,4]:
    print(i)

for i in {2,46,76,4,3}:
    print(i)

# nested loop
# rows = int(input("Enter the number of rows")) +1
# for i in range(rows):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")

# break - terminate the loop
# continue - skip the loop iteration
# pass - pass that value
for i in range(1,11):
    if i == 2:
        continue
    print(i)
