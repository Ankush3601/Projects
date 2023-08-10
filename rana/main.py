# x=int(input("Enter value:"))
# match x:
#     case 0:
#         print("x is zero")
#     case 1:
#         print("x is 1")
#     case 2:
#         print("x is 2")
#     case _:
#         print(x)

# vowels=("a","b","c","d")
# sum=0
# for i in numbers:
#     sum=sum+i
# print("Average is:",sum/len(numbers))
# n=int(input("Enter the value"))
# temp=0
# for(i=2;i<=n-1;i++)
# n=int(input("Entr"))
# temp = 0
# for i in range(2,n+1):
#
#             if(i % n==0):
#                 temp = temp+1
#
# if(temp>0):
#     print("no.is not prime")
# else:
#     print("no.is  prime")
# n=int(input("Enter number"))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# if(temp==sum):
#         print("no is palindrome")
# else:
#         print("not palindome")
# n=int(input("Enter number"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False

print(is_prime(9))