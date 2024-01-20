 # a "Abstract Base Class" does not have defenition on its own.
# It has abstract methods which "forces implementation of certain methods in its dirived classes"

 # ABCMeta is class which has the property of abstact base class
from abc import ABCMeta, abstractmethod



class Shape(metaclass = ABCMeta):
 # By adding "abstractmethod" decoration below method, we are making sure it is present in drived classes
 @abstractmethod
 def area(self):
  return 0

class Square(Shape):
 side = 4
 # def area(self):
 #  print("area of square: ", self.side * self.side)


class Rectangle(Shape):
 width = 4
 length = 3
 def area(self):
  print("area of rectangle: ", self.width * self.length)


square = Square()

rectangle = Rectangle()

# square.area()
rectangle.area()