# def greet(first_name,last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
#
#
#
# greet("Ankush","Minocha")
# def increment(number,by):
#     return number+by
#
# # result = increment(2,1)
# print(increment(2, by=1))

# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total *= number
#     return total
#
# print(multiply(2,3,4,5))
# def user(**details):
#     print(details)
#
#
# user(id=1, name="ankush", age=22)

def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        return "fizz_buzz"
    if input%3==0:
        return "fizz"
    if input%5==0:
        return "buzz"
    else:
        return (input)

print(fizz_buzz(16))






