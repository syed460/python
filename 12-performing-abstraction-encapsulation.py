# implement a library management system which will handle the following tasks:

# 1. customer should be able to display all the books availble in the library
# 2. Handle the process when a customer requests to borrow a book
# 3. update the library collection when the customer returns a book

class Library:
 def __init__(self, bookList):
  self.availableBooks = bookList

 def displayAvailableBooks(self):
  print("Displaying the available books details")
  print(self.availableBooks)
  for book in self.availableBooks:
   print(book)

 def lendBook(self, requestedBook):
  if requestedBook in self.availableBooks:
   print("Book is available")
   self.availableBooks.remove(requestedBook)
  else: print("Requested Book is not availble")
 
 def addBook(self, bookName):
  self.availableBooks.append(bookName)
  print("Added the book to the library")


class Customer:

 def requestBook(self):
  print("select the required book to borrow")
  self.book = input()
  return self.book

 def returnBook(self):
  print("Enter the name of the book")
  self.book = input()
  return self.book


library = Library(["Book One", "Bood Two", "Book Three"])
customer = Customer()

while True:
 print("Enter 1 to display the availble books")
 print("Enter 2 to request a book")
 print("Enter 3 to return a book")
 print("Enter 4 to exit")

 userInput = int(input())

 if userInput == 1:
  library.displayAvailableBooks()
 elif userInput == 2:
  book = customer.requestBook()
  library.lendBook(book)
 elif userInput == 3:
  book = customer.requestBook()
  library.addBook(book)
 elif userInput == 4:
  quit()

# =========== Learning
# input() function which will take the input from the user.
# array.remove("something") function to delete item in array
# array.append("something") function to append item into array
# quit() function is to exit the script