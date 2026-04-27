from books import Book
import email_validator as emv
from library import library
from exception import *
class Member:
    def __init__(self, firstN: str, lastN : str,  age: int, email: str):
        self.connection = get_connection()
        cursor = self.connection.cursor()
        self.__First_Name, self.__Last_Name, self.__Age, self.__Email =  firstN, lastN, age, emv.validate_email(email, check_deliverability=False).email
        cursor.execute("insert into Member (First_Name, Last_Name, Age, Email) values (?,?,?,?)", ( firstN, lastN, age, self.__Email))
        self.__ID = cursor.lastrowid
        self.connection.commit()
        cursor.close()

    @property
    def first_name(self)-> str:
        return self.__First_Name
    
    @property
    def last_name(self)-> str:
        return self.__Last_Name

    @property
    def age(self) -> int:
        return self.__Age
    
    @property
    def email(self) -> str:
        return self.__Email
    
    @property
    def id(self):
        return self.__ID
    
    @first_name.setter
    def first_name(self, first: str)-> None:
        self.__First_Name = first

    @last_name.setter
    def last_name(self, last: str)-> None:
        self.__Last_Name = last

    @age.setter
    def age(self, age: int) -> None:
        self.__Age = age
    
    @email.setter
    def email(self, email: str) -> None:
        self.__Email = emv.validate_email(email, check_deliverability= False).email

    # Library id, once created, can not be changed so no setter for it 


    def borrow_book(self, book: Book, lib : library) -> None:
        cursor = self.connection.cursor()
        try:
            temp = lib.getBook_by_serialNumber(book.serialNumber)
            if temp[6] == 0:
                print("Book has already been borrrowed")
            elif temp[6] == 1:
                cursor.execute("update Books set is_borrowed = 1 where serial_number = ?", (book.serialNumber,))
                cursor.execute("insert into Borrows(member_id, book_id) values (?,?)", (self.__ID, book.serialNumber))
                self.connection.commit()
                cursor.close()
                print("The book has been borrowed")
        except BookRetrivalError:
            raise BookRetrivalError("The book is not present in the library")

    def return_book(self, book: Book, lib: library) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute("select * from Borrows where book_id = ?", (book.serialNumber))
        except:
            pass


    def __str__(self) -> str:
        return(f"Member name is {self.__name} with {self.__num_borrowed} borrowed book(s)")

    def __repr__(self) -> str:
        return(f"Member name = {self.__name} age = {self.__age} email = {self.__email} library ID = {self.__library_id} Books borrowed = {self.__books_borrowed} Total = {self.__num_borrowed}")