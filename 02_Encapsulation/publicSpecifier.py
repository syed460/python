# Public: Sticking notice outside house
# Making the member accessible from everywhere
# memberName

# Protected: sticking notice inside house
# Making member accessible within this class and its drived class
# _memberName

# Private: sticking notice inside your room
# Making member accessible within this class
# __memberName


class Car:
 numberOfWheels = 4
 _color = "Black"
 __yearOfManufacture = 2018 # Stored as _Car__yearOfManufacture

class Bmw(Car):
 def __init__(self):
  print("The BMW car color is {}".format(self._color))

bmwCar = Bmw()

# print("Car Manufatured Year {}".format(bmwCar.__yearOfManufacture)) # Error

print(Car._Car__yearOfManufacture)

car = Car()

print(car._Car__yearOfManufacture)