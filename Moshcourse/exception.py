# try:
#     age=int(input("Enter age: "))
#     print(age)
# except ValueError as er :
#     print("age is not valid")
#     print(er)
# from timeit import timeit
# code1= """
# def check_age(age):
#     if age<=0:
#              raise ValueError ("Age cannot be less than 0")
#
#     return 10/age
#
#
# try:
#     check_age(-5)
# except ValueError as p:
#     print(p)
# """
# print(timeit (code1, number=1000))

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x,y)

    # def draw(self):
    #     print(self.x,self.y)

point=Point(1,2)
# point.draw()

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#          print(x,y)
#
#     def __eq__(self, next):
#         return self.x==next.x and self.y==next.y
#
#
# point = Point(1,2)
# next = Point(1,2)
# print(point==next)










