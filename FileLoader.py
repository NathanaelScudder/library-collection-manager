from collections import namedtuple
import os
from pathlib import Path
import time

class InputError(Exception):
    pass

class BookNotFoundError(Exception):
    pass

class BadPathError(Exception):
    pass

class EmptyDirectory(Exception):
    pass

class Library:
    def __init__(self,path,bookList = list):
        self.path = path
        self.bookList = bookList

Book = namedtuple("Book", "title author yearPub pageLength dateAdded")

"""def CreateDirect(library, fileName):
    'Takes the currently loaded library and a file name and creates a new directory. Returns an error if directory already exists. Returns nothing'
    library.path = library.path + "\\" + fileName
    newPath = Path(library.path)
    if newPath.exists() and newPath.is_dir(): 
        raise InputError("Error. There is a already a directory by that name")
    else:
        os.mkdir(newPath)
    return library"""
    
def addBook(library,title,author,yearPub,pageCount): 
    'takes the currently loaded library, plus the information from each book, info received by the GUI, returns the updated library object with new bookList'
    try:
        path = library.path
        title = title
        author = author
        yearPub = yearPub
        pageCount = pageCount
        dateAdded = time.time()
        p = Book(title,author,int(yearPub),int(pageCount),dateAdded)
    except:
        raise InputError("There was an error with your input") #Theortically, this error should never be raised as all the info should be supplied 
    dateString = str(dateAdded) #allows for a string representation of the date
    newPath = path + "\\" + dateString + ".book"                    #from the GUI prior to the addBook being called
    file = newPath #Creates a copy of the directory that is not a Path object
    newPath = Path(newPath) #takes the current path, adds on the UNIX date and .book extension and makes it a Path object
    library.bookList.append(p)
    temp = open(file, "w")
    temp.write(title + "\n" + author + "\n" + str(yearPub) + "\n" + str(pageCount) + "\n" + dateString)
    temp.close()
    return library

            
def deleteBook(library,date):
    'takes the currently loaded library object and a title of a book to delete. Returns the newly updated library objected'
    date = str(date) #Ensures date is of string type 
    if len(library.bookList) == 0:
        raise EmptyDirectory("You attempted to remove a book from an empty list. Either your loaded directory has no books or you have not loaded a directory")
    path = library.path + "\\" + date + ".book"
    #library.path = path
    newPath = Path(path)
    if newPath.exists():
        for x in range(len(library.bookList)):
            if library.bookList[x].dateAdded.strip() == date: #goes through the bookList, finds the index of the date given, and deletes both
                index = x                                   #the from bookList and deletes it from the file directory 
                del library.bookList[index]
                os.remove(newPath)
                break            
            
    else:
        raise BookNotFoundError("Book not found in specified directory")

    return library

def loadFile(directory):
    'takes a directory path to load in. Returns a library object containing the path and a list of namedTuples'  
    library = Library(directory) #creates a current instance of library to be used 
    library.bookList = []
    path = library.path
    path = Path(path) #Makes the string path a path object
    if path.exists() and path.is_dir(): #Makes sure given path exists and is a directory
        for book in path.iterdir(): #iterates through directory, adding all .book files in said directory to the current instance of bookList
            if book.is_file() and book.suffix == ".book":
                temp = open(book, "r")
                lines = [line.rstrip() for line in temp.readlines()]
                tempBook = Book(lines[0],lines[1],lines[2],lines[3],lines[4]) #every .book contains a single piece of the required info on its own line
                library.bookList.append(tempBook)
                temp.close()
        
    else: #if this is reached then either the path is not a usable input
        raise BadPathError("Given path is not a directory or does not exist")

    return library
    
    
'''
def Test():
    test = input("Give a path to load or create a library directory: ")
    
    while(True):
        choice = input("C: for creating new file, L: loading, A: adding book, AB: add book by ISBN, D: for deleting: ")
        if choice == "C":
            fileName = input("File name to create: ")
            test = CreateDirect(test,fileName)

        elif choice == "L":
            test = loadFile(test)

        elif choice == "A":
            title = input()
            author = input()
            yearPub = input()
            page = input()
            test = addBook(test,title,author,yearPub,page)

        elif choice == "D":
            date = input("Book to delete: ")
            test = deleteBook(test,date)

 '''           
            

