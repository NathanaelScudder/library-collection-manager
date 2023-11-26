from collections import namedtuple
from datetime import datetime

'''
used for testing purposes
Book = namedtuple("Book", "title author yearPub pageLength dateAdded")
listOfBooks = []
p = Book("Taco", "Aba", "2019", "500", "375777678678")
q = Book("Food", "Aba", "2019", "378", "46586774")
d = Book("Pizza", "Aba", "2017", "500", "6547")
e = Book("AllyBaba", "William Shakespeare", "1700", "996", "123776767686")
h = Book("Superman", "Albert Roe", "1967", "679", "234868687872")
k = Book("Tommy Tooth", "Einstein", "1245", "1500", "1787806")

listOfBooks.append(p)
listOfBooks.append(q)
listOfBooks.append(d)
listOfBooks.append(e)
listOfBooks.append(h)
listOfBooks.append(k)
'''

### Author, pages, and year each have a secondary sorting method. If multiple instances of a desired search
### exist (i.e an author has two or more books or two or more books were published in 2012)
### the instances have a sub-sorting using their title and go in ABC order
###
### sorted usage adapted from: https://docs.python.org/3/howto/sorting.html

def sortByAuthor(library):
    'takes library object as input, sorts by author. Returns updated library object'
    tempList = library.bookList
    library.bookList = sorted(tempList, key=lambda Book: (Book[1],Book[0]))
    return library

def sortByPages(library):
    'takes library object as input. Sorts from smallest page count to highest page count. Returns updated library object'
    tempList = library.bookList
    library.bookList = sorted(tempList, key=lambda Book: (int(Book[3]), Book[0]))
    return library

def sortByYear(library):
    'takes library object as input. Sorts from oldest to newest by year looking at the books publishing year. Returns updated library object'
    tempList = library.bookList
    library.bookList = sorted(tempList, key = lambda Book: (int(Book[2]), Book[0]))
    return library

def sortByTitle(library):
    'takes library object as input. Sorts titles in ABC order. Returns updated library object' 
    tempList = library.bookList
    library.bookList = sorted(tempList, key=lambda Book: Book[0])
    return library

def sortByDate(library):
    'takes library object as input. Sorts from oldest to newest in terms of when the book was first added to the library database. Returns updated library object'
    tempList = library.bookList
    library.bookList = sorted(tempList, key=lambda Book: float((Book[4])))
    return library

