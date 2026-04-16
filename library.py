from books import Book
from exception import BookRemovalError, BookRetrivalError
from validator import checkAuthor, checkTitle, checkDates
from datetime import date
from db import *

class library():
    totalBooks = 0
    def __init__(self):
        self.connection = get_connection()
            
  
    def removeBook_Book(self, book: Book):
        
        cursor = self.connection.cursor()
        cursor.execute("select * from Books where Title = ? AND Serial_number = ?", (book.title, book.serialNumber))
        temp_Book = cursor.fetchone()     
        if temp_Book is None:
            raise BookRemovalError("Sorry but the book was never present in the library")
        elif temp_Book[6] == 0:
            raise BookRemovalError("Sorry but the book is not present in the library")
        else:
            cursor.execute("update Books set is_present = 0 where Title = ? AND Serial_number = ?", (book.title, book.serialNumber))
        self.connection.commit()
        cursor.close()

        
    def getBook_by_serialNumber(self, serial_no: int):
        cursor = self.connection.cursor()
        cursor.execute("select * from Books where Serial_number = ?", (serial_no,))
        result = cursor.fetchone()
        if result is None:
            raise BookRetrivalError(f"The book with the serial number {serial_no} can not be found")
        cursor.close()
        return result
    
    def getBook_by_Title(self, title: str):
        cursor = self.connection.cursor()
        cursor.execute("select * from Books where Title = ?", (title,))
        result = cursor.fetchall()
        if not result:
            raise BookRetrivalError(f"The book with the Title {title} can not be found")
        cursor.close()
        return result

    def getBook_by_Author(self, author: str):
        cursor = self.connection.cursor()
        cursor.execute("select * from Books where Author = ?", (author,))
        result = cursor.fetchall()
        if not result:
            raise BookRetrivalError(f"The book by the Author {author} can not be found")
        cursor.close()
        return result

    def __iter__(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Books where is_present = 1")
        return iter(cursor.fetchall())