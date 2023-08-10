# overriding
# class Animal:
#     def __init__(self):
#         self.age=1
#     def eat(self):
#         print("eat")
#
#
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         self.weight=2
#     def walk(self):
#         print("walk")
#
#
# class Fish(Animal):
#     def swim(self):
#         print("swim")
#
#
# m = Mammal()
# print(m.age)
# print(m.weight)

# Multilevel inheritance

# class Swimmer:
#     def swim(self):
#         pass
#
#
# class Flyer:
#     def fly(self):
#         pass
#
# class SwimFly(Swimmer,Flyer):
#     pass
# from logging import exception
#
#
# class InvalidError(exception):
#     pass
#
#
# class Stream:
#     def __init__(self):
#         self.opened = False
#
#     def open(self):
#         if self.opened:
#             raise InvalidError("Already opened")
#
#         self.opened = True
#     def close(self):
#         if not self.opened:
#             raise  InvalidError("Already closed")
#
# class FileStream:
#     def read(self):
#         print("reading data from file")
#
# class NetworkStream:
#     def read(self):
#         print("reading data from network")
# import convertor
# c=convertor.convert_kg_to_lb(56)
# print(c)

