# first = int(input("enter first number:"))
# second = int(input("enter second number:"))
# result = first * second
# print(result)

# to print sum of current and previous number in iteration
# n = 10
# current = 0
# for i in range(n+1):
#     sum = i+current
#     print(sum)
#     current = i

# to print even string & index wise

# lst = ("pynative")
# # print(lst[0::2])
# print(lst[4:])
# comparing last index

# def frst_last_same(number_list):
#     last_number = number_list[-1]
#     first_number = number_list[0]
#     if first_number == last_number:
#         return True
#     else:
#         return False
#
#
# a=frst_last_same([2,3,4,5,6])
# print(a)
#
# Print number divisible  by 5
# numbers = [2, 3, 4, 5, 8, 12, 24, 23, 56, 67]
# lst = []
#
# def division(numbers):
#     for n in numbers:
#         if n % 2 == 0:
#             print(f"{n} is divisible by 2")
#             lst.append(n)
#     print(f"list of no. divisible by 2 {lst}")
#
#
# d = division(numbers)

# count method

# str = "Ankush is my name, Ankush is fame,ok ok ok ok hello ankush"
# str = str.lower()
# cnt = str.count("Ankush")
# print(cnt)

# Pattern

# for number in range(1,6):
#     for i in range(number):
#
#         print(number,end="")
#     print("\n")

# palindrome

# num = 121
# temp = num
# sum = 0
# while num > 0:
#     r = num % 10
#     sum = sum*10 + r
#     num = num//10
#     if sum == temp:
#         print("no.is palindrome")/////////////////////////////////////////////////
#     else:
#          print("not palindrome")

# append in list

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# list_result = []
# for lst in list1:
#     if lst%2 != 0:
#         list_result.append(lst)
#
# for ls in list2:
#     if ls%2 == 0:
#         list_result.append(ls)
#
# print(list_result)
#
# table----------------------------------------------------
#
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end ="  ")
#     print("\n")

#pattern
# for i in range(6,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print(" ")


# Exponent and base
# def exponent(base,exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num-1
#     print(result)
#
#
# exponent(3, 3)

#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print("")

# inheritance-------------------------------------------------------

class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def printname(self):
        print(self.first_name,self.last_name)

# a=Person("Ankush","Minocha")
# a.printname()


class Student(Person):
    def student(self):
        pass


x = Student("Ankush","Minocha")
x.printname()