from random import randint
import sys
from datetime import date
from validator import checkNum, checkAuthor, checkTitle, checkDates

class Book:

    __book_number_list = set()

    def __init__(self, year: int, month: int, day: int, book_number:int = None, author: str = "", title: str = "") -> None:
            self.__title = checkTitle(title)
            self.__author = checkAuthor(author)
            if book_number is None:
                self.__serialNumber = checkNum(randint(0, sys.maxsize), Book.__book_number_list)
            else:
                self.__serialNumber = checkNum(book_number, Book.__book_number_list)    
            Book.__book_number_list.add(self.__serialNumber)
            self.__publishing_date = checkDates(year, month, day)
            
    @property
    def author(self) -> str:
        return self.__author
    
    @author.setter
    def author(self, author: str) -> None:
        self.__author = checkAuthor(author)

    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, title: str) -> None:
        self.__title = checkTitle(title)

    @property
    def serialNumber(self) -> int:
        return self.__serialNumber
    
    @property
    def publishing_date(self) -> date:
        return self.__publishing_date
    
    @classmethod
    def reset_book_list(self) -> None:
        Book.__book_number_list.clear()

    # This method is mainly used for comparing serial numbers of the book as there cannot be two books with same serial number 
    def __eq__(self, another: "Book") -> bool:
        if isinstance(another, Book):
            return another.serialNumber == self.serialNumber
        return False
    
    # Overriding the hash function to set the key to serial numbers of the books
    def __hash__(self) -> int:
        return hash(self.serialNumber)

    def __str__(self) -> str:
        return (f"{self.__title} written by {self.__author} (Serial Number {self.__serialNumber}) published on {self.__publishing_date}")
    
    def __repr__(self) -> str:
        return (f"Book(Author = ({self.author}) Title = ({self.title}) Serial Number = ({self.serialNumber}) Date = ({self.publishing_date}))")