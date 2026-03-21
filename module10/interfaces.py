from abc import ABC, abstractmethod

#abstract class 'printable' acts as a interface

class Printable(ABC):
    #abstract method that must beb implament by any subclass
    @abstractmethod
    def print_info(self):
        pass

class Book(printable):
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"Book:{self.title} by {self.author} ")


#create an instance of  the 'book' class  and call the 'print_info' method

book = Book("the great gatsby", "f. scott")
