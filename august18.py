#Create a simple calculater class to perform basic mathematical operations
#(square,cube,square_root)

import math

class calculater:
    def __init__(self,number):
        self.number = number
    def square(self):
        print("Square of ",self.number,"is",self.number**2)
    def cube(self):
        print("Cube of ",self.number,"is",self.number**3)
    def square_root(self):
        if self.number<0:
            raise ValueError("Square root of a negative number is not defined in real number.. ")
        else:
            print("Square root of",self.number,"is",math.sqrt(self.number))
#create objects of calculater
s1 = calculater(18)
s2 = calculater(27)
#call methods
s1.square()
s1.cube()
s1.square_root()
print("----------------------")
s2.square()
s2.cube()
s2.square_root()

    
