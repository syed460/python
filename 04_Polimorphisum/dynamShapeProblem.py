# creating 
# classA 
#  -> classB 
#    -> classD
#  -> classC 
#    -> classD


class A:
 def method(self):
  print("this method belongs to class A")

class B(A):
 def method(self):
  print("This method is overridden in class B")
 # pass

class C(A):
 def method(self):
  print("This method is overridden in class C")
 # pass

class D(C, B):
 pass

# CASE1: Method will not be overridden in class B and C

d = D()

d.method()

# CASE2: Method will be overridden in class B but not in C


# CASE3: Method will be overridden in class C but not in B
# CASE4: Method will be overridden in both class B and class C