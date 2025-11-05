from books import Book
import email_validator
from library import *
from exception import *
class Member:
    def __init__(self, name: str, age: int, email: str, library_id: int):
        self.__name = name
        self.__age = age
        self.__email = email_validator.validate_email(email, check_deliverability= False).email
        self.__library_id = library_id
        self.__books_borrowed = set()
        self.__num_borrowed = 0

    @property
    def name(self)-> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def library_id(self)-> int:
        return self.__library_id
    
    @name.setter
    def name(self, name: str)-> None:
        self.__name = name

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email_validator.validate_email(email, check_deliverability= False).email

    # Library id, once created, can not be changed so no setter for it 

    def print_set(self) -> None:
        for x in self.__books_borrowed:
            print(x)

    def borrow_book(self, book: Book, lib: library) -> None:
        if book in lib.book_list:
            self.__books_borrowed.add(book)
            self.__num_borrowed+=1
            lib.removeBook_Book(book)
        else:
            raise searchError("Book is not present in the library")

    def return_book(self, book: Book, lib: library) -> None:
        if book in self.__books_borrowed:
            self.__books_borrowed.discard(book)
            self.__num_borrowed -= 1
            lib.addbook(book)
        else:
            raise searchError("Book not present to return")

    def __str__(self) -> str:
        return(f"Member name is {self.__name} with {self.__num_borrowed} borrowed book(s)")

    def __repr__(self) -> str:
        return(f"Member name = {self.__name} age = {self.__age} email = {self.__email} library ID = {self.__library_id} Books borrowed = {self.__books_borrowed} Total = {self.__num_borrowed}")