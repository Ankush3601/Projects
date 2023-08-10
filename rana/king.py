# stu=input("Enter string")
#
# cntspc=0
# cntdig=0
# cntvow=0
# for num in stu:
#  if num==" ":
#      cntspc+= 1
#  elif num>=str(0) and num<=str(9):
#      cntdig+= 1
#  elif num in ("a","e","i","o","u"):
#      cntvow+=1
# print(f"spaces : {cntspc}")
# print(f"digits : {cntdig}")
# print(f"vowels : {cntvow}")
# __________________________________________________________________________________________
# n=int(input("Enter number to check "))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# if(temp==sum):
#     print("palindrome")
# else:
#     print("not palindrome")


# ---------------------------------------------------------------------------------------

# first = int(input("Enter first number: "))
# choice = input("Enter operator choice(+,-,/,*,% )")
# second = int(input("Enter second number: "))
# if choice=="+":
#     print(f"result is:{first+second}")
# elif choice=="-":
#     print(f"result is:{first - second}")
# elif choice=="/":
#     print(f"result is:{first / second}")
# elif choice=="*":
#     print(f"result is:{first * second}")
# elif choice=="%":
#     print(f"result is:{first % second}")
# else:
#     print("invalid")

# -----------------------------------------------------------------------------------------------------------------

# lst=[2,4,5,6]
# lst.append(7)
# print(lst)

# ------------------------------------------------------------------------------------------------------------------

# a=1
# b=50
# for num in range(a,b+1):
#     if num%2!=0:
#         print(f"These numbers are odd: {num}")

# ------------------------------------------------------------------------------------------------------------------

# i=int(input("enter"))
# for n in range(i):
#     for j in range(n+1):
#         print("*",end=" ")
#     print("\n")

# ---------------------------------------------------------------------------------------------------------------------
# i=0
# while i<=10:
#     print(i*"*")
#     i=i+1

# ------------------------------------------------------------------------------------------------------------------

# temp=int(input("enter temp:" ))
# if temp>30:
#     print(f"it is hot day")
# elif temp<10:
#     print(f"It is cool day")
# else:
#     print(f"invalid")

# ------------------------------------------------------------------------------------------------------------------
# a =int(input("Enter the selling price"))
# b=int(input("Enter the buying price"))
# q=int(input("Enter quant"))
# profit= (a-b)*q
# print(profit)
# ________________________________________________________________________________________________________________
# a =eval(input("Enter the selling price"))
# b=eval(input("Enter the buying price"))
# q=eval(input("Enter quant"))
# profit= (a-b)*q
# print(profit)

# ------------------------------------------------------------------------------------------------------------------
# class Point:
#   def __init__(self,xx=0,yy=0):
#         self.x=xx
#         self.y=yy
#
#         print(f"{self.x},{self.y}")
#
#
#
#
#
# p1 = Point(2,4)

# ------------------------------------------------------------------------------------------------------------------
# lst = [2,2,2,2,2,2,4,5,6]
# while True:
#     if 2 in lst:
#         lst.remove(2)
#     else:
#         break;
# print(lst)
# ------------------------------------------------------------------------------------------------------------------
# lst = [2,2,2,2,3,4,5]
# unq = []
# for num in lst:
#     if num not in unq:
#         unq.append(num)
# print(unq)

# -------------------------------------------------------------------------------------------------------------------
# lst = ["ankush","hello", "very good","okay"]
# a,b,c,d= lst
# print(a)
# print(b)
# print(c)
# print(d)

# --------------------------------------------------------------------------------------------------------------------

# name,sal,desi= (input("enter n,s,d")).split(",")
# print(name, sal, desi)

# --------------------------------------------------------------------------------------------------------------------
# lst = [2,3,4,5]
# for ind,val in enumerate(lst):
#     print(f"index: {ind}, value: {val}")

# -------------------------------------------------------------------------------------------------------------------
# lst = [2,3,4,5]
# for ind,val in enumerate(lst):
#      if ind in (0,1,2):
#          lst[ind]=val+10
#      else:
#          lst[ind]=val-2
# print(lst)

# -----------------------------------------------------------------------------------------------------------------
# lst =[]
# loop=(int(input("Enter value for loop")))
# for i in range(loop):
#     i=int(input("Enter values to add:"))
#     lst.append(i)
# print(lst)
# even=[]
# odd=[]
# for x in lst:
#     if x%2==0:
#         even.append(x)
#     else:
#         odd.append(x)
# print(even)
# print(odd)

# ---------------------------------------------------------------------------------------------------------------------

# class Project:
#     def __init__(self,nm,mrk,tpc):
#         self.name=nm
#         self.marks=mrk
#         self.topic=tpc
#
#
#         print(self.name,self.marks,self.topic)
#
#
# p=Project("ankush",25,"python")

# -------------------------------------------------------------------------------------------------------------
# a=1
# b=50
# for c in range(a,b):
#     if c%2==0:
#         print(f"even number{c}")
# -----------------------------------------------------------------------------------------------------------
# num=int(input("Enter the statring value: "))
# end=int(input("Enter ending value: "))
# for i in range(num,end):
#     if i%2==0:
#         print(i)
#--------------------------------------------------------------------------------------------------------------
# a=0
# while a<=5:
#     print(a*" *")
#     a=a+1
# ------------------------------------------------------------------------------------------------------
# n=int(input("Enter the value: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\n")
# ---------------------------------------------------------------------------------------------------------------
# import random
# lucky_num=(random.randint(1,100))
# num=eval(input("Enter the number want to match: "))
# while num!=lucky_num:
#     if num==lucky_num:
#         Print("Number matches")
#     else:
#         if num>lucky_num:
#             print("Number is large")
#         elif num<lucky_num:
#             print("Number is small")
#         num = int(input("Enter the number want to match: "))
#
# # ---------------------------------------------------------------------------------------------------------------------
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))
# c=int(input("Enter value of c: "))
#
# if a>b and a>c:
#     print("Maximum number is", a)
# elif c>b and c>a:
#     print("Maximum number is", c)
# elif b>a and b>c:
#     print("Maximum number is", b)

#---------------------------------------------------------------------------------------------------------------------
# a=int(input("enter ending point"))
# for i in range(1,a+1):
#     print(i)

#----------------------------------------------------------------------------------------------------------------------
# SWAPPING OF NUMBERS
# a=int(input("Enter the first no: "))
# b=int(input("Enter the second no: "))
# a=a+b
# b=a-b
# a=a-b
# print(f"First no: {a},Second no: {b}")
#-----------------------------------------------------------------------------------------------------------------------
# FACTORIAL
# num=int(input("Enter value:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)
#----------------------------------------------------------------------------------------------------------------------
#PALINDROME
# n=int(input("enter number to check: "))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# if temp==sum:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")
#-------------------------------------------------------------------------------------------------------------------
#REVERSE NO.
# n=int(input("Enter number"))
# while n>0:
#     r=n%10
#     print(r,end="")
#     n=n//10
#--------------------------------------------------------------------------------------------------------------------
# l=int(input("Enter length:"))
# b=int(input("breadth:"))
# area=l*b
# print(f"area of rectangle is,{area}")

#--------------------------------------------------------------------------------------------------------------------
#ARMSTRONG
# n=int(input("Enter the number to check"))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum+r*r*r
#     n=n//10
# if temp==sum:
#     print("no. is armstrong")
# else:
#     print("invalid")

#--------------------------------------------------------------------------------------------------------------------

# n=int(input("Enter No. to check"))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# i=0
# sum=0
# while i<5:
#     sum = i*i
#     i += 1
# print(sum)
