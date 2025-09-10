#BASE CLASS (PARENT)

class shape:
        def area(self):
                return 0
        def perimeter(self):
                return 0

#CHILD CLASS (RECTANGLE INHERITS SHAPE)
class Rectangle(shape):
        def __init__(self,length,width):
                self.length = length
                self.width = width
        # Polymorphism: same method names but different logic
        def area(self):
                return self.length*self.width
        def perimeter(self):
                return 2*(self.length+self.width)
#CHILD CLASS (CIRCLE INHERITS SHAPE)
class Circle(shape):
        def __init__(self,radius):
                self.radius = radius
        # Polymorphism: same method names but different logic
        def area(self):
                return 3.14*self.radius
        def perimeter(self):
                return 2*3.14*self.radius
#USING POLYMORPHISM
shapes = [Rectangle(5,10),Circle(7)]

for shape in shapes:
        print(f"{shape.__class__.__name__} _>Area:{shape.area()},Perimeter:{shape.perimeter()}")
