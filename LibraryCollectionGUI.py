# LibraryCollectionGUI.py
#
# GUI widget code and tkinter usage adapted from:
# https://realpython.com/python-gui-tkinter/
# https://tkdocs.com/tutorial
# https://docs.python.org/3/library/tkinter.html

import tkinter
from tkinter import filedialog
from tkinter import messagebox

from MainMenuFrame import MainMenuFrame
from CreditsFrame import CreditsFrame
from CollectionMenuFrame import CollectionMenuFrame
from ViewCollectionFrame import ViewCollectionFrame
from AddBookFrame import AddBookFrame
from InstructionsFrame import InstructionsFrame

import os

import FileLoader

# Constants for the window length and width
_WINDOW_WIDTH = 800
_WINDOW_LENGTH = 600

# Constants for the button length and width
_BUTTON_WIDTH = 15
_BUTTON_LENGTH = 2


class LibraryCollectionGUI:
    """
    Defines LibraryCollectionGUI objects.

    Once instantiated, invoking start() will initialize the program for use by the user.

    The GUI will allow the user to:
    View the program's instructions
    View the credits
    Load a collection from a directory
    View a specified collection
    Add a book to a collection
    Delete a book from a collection

    """

    def __init__(self):
        """
        Default constructor of LibraryCollectionGUI.

        Start the GUI with start()
        """

        self.window = tkinter.Tk()

        self.window.title("Library Collection Manager")
        self.window.resizable(False, False)
        self.window.minsize(_WINDOW_WIDTH, _WINDOW_LENGTH)
        self.window.maxsize(_WINDOW_WIDTH, _WINDOW_LENGTH)

        self.mainMenuFrame = None
        self.creditsFrame = None
        self.collectionMenuFrame = None
        self.viewCollectionFrame = None
        self.addBookFrame = None
        self.instructionsFrame = None

        self.activeCollection = None

        # End of init()

    def start(self) -> None:
        """
        Constructs the screens for the GUI, draws the main menu to the user, and starts the GUI window's main
        event loop.

        Invoke when starting the GUI program.

        :return: None
        """

        # Build each of the needed frames to run the GUI
        self.mainMenuFrame = MainMenuFrame(self.window, self._openCollectionEvent, self._instructionsEvent,
                                           self._creditsEvent, self._quitEvent)

        self.creditsFrame = CreditsFrame(self.window, self._creditsBackEvent)

        self.collectionMenuFrame = CollectionMenuFrame(self.window, "TEMP", self._collectionViewBooksEvent,
                                                       self._collectionAddBookEvent, self._collectionBackEvent)

        self.viewCollectionFrame = ViewCollectionFrame(self.window, self.activeCollection,
                                                       self._viewCollectionBackEvent,
                                                       self._crashViewCollectionToMainMenuEvent)

        self.addBookFrame = AddBookFrame(self.window, self.activeCollection, self._cancelAddBookEvent,
                                         self._crashAddBookToMainMenuEvent)

        self.instructionsFrame = InstructionsFrame(self.window, self._instructionsBackEvent)

        # Draw the main menu and start the GUI event loop
        self.mainMenuFrame.draw()

        self.window.mainloop()

        # End of start()

    #
    #
    # MAIN MENU FRAME EVENTS
    #
    #
    def _openCollectionEvent(self) -> None:
        """
        Button Event Function to give the main menu frame's "OPEN COLLECTION" button.

        Presents a dialog to the user to get the directory of the collection to load, and then loads that directory.

        Destroys the main menu frame and draws the collection menu frame.

        :return: None
        """

        # Prompt the user for a directory to use as the collection using their file explorer
        directoryPath = filedialog.askdirectory()

        # If the user canceled the dialog, abort the event
        if directoryPath == "":
            return

        # Otherwise, load the directory's collection into the back end and pass it to the collection menu frame
        else:
            # Attempt to load the directory path and the .book files contained therein
            try:
                self.activeCollection = FileLoader.loadFile(directoryPath)

            # If failed, show an error pop-up and end the event
            except FileLoader.BadPathError as message:
                messagebox.showerror("ERROR", message)
                return

            # If successful, show a success pop-up and send the collection name to the collection frame
            messagebox.showinfo("LOAD COMPLETE", f"Successfully Loaded: {os.path.basename(directoryPath)}!")
            self.collectionMenuFrame.collectionName = os.path.basename(directoryPath)

        # Draw the collection menu
        self.mainMenuFrame.destroy()

        self.collectionMenuFrame.draw()

        # End of openLibraryCollectionEvent()

    def _instructionsEvent(self) -> None:
        """
        Button Event Function to give the main menu frame's "INSTRUCTIONS" button.

        Destroys the main menu frame and draws the instructions frame.

        :return: None
        """

        self.mainMenuFrame.destroy()

        self.instructionsFrame.draw()

        # End of instructionsEvent()

    def _creditsEvent(self) -> None:
        """
        Button Event Function to give the main menu frame's "CREDITS" button.

        Destroys the main menu frame and draws the credits frame.

        :return: None
        """

        self.mainMenuFrame.destroy()

        self.creditsFrame.draw()

        # End of creditsEvent()

    def _quitEvent(self) -> None:
        """
        Button Event Function to give the main menu frame's "QUIT" button.

        Quits the program.

        :return: None
        """

        self.window.destroy()

        quit()

        # End of quitEvent()

    #
    #
    # CREDITS FRAME EVENTS
    #
    #
    def _creditsBackEvent(self) -> None:
        """
        Button Event Function to give the credits frame's "BACK" button.

        Destroys the credits frame and draws the main menu frame

        :return:
        """

        self.creditsFrame.destroy()

        self.mainMenuFrame.draw()

        # End of creditsBackEvent

    #
    #
    # INSTRUCTIONS FRAME EVENTS
    #
    #
    def _instructionsBackEvent(self) -> None:
        """
        Button Event Function to give the instructions frame's "BACK" button.

        Destroys the instructions frame and draws the main menu frame

        :return:
        """

        self.instructionsFrame.destroy()

        self.mainMenuFrame.draw()

        # End of instructionsBackEvent()

    #
    #
    # COLLECTION MENU FRAME EVENTS
    #
    #
    def _collectionViewBooksEvent(self) -> None:
        """
        Button Event Function to give the collection menu frame's "VIEW COLLECTION" button.

        Destroys the collection menu frame and draws the view collection frame.

        Will not draw the screen if the directory was deleted or the collection is empty.

        :return: None
        """

        # Ensure that the directory still exists by attempting to reload the directory path and the .book files
        # contained therein
        try:
            self.activeCollection = FileLoader.loadFile(self.activeCollection.path)
        # If failed, show an error pop-up and end the event
        except FileLoader.BadPathError:
            messagebox.showerror("ERROR", "The entire collection directory was removed outside the program!" +
                                 "\n\nReturning to main menu...")
            self._collectionBackEvent()
            return

        # Send the loaded .book files into the view collection frame
        self.viewCollectionFrame.bookCollection = self.activeCollection

        # Attempt to draw the view collection frame, if the collection is empty, abort the event
        try:
            self.viewCollectionFrame.draw()
            self.collectionMenuFrame.destroy()
        except AttributeError:
            messagebox.showerror("ERROR", "Cannot show empty collection!")
            return

        # End of collectionViewBooksEvent()

    def _collectionAddBookEvent(self) -> None:
        """
        Button Event Function to give the collection menu frame's "ADD BOOK" button.

        Destroys the collection menu frame and draws the add book frame.

        :return:
        """

        # Send the loaded .book files into the view collection frame
        self.addBookFrame.bookCollection = self.activeCollection

        self.collectionMenuFrame.destroy()

        self.addBookFrame.draw()

        # End of collectionAddBookEvent()

    def _collectionBackEvent(self) -> None:
        """
        Button Event Function to give the collection menu frame's "BACK" button.

        Destroys the collection menu frame and draws the main menu frame.

        :return: None
        """

        self.collectionMenuFrame.destroy()

        self.mainMenuFrame.draw()

        # End of collectionBackEvent()

    #
    #
    # VIEW COLLECTION EVENTS
    #
    #
    def _viewCollectionBackEvent(self) -> None:
        """
        Button Event Function to give the view collection frame's "BACK" button.

        Destroys the view collection frame and draws the collection menu frame.

        :return: None
        """

        self.viewCollectionFrame.destroy()

        self.collectionMenuFrame.draw()

        # End of viewCollectionBackEvent()

    def _crashViewCollectionToMainMenuEvent(self) -> None:
        """
        Event to occur if the directory is deleted while viewing the collection.

        Destroys the view collection frame and draws the main menu frame.

        :return: None
        """

        self.viewCollectionFrame.destroy()

        self.mainMenuFrame.draw()

        # End of crashViewCollectionToMainMenuEvent()

    #
    #
    # ADD BOOK EVENTS
    #
    #
    def _cancelAddBookEvent(self) -> None:
        """
        Button Event Function to give the add book frame's "CANCEL" button.

        Destroys the add book frame and draws the collection menu frame.

        :return:
        """

        self.addBookFrame.destroy()

        self.collectionMenuFrame.draw()

        # End of cancelAddBookEvent

    def _crashAddBookToMainMenuEvent(self) -> None:
        """
        Event to occur if the directory is deleted while adding a book.

        Destroys the view collection frame and draws the main menu frame.

        :return: None
        """

        self.addBookFrame.destroy()

        self.mainMenuFrame.draw()

        # End of crashAddBookToMainMenuEvent()

    # End of LibraryCollectionGUI
