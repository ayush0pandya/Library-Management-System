from books import Book
from exception import BookRemovalError, BookRetrivalError, searchError
from validator import checkAuthor, checkTitle, checkDates
from datetime import date
class library():
    totalBooks = 0
    def __init__(self):
        self.book_list = []

    def addbook(self, book: Book):
        self.book_list.append(book)
        library.totalBooks += 1
        print("Book added")

    def removeBook_index(self, index: int):
        if len(self.book_list) == 0:
            raise BookRemovalError("No books present to remove")
        elif index >= len(self.book_list):
            raise BookRemovalError("Trying to remove book which is out of scope")
        else:
            print("Book present")
            library.totalBooks -= 1
            print("Book removed")
            return self.book_list.pop(index)
            
    
    def removeBook_Book(self, book: Book):
        if len(self.book_list) == 0:
            raise BookRemovalError("No book to remove, library is empty")
        elif book in self.book_list:
            print("Book present")
            self.book_list.remove(book)
            library.totalBooks -=1
            print("Book removed")
        else:
            raise BookRemovalError("Sorry but the book was not present in the library")


        
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