# AddBookFrame.py

import tkinter
from tkinter import messagebox

import FileLoader
from FileLoader import Library

import ISBNAPI
from ISBNAPI import BookAPI

# Constants for the button length and width
_BUTTON_WIDTH = 15
_BUTTON_LENGTH = 2

# Constants for the entry width
_ENTRY_WIDTH = 30


class AddBookFrame:
    """
    Defines AddBookFrame objects.

    Contains the widgets needed to operate the Add Book screen for the LibraryCollectionGUI.

    The frame can be drawn to the GUI using draw(), or removed from the GUI using destroy().

    """

    def __init__(self, window: tkinter.Tk, bookCollection: Library, cancelFunction, crashToMainMenuFunction):
        """
        Constructs the AddBookFrame for the specified window.

        :param window: The window to set as the master for this frame.
        :param bookCollection: The list of books to add the new book to.
        :param cancelFunction: The function to invoke when the user selects "CANCEL".
        :param crashToMainMenuFunction: The function to invoke if the collection is removed outside the program
        """

        self.window = window
        self.addBookFrame = None

        self.cancelFunction = cancelFunction
        self.crashToMainMenuFunction = crashToMainMenuFunction

        self.bookCollection = bookCollection

        # To hold the attributes for the new book
        self.bookTitle = tkinter.StringVar()
        self.authorName = tkinter.StringVar()
        self.yearPublished = tkinter.StringVar()
        self.pageLength = tkinter.StringVar()

        # To hold an optional ISBN numbers
        self.isbn = tkinter.StringVar()

        # End of init()

    def draw(self) -> None:
        """
        Draws the AddBookFrame widgets to the window.

        :return: None
        :raises AttributeError: If the current collection is empty
        """

        # Construct the frame
        self.addBookFrame = tkinter.Frame(self.window, pady=50)

        # Construct the frame for the attribute entries and labels
        entryFrame = tkinter.Frame(self.addBookFrame, padx=10)

        bookTitleLabel = \
            tkinter.Label(entryFrame, text="Enter the book's title:                ", font="TkFixedFont")

        authorNameLabel = \
            tkinter.Label(entryFrame, text="Enter the author name(s):              ", font="TkFixedFont")

        yearPublishedLabel = \
            tkinter.Label(entryFrame, text="Enter the book's publishing year:      ", font="TkFixedFont")

        pageLengthLabel = \
            tkinter.Label(entryFrame, text="Enter the book's page length:          ", font="TkFixedFont")

        bookTitleLabel.grid(row=0, column=0, pady=5)
        authorNameLabel.grid(row=1, column=0, pady=5)
        yearPublishedLabel.grid(row=2, column=0, pady=5)
        pageLengthLabel.grid(row=3, column=0, pady=5)

        bookTitleEntry = \
            tkinter.Entry(entryFrame, textvariable=self.bookTitle, font="TkFixedFont", width=_ENTRY_WIDTH)

        authorNameEntry = \
            tkinter.Entry(entryFrame, textvariable=self.authorName, font="TkFixedFont", width=_ENTRY_WIDTH)

        yearPublishedEntry = \
            tkinter.Entry(entryFrame, textvariable=self.yearPublished, font="TkFixedFont", width=_ENTRY_WIDTH)

        pageLengthEntry = \
            tkinter.Entry(entryFrame, textvariable=self.pageLength, font="TkFixedFont", width=_ENTRY_WIDTH)

        bookTitleEntry.grid(row=0, column=1, pady=5)
        authorNameEntry.grid(row=1, column=1, pady=5)
        yearPublishedEntry.grid(row=2, column=1, pady=5)
        pageLengthEntry.grid(row=3, column=1, pady=5)

        entryFrame.grid(row=1, column=0, pady=40)

        # Construct the frame for entering ISBN numbers
        isbnFrame = tkinter.Frame(self.addBookFrame, padx=10)

        isbnLabel = \
            tkinter.Label(isbnFrame, text="Enter a book's ISBN number:            ", font="TkFixedFont")

        isbnEntry = \
            tkinter.Entry(isbnFrame, textvariable=self.isbn, font="TkFixedFont", width=_ENTRY_WIDTH)

        isbnButton = \
            tkinter.Button(isbnFrame, text="PULL ISBN INFO", command=self._ISBNEvent,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        isbnLabel.grid(row=0, column=0)
        isbnEntry.grid(row=0, column=1)
        isbnButton.grid(row=1, column=0, pady=40)

        isbnFrame.grid(row=0, column=0, pady=20)

        # Construct the add and cancel button frame
        addCancelFrame = tkinter.Frame(self.addBookFrame, padx=10)

        addButton = \
            tkinter.Button(addCancelFrame, text="ADD BOOK", command=self._addEvent,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)
        cancelButton = \
            tkinter.Button(addCancelFrame, text="CANCEL", command=self.cancelFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        addButton.grid(row=0, column=0, padx=20)
        cancelButton.grid(row=0, column=1)
        addCancelFrame.grid(row=2, column=0)

        # Draw the frame to the window
        self.addBookFrame.pack(padx=5, pady=5)

        # End of build()

    def destroy(self) -> None:
        """
        Destroys the widgets held by this frame. This effectively un-draws the frame from the GUI.

        :return: None
        """

        self.addBookFrame.destroy()
        self.addBookFrame = None

        self._clearEntries()

        # End of destroy()

    def _addEvent(self) -> None:
        """
        Takes in the values entered into the book title, author name, year published, and page length fields and
        uses them to add a book to the currently loaded collection.

        :return: None
        """

        # Test whether any of the book attribute entry fields are empty
        hadMissingField = False
        errorMessage = "Cannot add book with missing fields!\n\nRequired fields that still need entries:"

        if self.bookTitle.get() == "":
            errorMessage += "\nTitle"
            hadMissingField = True
        if self.authorName.get() == "":
            errorMessage += "\nTitle"
            hadMissingField = True
        if self.yearPublished.get() == "":
            errorMessage += "\nTitle"
            hadMissingField = True
        if self.pageLength.get() == "":
            errorMessage += "\nTitle"
            hadMissingField = True

        # If any fields were missing, print the error message and end the event
        if hadMissingField:
            messagebox.showerror("ERROR", errorMessage)
            return

        # Otherwise, attempt to use the values from the book attribute fields to add a book to the current collection
        try:
            FileLoader.addBook(self.bookCollection,
                               self.bookTitle.get(),
                               self.authorName.get(),
                               self.yearPublished.get(),
                               self.pageLength.get())

        # If the attempt failed, show an error
        except FileLoader.InputError as message:
            messagebox.showerror("ERROR", message)
            return
        except OSError:
            messagebox.showerror("ERROR", "The collection was either deleted outside the program or cannot be written" +
                                 " to!\n\nReturning to main menu...")
            self.crashToMainMenuFunction()
            return

        # Otherwise, show the book added
        messagebox.showinfo("BOOK ADDED SUCCESSFULLY",
                            "Successfully added the new book!" +
                            "\n\nTitle:\n" + self.bookTitle.get() +
                            "\n\nAuthor:\n" + self.authorName.get() +
                            "\n\nYear Published:\n" + self.yearPublished.get() +
                            "\n\nPage Length:\n" + self.pageLength.get())

        self._clearEntries()

        # End of addEvent()

    def _ISBNEvent(self) -> None:
        """
        Takes the value entered into the isbn entry field and fills the other entry fields with data pulled
        using BookAPI and the specified number.

        :return: None
        """

        # If the ISBN number is empty, just show an error
        if self.isbn.get() == "":
            messagebox.showerror("ERROR", "No ISBN number was entered!")
            return

        # Attempt to construct the BookAPI object for the entered ISBN number
        bookAPIData = None

        try:
            bookAPIData = BookAPI(self.isbn.get())

        except ISBNAPI.ConnectionError as message:
            messagebox.showerror("ERROR", message)
            return

        except ISBNAPI.URLError as message:
            messagebox.showerror("ERROR", message)
            return

        except ISBNAPI.InputError as message:
            messagebox.showerror("ERROR", message)
            return

        # To hold the amount of attributes returned from the API
        dataPointsRetrieved = 0

        # To hold the message to show to the user as to what was pulled from the API
        completeMessage = "ISBN pull complete!"
        pulledMessage = "\n\nPulled the following information for the new book:"
        nonPulledMessage = "\n\nCould not pull the following information:"

        # Go through and determine what attributes were loaded, assign them to the entries and the output message as
        # appropriate
        if bookAPIData.title != "":
            dataPointsRetrieved += 1
            pulledMessage += "\n\nTitle:\n" + bookAPIData.title
        else:
            nonPulledMessage += "\nTitle"

        if bookAPIData.author != "":
            dataPointsRetrieved += 1
            pulledMessage += "\n\nAuthor:\n" + bookAPIData.author
        else:
            nonPulledMessage += "\nAuthor"

        if bookAPIData.yearPub != "":
            dataPointsRetrieved += 1
            pulledMessage += "\n\nYear Published:\n" + str(bookAPIData.yearPub)
        else:
            nonPulledMessage += "\nYear Published"

        if bookAPIData.pageCount != "":
            dataPointsRetrieved += 1
            pulledMessage += "\n\nPage Count:\n" + str(bookAPIData.pageCount)
        else:
            nonPulledMessage += "\nPage Count"

        self.bookTitle.set(bookAPIData.title)
        self.authorName.set(bookAPIData.author)
        self.yearPublished.set(bookAPIData.yearPub)
        self.pageLength.set(bookAPIData.pageCount)

        # Show the pull completion message based on what attributes were loaded
        if dataPointsRetrieved == 0:
            messagebox.showinfo("PULL COMPLETE",
                                completeMessage + "\n\nCould not pull any information for the given ISBN.")
        elif dataPointsRetrieved == 4:
            messagebox.showinfo("PULL COMPLETE",
                                completeMessage + pulledMessage )
        else:
            messagebox.showinfo("PULL COMPLETE",
                                completeMessage + pulledMessage + nonPulledMessage)

        # End of ISBNEvent()

    def _clearEntries(self) -> None:
        """
        Clears out the text within the entry widgets.

        :return: None
        """

        self.bookTitle.set("")
        self.authorName.set("")
        self.yearPublished.set("")
        self.pageLength.set("")
        self.isbn.set("")

        # End of clearEntries()

    # End of ViewCollectionFrame
