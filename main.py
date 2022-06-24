from pip import main


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in Central Library are: ")
        for book in self.books:
            print(" *"+book)

    def burrowBook(self, bookName):
        if bookName in self.books:
            print(f"{bookName} is issued for you. please return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry {bookName} is currently unavailable. Wait until book will be available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thanks for returning {bookName}!")

class Student:
    def requestBook(self):
        self.book = input("Enter name of book that you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter name of book that you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["CP", "Algo", "DS", "Networking", "Python"])
    # centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        welcomeMsg = '''
                -*-*-*  Welcome to Central Library  *-*-*-
                        Please choose one option from below:
                        1. View all books available in library
                        2. Request a book
                        3. Return a book
                        4. Exit form Library
        '''
        print(welcomeMsg)

        option = int(input("\nEnter your option: "))
        if option == 1:
            centralLibrary.displayAvailableBooks()
        elif option == 2:
            centralLibrary.burrowBook(student.requestBook())
        elif option == 3:
            centralLibrary.returnBook(student.returnBook())
        elif option == 4:
            print("Thanks for using Central Library")
            exit()
        else:
            print("Invalid choice. Please choose correct option.")

