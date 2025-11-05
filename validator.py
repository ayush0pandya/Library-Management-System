# This module is specificaly made to contain the validators for the program 
import sys
from random import randint
from exception import WrongTitleError, WrongDateError, WrongAuthorError, BookRemovalError
from datetime import date

def checkNum(num, num_list):
    if num in num_list:
        while num in num_list:
            num = randint(0, sys.maxsize)

    return num

def checkAuthor(author):  
    disallowed_chars = set(['@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '~', '"', '!', '_', '+', '='])
    if not isinstance(author, str):
        raise WrongAuthorError("Please enter the author as String")
    author = author.strip()
    if len(author) > 50:
        raise WrongAuthorError("Please enter the appropriate length of author")
    elif any(x in disallowed_chars for x in author):
        raise WrongAuthorError("Invalid character detected")
    elif any(ord(x) >= 48 and ord(x) <= 57 for x in author):
        raise WrongAuthorError("Numbers can not be a author")
    elif len(author) == 0:
        return "Unknown Author"
    else:
        return author
    

def checkTitle(title):
    disallowed_chars = set(['@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '~', '"', '_', '+', '='])
    '''if not isinstance(title, str):
        raise WrongTitleError("Please enter the title as String")'''
    
    title = title.strip()
    if len(title) > 50:
        raise WrongTitleError("Please enter the appropriate lenth of title")
    elif any(x in disallowed_chars for x in title):
        raise WrongTitleError("Invalid character detected")
    elif len(title) == 0:
        return "Unknown Title"
    else:
        return title


def checkDates(year: int, month: int, day: int):
    try:
        final_date = date(year,month,day)
    except ValueError as e:
        raise WrongDateError("Wrong date provided")
    else:
        return final_date
    
    