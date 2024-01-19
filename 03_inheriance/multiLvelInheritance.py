

# create class 
class MusicalInstruments:
 numberOfMajorKeys = 12

#creating subset of MusicalInstruments 
class StringInstruments(MusicalInstruments):
 typeOfWood = "ToneWood"

# Creating subset of StringInsturments
 
class Guitar(StringInstruments):
 def __init__(self):
  self.numberOfString = 6
  print("This Guitar consists of {} strings. It is made of {} it can play {} keys".format(self.numberOfString, self.typeOfWood, self.numberOfMajorKeys))


guitar = Guitar()