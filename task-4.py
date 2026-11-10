class Dog:
    def make_sound(self):
        print("Dog's sound")

class Cat:
    def make_sound(self):
        print("Cat's sound")
class Cow:
    def make_sound(self):
        print("Cow's sound")


dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()
cow = Cow()
cow.make_sound()


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        ...

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):

        return f"the area of rectangle{self.width * self.height}"



class Circle(Shape):
    PI = 3.14159
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return f"area of circle {round(Circle.PI * self.radius * self.radius,2)}"

rectangle = Rectangle(100, 200)
print(rectangle.calculate_area())
circle = Circle(100)
print(circle.calculate_area())


# QUESTIONS ANSWER

# polymorphism is using one method in many form
# abstraction is the process of hiding unnecessary implementation details and exposing only the essential functionality to the user.
# ABSTRACT class is a class that inherits from ABC and have an abstract methods that must be implemented by the child classes
# if child class doesn't implement abstract method it gives typeError error



