# For loop
# for number in range(1,4):
#     print("attempted", number, number * ".")

# for-else loop
# sucessfull = False
# for number in range(1,4):
#     print("Attempt",number * ".")
#     if sucessfull:
#         print("it is sucessfull")
#         break
# else:
#         print("Not sucessfull")

# nested loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")
# for x in "python":
#     print(x)


# While loop
# number = 100
# while number>0:
#     print(number)
#     number //=2

# command =""
#
# while command.upper() != "ANKUSH":
#     command = input("Enter value")
#     print("ECHO",command)

# Even numbers excercise
# count=0
# for i in range(1,11):
#     if i%2==0:
#         count=count+1
#         print(i)
# print((f"We have {count} even numbers"))

# import random
# choices=["ankush","avi","ishi"]
# leader=random.choice(choices)
# print(leader)

import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
