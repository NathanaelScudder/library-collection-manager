# ViewCollectionFrame.py
#
# GUI widget code and tkinter usage adapted from:
# https://realpython.com/python-gui-tkinter/
# https://tkdocs.com/tutorial
# https://docs.python.org/3/library/tkinter.html

import tkinter
from tkinter import messagebox

import time

from FileLoader import Library, BookNotFoundError, BadPathError
import FileLoader

import sortModules

import copy

# Constants for the button length and width
_BUTTON_WIDTH = 15
_BUTTON_LENGTH = 2

# Constants for sorting keywords
_SORT_TITLE = "Title         "
_SORT_AUTHOR = "Author        "
_SORT_YEAR_PUBLISHED = "Year Published"
_SORT_PAGE_LENGTH = "Page Length   "
_SORT_DATE_ADDED = "Date Added    "


class ViewCollectionFrame:
    """
    Defines ViewCollectionFrame objects.

    Contains the widgets needed to operate the View Collection screen for the LibraryCollectionGUI.

    The frame can be drawn to the GUI using draw(), or removed from the GUI using destroy().

    """

    def __init__(self, window: tkinter.Tk, bookCollection: Library, backFunction, crashToMainMenuFunction):
        """
        Constructs the ViewCollectionFrame for the specified window.

        :param window: The window to set as the master for this frame.
        :param bookCollection: The list of books to let the user view using the frame.
        :param backFunction: The function to invoke when the user selects "BACK".
        :param crashToMainMenuFunction: The function to invoke if the collection is removed outside the program
        """

        self.window = window
        self.viewCollectionFrame = None
        self.currentBookTextArea = None

        self.backFunction = backFunction

        self.crashToMainMenuFunction = crashToMainMenuFunction

        self.bookCollection = bookCollection

        # To hold which book the user is currently viewing in the list
        self.currentBookIndex = 0

        # To hold the sorting technique currently in use
        self.sortingTechnique = tkinter.StringVar(value=_SORT_TITLE)

        # End of init()

    def draw(self) -> None:
        """
        Draws the ViewCollectionFrame widgets to the window.

        :return: None
        :raises AttributeError: If the current collection is empty
        """

        # To hold the text of the first book to draw
        currentBookText = None
        self.currentBookIndex = 0

        # Get the current book as formatted text, or raise an AttributeError if the list was empty
        try:
            # Sort the library by book title by default
            sortModules.sortByTitle(self.bookCollection)

            currentBookText = self._getCurrentBookText()
        except IndexError:
            raise AttributeError()
        except ValueError:
            raise AttributeError()

        # Construct the frame
        self.viewCollectionFrame = tkinter.Frame(self.window, pady=50)

        # Construct the text box to show book information
        # Text setup adapted from https://tkdocs.com/tutorial/text.html
        textFrame = tkinter.Frame(self.viewCollectionFrame)

        self.currentBookTextArea = tkinter.Text(textFrame, bg="white", width=70, height=15, wrap="none",
                                                font="TkFixedFont")

        scrollBar = tkinter.Scrollbar(textFrame, orient=tkinter.HORIZONTAL, command=self.currentBookTextArea.xview)
        self.currentBookTextArea["xscrollcommand"] = scrollBar.set

        self.currentBookTextArea.insert("1.0", currentBookText)
        self.currentBookTextArea["state"] = "disabled"

        self.currentBookTextArea.grid(row=0, column=0)
        scrollBar.grid(row=1, column=0, sticky=(tkinter.W, tkinter.E))
        textFrame.grid(row=0, column=0, pady=50)

        # Construct the frame of buttons to designate which book is being viewed
        upDownButtonFrame = tkinter.Frame(self.viewCollectionFrame, padx=10, pady=10)

        upButton = \
            tkinter.Button(upDownButtonFrame, text="PREVIOUS BOOK", command=self._up,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        downButton = \
            tkinter.Button(upDownButtonFrame, text="NEXT BOOK", command=self._down,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        upButton.grid(row=0, column=0)
        downButton.grid(row=1, column=0)
        upDownButtonFrame.grid(row=0, column=1)

        # Construct the frame of radio buttons for determining the sorting technique
        sortingButtonFrame = tkinter.Frame(self.viewCollectionFrame, padx=10)

        sortingLabel = \
            tkinter.Label(sortingButtonFrame, text="Sort Books By:", font="TkFixedFont")

        sortTitleButton = \
            tkinter.Radiobutton(sortingButtonFrame, text=_SORT_TITLE, variable=self.sortingTechnique,
                                value=_SORT_TITLE, command=self._radioSortEvent, font="TkFixedFont")

        sortAuthorButton = \
            tkinter.Radiobutton(sortingButtonFrame, text=_SORT_AUTHOR, variable=self.sortingTechnique,
                                value=_SORT_AUTHOR, command=self._radioSortEvent, font="TkFixedFont")

        sortYearPublishedButton = \
            tkinter.Radiobutton(sortingButtonFrame, text=_SORT_YEAR_PUBLISHED,
                                variable=self.sortingTechnique, value=_SORT_YEAR_PUBLISHED,
                                command=self._radioSortEvent, font="TkFixedFont")

        sortPageLengthButton = \
            tkinter.Radiobutton(sortingButtonFrame, text=_SORT_PAGE_LENGTH,
                                variable=self.sortingTechnique, value=_SORT_PAGE_LENGTH,
                                command=self._radioSortEvent, font="TkFixedFont")

        sortDateAddedButton = \
            tkinter.Radiobutton(sortingButtonFrame, text=_SORT_DATE_ADDED,
                                variable=self.sortingTechnique, value=_SORT_DATE_ADDED,
                                command=self._radioSortEvent, font="TkFixedFont")

        sortingLabel.grid(row=0, column=0)
        sortTitleButton.grid(row=1, column=0)
        sortAuthorButton.grid(row=2, column=0)
        sortYearPublishedButton.grid(row=3, column=0)
        sortPageLengthButton.grid(row=4, column=0)
        sortDateAddedButton.grid(row=5, column=0)
        sortingButtonFrame.grid(row=1, column=1)

        # Construct the back and delete button frame
        deleteBackFrame = tkinter.Frame(self.viewCollectionFrame, padx=10)

        deleteButton = \
            tkinter.Button(deleteBackFrame, text="DELETE BOOK", command=self._deleteEvent,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)
        backButton = \
            tkinter.Button(deleteBackFrame, text="BACK TO MENU", command=self.backFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        deleteButton.grid(row=0, column=0, padx=20)
        backButton.grid(row=0, column=1)
        deleteBackFrame.grid(row=1, column=0)

        # Draw the frame to the window
        self.viewCollectionFrame.pack(padx=5, pady=5)

        # End of build()

    def destroy(self) -> None:
        """
        Destroys the widgets held by this frame. This effectively un-draws the frame from the GUI.

        :return: None
        """

        if self.viewCollectionFrame is not None:
            self.viewCollectionFrame.destroy()

        self.viewCollectionFrame = None
        self.currentBookTextArea = None

        # End of destroy()

    def _up(self) -> None:
        """
        Button Event Function to give the view collection frame's "UP" button.

        Draws the previous book's attributes to the GUI.

        :return: None
        """

        # If the user is at the first book in the list (i.e. can't go back) present an error dialog and abort the event
        if self.currentBookIndex == 0:
            messagebox.showerror("ERROR", "Reached beginning of collection. Cannot go further back!")
        else:
            self.currentBookIndex -= 1
            self._drawCurrentBook()

        # End of up()

    def _down(self) -> None:
        """
        Button Event Function to give the view collection frame's "DOWN" button.

        Draws the next book's attributes to the GUI.

        :return: None
        """

        # If the user is at the last book in the list (i.e. can't go forward)
        # present an error dialog and abort the event
        if self.currentBookIndex >= len(self.bookCollection.bookList) - 1:
            messagebox.showerror("ERROR", "Reached end of collection. Cannot go further forward!")
        else:
            self.currentBookIndex += 1
            self._drawCurrentBook()

        # End of down()

    def _drawCurrentBook(self) -> None:
        """
        Draws the book at the current index within the held list of books.

        :return: None
        :raises AttributeError: If the current collection is empty
        """

        # Get the text for the current book in the list, if the collection is empty, raise an AttributeError.
        currentBookText = None

        try:
            currentBookText = self._getCurrentBookText()
        except ValueError:
            raise AttributeError()

        # Enable the text area for edits
        self.currentBookTextArea["state"] = "normal"

        # Remove the text currently in the text area
        self.currentBookTextArea.delete("1.0", tkinter.END)

        # Add the book text to the text area
        self.currentBookTextArea.insert("1.0", currentBookText)

        # Disable the text area for edits so that the user cannot change the book text
        self.currentBookTextArea["state"] = "disabled"

        # End of drawCurrentBook()

    def _getCurrentBookText(self) -> str:
        """
        Returns the index and attributes of the current book in a formatted table.

        :return: The index and attributes of the current book in a formatted table as a string.
        :raises IndexError: If the current collection is empty
        """

        # Get the current book
        currentBook = self.bookCollection.bookList[self.currentBookIndex]

        # Get the max length of the book's attributes, and set the bar length to that value plus 3
        barLength = max([len(currentBook.title), len(currentBook.author), len(str(currentBook.yearPub)),
                         len(str(currentBook.pageLength)),
                         len(time.asctime(time.localtime(float(currentBook.dateAdded))))]) + 3

        return "|-----------------|" + ("-" * barLength) + (" " * 5) + \
               f"\n| Book Number     | {self.currentBookIndex + 1} of {len(self.bookCollection.bookList)}" + \
               "\n|-----------------|" + ("-" * barLength) + (" " * 5) + \
               "\n|-----------------|" + ("-" * barLength) + (" " * 5) + \
               f"\n| Title           | {currentBook.title}" + \
               "\n|-----------------|" + ("-" * barLength) + (" " * 5) + \
               f"\n| Author          | {currentBook.author}" + \
               "\n|-----------------|" + ("-" * barLength) + (" " * 5) + \
               f"\n| Year Published  | {currentBook.yearPub}" + \
               "\n|-----------------|" + ("-" * barLength) + (" " * 5) + \
               f"\n| Page Length     | {currentBook.pageLength}" + \
               "\n|-----------------|" + ("-" * barLength) + (" " * 5) + \
               f"\n| Date Added      | {time.asctime(time.localtime(float(currentBook.dateAdded)))}" + \
               "\n|-----------------|" + ("-" * barLength) + (" " * 5)

        # End of getCurrentBookText()

    def _radioSortEvent(self) -> None:
        """
        Sorts the books held in the collection by the technique specified by the clicked radio button widget.

        Also draws the current book according to the new ordering.

        :return: None
        """

        # Get the technique by which the user wishes to sort the books
        sortingTechnique = self.sortingTechnique.get()

        # Sort the books according to the selected technique
        if sortingTechnique == _SORT_TITLE:
            sortModules.sortByTitle(self.bookCollection)
        elif sortingTechnique == _SORT_AUTHOR:
            sortModules.sortByAuthor(self.bookCollection)
        elif sortingTechnique == _SORT_YEAR_PUBLISHED:
            sortModules.sortByYear(self.bookCollection)
        elif sortingTechnique == _SORT_PAGE_LENGTH:
            sortModules.sortByPages(self.bookCollection)
        elif sortingTechnique == _SORT_DATE_ADDED:
            sortModules.sortByDate(self.bookCollection)

        # Redraw the new current book
        self._drawCurrentBook()
        return

        # End of radioTitleEvent()

    def _deleteEvent(self) -> None:
        """
        Deletes the book the user is currently viewing from the collection.

        :return: None
        """

        # Get the book the view is currently viewing
        currentBook = None

        try:
            currentBook = self.bookCollection.bookList[self.currentBookIndex]
        except IndexError:
            messagebox.showerror("ERROR", "No book to delete!")
            return

        # Attempt to delete the book from the collection using its date added
        try:
            # Ask the user to confirm the deletion, otherwise end the event
            if not messagebox.askokcancel("CONFIRM BOOK DELETION", "Confirm the book to delete:\n\n" +
                                                                   "Title:\n" + currentBook.title +
                                                                   "\n\nAuthor(s):\n" + currentBook.author +
                                                                   "\n\nYear Published:\n" + str(currentBook.yearPub) +
                                                                   "\n\nDated Added:\n" +
                                                                   time.asctime(
                                                                       time.localtime(float(currentBook.dateAdded)))):
                return

            FileLoader.deleteBook(self.bookCollection, currentBook.dateAdded)
            messagebox.showinfo("BOOK DELETED", "The book was deleted successfully.")

            # If that removed the last book in the list, back out of this menu,
            # otherwise, draw the new current book
            if len(self.bookCollection.bookList) == 0:
                messagebox.showwarning("ALL BOOKS REMOVED", "The last book was removed from the collection!")

                self.backFunction()
            else:
                # if the current index is the last index, we need to decrement the number
                if self.currentBookIndex == len(self.bookCollection.bookList):
                    self.currentBookIndex -= 1

                self._drawCurrentBook()

        # If the deletion failed, a .book file was removed outside the program, restart the view collection frame
        except BookNotFoundError as message:
            # Tell the user what happened with message boxes
            messagebox.showerror("ERROR", message)
            messagebox.showinfo("RESTARTING WINDOW", "A book file was removed outside the program." +
                                "\n\nThe collection view will restart!")

            # Attempt to reload the library's directory
            updatedLibrary = None

            try:
                updatedLibrary = FileLoader.loadFile(self.bookCollection.path)

            # If the entire directory is missing, jump back to the main menu
            except BadPathError:
                messagebox.showinfo("ATTENTION", "The entire collection directory was removed outside the program!" +
                                    "\n\nReturning to main menu...")
                self.crashToMainMenuFunction()
                return

            # Copy the newly loaded library's books and save it to this one
            self.bookCollection.bookList = copy.deepcopy(updatedLibrary.bookList)

            # Attempt to re-draw the view collection frame
            try:
                self.destroy()
                self.draw()

            # If the collection was empty, back out of this menu
            except AttributeError:
                messagebox.showinfo("ATTENTION", "The collection directory no longer contains any books!")

                self.backFunction()
                return

        # End of deleteEvent()

    # End of ViewCollectionFrame
