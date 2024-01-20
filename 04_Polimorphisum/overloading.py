# overloading is one of the property of polimorphism

# lets see how to overload addtion operator

class Square:
 def __init__(self, side):
  self.side = side

 def __add__(squareOne, squareTwo):
  return ((4 * squareOne.side) + (4 * squareTwo.side))

squareOne = Square(5)

squareTwo = Square(6)


print("sum of squareOne and squareTwo: ", squareOne + squareTwo)


# Learnings

# __add__ is special method