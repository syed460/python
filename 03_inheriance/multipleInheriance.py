# A Dirived Class can have more than one BASE Class. It will have access to all the attributes and methods of all the base classes.

# Three Classes
 # Two classes are BASE clases
 # one class is Drived class

class OperatingSystem:
 multitasking = True

class Apple:
 website = "www.apple.com"

class MacBook(OperatingSystem, Apple):
 def __init__(self):
  if self.multitasking == True:
   print("It is multitasking system. Visit {} for more details.".format(self.website))


macBook = MacBook()

#-----------

# If we have commun attribute in the BASE classes. First it will check from baseclass configured from left to right.

# Dymenshape Problem
 #-- when we will face while using multiple inheritance