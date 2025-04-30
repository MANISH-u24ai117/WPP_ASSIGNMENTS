import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# User Input
shape_type = input("Enter shape type (rectangle/circle): ").lower()

if shape_type == "rectangle":
    width = float(input("Enter width of rectangle: "))
    height = float(input("Enter height of rectangle: "))
    rect = Rectangle(width, height)
    print("Rectangle area:", rect.area())
    print("Rectangle perimeter:", rect.perimeter())

elif shape_type == "circle":
    radius = float(input("Enter radius of circle: "))
    circle = Circle(radius)
    print("Circle area:", circle.area())
    print("Circle perimeter:", circle.perimeter())
