# two class
# first parent class
# second child class which will inherite certain attribuet and methods from parent class apart from having its own attributes and methods


class Apple:
 manufaturere = "Apple Inc."
 contactWebSite = "www.apple.com/contact"

 def contactDetails(self):
  print("to contact apple log on to ", self.contactWebSite)


# to make MacBook class to inherite the attribute and method add 'Apple' within parentesys
class MacBook(Apple):
 def __init__(self):
  self.yearOfManufacturer = 2019

 def manufaturereDetails(self):
  print("This macBook was manufactured Year {} by {}".format(self.yearOfManufacturer, self.manufaturere))


macBook= MacBook()

macBook.manufaturereDetails()

macBook.contactDetails()

#=============
# Base Class Class Apple
# Derived class is MacBook