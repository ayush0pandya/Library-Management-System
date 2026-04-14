from books import Book
from exception import BookRemovalError, BookRetrivalError, searchError
from validator import checkAuthor, checkTitle, checkDates
from datetime import date
from db import *

class library():
    totalBooks = 0
    def __init__(self):
        self.connection = get_connection()
            
  
    def removeBook_Book(self, book: Book):
        '''if len(self.book_list) == 0:
            raise BookRemovalError("No book to remove, library is empty")
        elif book in self.book_list:
            print("Book present")
            self.book_list.remove(book)
            library.totalBooks -=1
            print("Book removed")
        else:
            raise BookRemovalError("Sorry but the book was not present in the library")'''
        
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
        self.connection.close()
           
        
        


        
    def getBook(self, index):
        if len(self.book_list) == 0:
            raise BookRetrivalError("No books present in the library")
        elif index >= len(self.book_list) or index < 0:
            raise BookRetrivalError("Trying to retrieve book info which is out of scope")
        else:
            return self.book_list[index]      
    
    def search_by_title(self, name: str):
        checkTitle(name)
        tempname = name.lower()
        result =[]
        for x in self.book_list:
            title = x.title.lower()
            if title == tempname:
                result.append(x)

        if len(result) == 0:
           raise searchError("No book retirieved")
        return result

    def search_by_author(self, name: str):
        checkAuthor(name)
        tempname = name.lower()
        result = []
        for x in self.book_list:
            auth = x.author.lower()
            if auth == tempname:
                result.append(x)

        if len(result) ==0:
            raise searchError("No book retirieved")
        return result 

    def search_by_year(self, year: int):
        result = []
        for x in self.book_list:
            if x.publishing_date.year == year:
                result.append(x)
        
        if len(result) == 0:
            raise searchError("No book retirieved")
        return result

    def __iter__(self):
        return iter(self.book_list)