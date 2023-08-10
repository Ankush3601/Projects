# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         print(a, b)
#
#     def __eq__(self, other):
#         return point.a == other.a and point.b == other.b
#
#
# point = Point(1, 2)
# other = Point(1, 2)
# print(point == other)

# class Product:
#     def __init__(self, price):
#         self.price=price
# print(price)
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("price can not be negative")
#         self.__price = value
#     # price = property(get_price,set_price)
#
# pr = Product(2)
# print(pr.price)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hello {self.name} Good Morning")
#
#
# a = Person("ankush")
# a.talk()
# print(a.name)
