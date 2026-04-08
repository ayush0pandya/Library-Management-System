# main.py
from books import Book
from library import library
from member import Member
import db
from exception import (
    WrongTitleError, WrongAuthorError, WrongDateError,
    searchError, BookRemovalError, BookRetrivalError
)

db.setup()