# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#
#     @classmethod
#     def sum(cls, num1, num2):
#         return num1 + num2
#
#
# print(Animal.sum(1, 2))
#
# class Shape:
#     def __init__(self, length, width):
#         self.lenght = length
#         self.width = width
#     def __add__(self, other):
#         return [self.lenght + other.lenght, self.width+other.width]
#
#     def __eq__(self, other):
#         return self.lenght == other.lenght and self.width == other.width
#
# rec1=Shape(10,20)
# rec2=Shape(10,20)
# print(rec1+rec2)
# print(rec1==rec2)


from abc import ABC, abstractmethod

