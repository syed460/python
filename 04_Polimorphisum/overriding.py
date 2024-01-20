# two classes
# one to 


class Employee:
 # def __init__(self):
 #  self
 def setNumberOfWorkingHours(self):
  self.numberOfWorkingHours = 40

 def displayNumberOfWorkingHours(self):
  print(self.numberOfWorkingHours)

class Trainee(Employee):
 def setNumberOfWorkingHours(self):
  # return super().setNumberOfWorkingHours()
  self.numberOfWorkingHours = 45

# We have created "setNumberOfWorkingHours" method in the derived class which will overrite the method while invoking.
  
 def resetNumberOfWorkingHours(self):
  return super().setNumberOfWorkingHours()

# We have created "resetNumberOfWorkingHours" using "super()" method which helps to access the parent methods
  
employee = Employee()

employee.setNumberOfWorkingHours()
print("Number of WorkingHours of Employee:", end = " ")
employee.displayNumberOfWorkingHours()

trainee = Trainee()

trainee.setNumberOfWorkingHours()
print("Number or working hours of Trainee ", end=" ")
trainee.displayNumberOfWorkingHours()

trainee.resetNumberOfWorkingHours()
print("Number or working hours of Trainee after reset ", end=" ")
trainee.displayNumberOfWorkingHours()