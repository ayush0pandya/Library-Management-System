# This is an exception only file that will have all the custom exception for the program
class WrongTitleError(Exception):
    def __init__(self, input):
        super().__init__(input)
        self.message = input

    def __str__(self):
        return (f"The input {self.message} is not valid, please enter the title as String")

class WrongDateError(Exception):
    def __init__(self, input):
        super().__init__(input)
        self.message = input

    def __str__(self):
        return (f"The date enterd {self.message} is not correct, please enter a correct date")
    
class WrongAuthorError(Exception):
    def __init__(self, input):
        super().__init__(input)
        self.message = input

    def __str__(self):
        return (f"The Author name enterd {self.message} is not correct, please enter name")

class BookRemovalError(Exception):
    def __init__(self, input):
        super().__init__(input)
        self.message = input

    def __str__(self):
        return (f"The book can not be removed {self.message}")    
    
class BookRetrivalError(Exception):
    def __init__(self, input):
        super().__init__(input)
        self.message = input

    def __str__(self):
        return (f"The book can not be found {self.message}")
    
class searchError(Exception):
    def __init__(self, input):
        super().__init__(input)
        self.message = input

    def __str__(self):
        return(f"The book can not be retirved {self.message}")