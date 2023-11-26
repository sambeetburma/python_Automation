class Shape:
    def area(self):
        print("Area of shape")


class Rectangle(Shape):
    def __init__(self, len, breadth):
        self.len = len
        self.breadth = breadth

    def area(self):
        return self.len * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Shape()
shape1.area()

shape2 = Rectangle(4,7)
print("shape of Rectangle:", shape2.area())

shape3 = Circle(6)
print("shape of circle:", shape3.area())


