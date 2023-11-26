# InstructionsFrame.py
#
# GUI widget code and tkinter usage adapted from:
# https://realpython.com/python-gui-tkinter/
# https://tkdocs.com/tutorial
# https://docs.python.org/3/library/tkinter.html

import tkinter

# Constants for the button length and width
_BUTTON_WIDTH = 15
_BUTTON_LENGTH = 2

# Constants for the ListBox labels
_OPEN_COLLECTION_LABEL = "Opening a Collection"
_VIEW_COLLECTION_LABEL = "Viewing a Collection"
_ADD_BOOK_LABEL = "Adding a Book"
_DELETE_BOOK_LABEL = "Deleting a Book"
_SORTING_BOOKS_LABEL = "Sorting a Collection"
_ISBN_LABEL = "Using an ISBN"
_DIVIDER = "--------------------"

_TUTORIAL_LABELS = [_DIVIDER,
                    _OPEN_COLLECTION_LABEL,
                    _DIVIDER,
                    _VIEW_COLLECTION_LABEL,
                    _DIVIDER,
                    _ADD_BOOK_LABEL,
                    _DIVIDER,
                    _DELETE_BOOK_LABEL,
                    _DIVIDER,
                    _SORTING_BOOKS_LABEL,
                    _DIVIDER,
                    _ISBN_LABEL,
                    _DIVIDER]

# Constants for instruction strings
_WELCOME_INSTRUCTION =\
    "Hello!" +\
    "\n\nWelcome to the Library Collection Manager by Jeff Hover and Nathanael Scudder!" +\
    "\n\nThis program allows you to create, add to, delete from, and view a collection of books " +\
    "and their title, author, page count, and year published." +\
    "\n\nFor more information, please pick a tutorial point on the left."

_OPEN_COLLECTION_INSTRUCTION =\
    f"{_OPEN_COLLECTION_LABEL}:" +\
    '\n\nWhen clicking "OPEN COLLECTION" on the main menu, you will have the opportunity to designate a directory to' +\
    ' use as the destination for any added books.' +\
    "\n\nNewly added books will be entered into the designated directory as .book files " +\
    "(these .book files are not meant to be tampered with outside the program)." +\
    "\n\nAny directory can be designated, regardless of its contents." +\
    "\n\nAlternatively, a new directory can be created using the opened file explorer window and used as the" +\
    " destination for any new books." +\
    "\n\nAfter designating a directory, any .book files that exist in the directory (but not inner-directories)" +\
    " will be loaded into the collection, which can then be viewed and or deleted."

_VIEW_COLLECTION_INSTRUCTION =\
    f"{_VIEW_COLLECTION_LABEL}:" +\
    f'\n\nOnce a collection has been opened (see "{_OPEN_COLLECTION_LABEL}"), you can click "VIEW COLLECTION" to' +\
    ' view the list of books in the current collection.' +\
    "\n\nIf the collection does not contain any books yet, you will not be able to view the collection." +\
    '\n\nAfter selecting "VIEW COLLECTION", you can click "NEXT BOOK" to advance through the collection and view' +\
    'the different book\'s title, author, year published, page length, and date added to the collection. ' +\
    'You can also click "PREVIOUS BOOK" to go backwards through the collection. However, the collection does not wrap.'\
    + f"\n\nAdditionally from this menu, you can click \"DELETE BOOK\" to delete books (see \"{_DELETE_BOOK_LABEL}\")"

_ADD_BOOK_INSTRUCTION =\
    f"{_ADD_BOOK_LABEL}:" +\
    f'\n\nOnce a collection has been opened (see "{_OPEN_COLLECTION_LABEL}"), you can click "ADD BOOK" to ' +\
    "enter a book's details in the form of its title, author, publishing year, and page length." +\
    "\n\nTo enter these details for a book, simply fill in the corresponding entry fields with the proper" +\
    " information, and click \"ADD BOOK\"" +\
    f"\n\nAlternatively, some or all of the book's information can be automatically filled using its ISBN number" +\
    f" (see \"{_ISBN_LABEL}\")."

_DELETE_BOOK_INSTRUCTION =\
    f"{_DELETE_BOOK_LABEL}:" +\
    f'\n\nOnce a collection has been viewed (see "{_VIEW_COLLECTION_LABEL}"), you can click "DELETE BOOK" to' +\
    "delete the currently viewed book from the collection." +\
    "\n\nDeleting the book will set the view screen to the previous book." +\
    "\n\nIf the last book in a collection is deleted, you will be sent back to the previous screen."

_SORTING_BOOKS_INSTRUCTION =\
    f"{_SORTING_BOOKS_LABEL}:" +\
    f'\n\nOnce a collection has been viewed (see "{_VIEW_COLLECTION_LABEL}"), you can click the five different ' +\
    "radio buttons to change the collection's sorting methodology." +\
    "\n\nChanging the sorting methodology will also affect the book currently being viewed. E.g. if book 1 is" +\
    " being viewed, whatever book is first in the new sorting methodology will be the one to appear in the" +\
    " view screen." +\
    "\n\nBy default, the collection is sorted according to each book's title (in alphabetical order)." +\
    "\n\nSelecting \"Author\" will sort the collection according to each book's author name (in alphabetical order)." +\
    "\n\nSelecting \"Year Published\" will sort the collection according to each book's year published name" +\
    " (in ascending order)." +\
    "\n\nSelecting \"Page Length\" will sort the collection according to each book's page length " +\
    "(in ascending order)." +\
    "\n\nSelecting \"Date Added\" will sort the collection according to each book's date added to the collection" +\
    " (in ascending order)."

_ISBN_INSTRUCTION =\
    f"{_ISBN_LABEL}:" +\
    f'\n\nWhen adding a book (see "{_ADD_BOOK_LABEL}"), you can use a book\'s ISBN to partially or fully fill the' +\
    ' book\'s details.' +\
    "\n\nTo use an ISBN number, simply enter the number with the associated entry field and click \"PULL ISBN INFO\"" +\
    " (this works for ISBN-10 and ISBN-13)." +\
    "\n\nOnce you pull the ISBN info, the entry fields for the book's title, author, publishing year, " +\
    "and page length will be pre-filled using the data pulled from the entered ISBN. " +\
    "However, a provided ISBN does not necessarily contain information for each of the four fields, " +\
    "nor is the data always accurate. " +\
    "In this case, you will have the opportunity to correct or add any missing information by using the associated " +\
    "entry fields." +\
    "\n\nOnce you have pulled the ISBN data and performed any necessary corrections, you can add the book as normal " +\
    f"(see {_ADD_BOOK_LABEL})"

# Constant dict for accessing instruction strings using their label
_INSTRUCTION_DICTIONARY = {_OPEN_COLLECTION_LABEL: _OPEN_COLLECTION_INSTRUCTION,
                           _VIEW_COLLECTION_LABEL: _VIEW_COLLECTION_INSTRUCTION,
                           _ADD_BOOK_LABEL: _ADD_BOOK_INSTRUCTION,
                           _DELETE_BOOK_LABEL: _DELETE_BOOK_INSTRUCTION,
                           _SORTING_BOOKS_LABEL: _SORTING_BOOKS_INSTRUCTION,
                           _ISBN_LABEL: _ISBN_INSTRUCTION}


class InstructionsFrame:
    """
    Defines InstructionsFrame objects.

    Contains the widgets needed to operate the instructions screen for the LibraryCollectionGUI.

    The frame can be drawn to the GUI using draw(), or removed from the GUI using destroy().

    """

    def __init__(self, window: tkinter.Tk, backFunction):
        """
        Constructs the InstructionsFrame for the specified window.

        :param window: The window to set as the master for this frame.
        :param backFunction: The function to invoke when the user selects "BACK".
        """

        self.window = window
        self.instructionsFrame = None
        self.currentInstructionTextArea = None

        self.backFunction = backFunction

        # To hold the which instruction to show
        self.instructionToShow = tkinter.StringVar(value=_WELCOME_INSTRUCTION)

        # To hold the list of tutorials
        self.tutorialListBox = None
        self.tutorialLabels = tkinter.StringVar(value=_TUTORIAL_LABELS)

        # End of init()

    def _insertInstruction(self, selection: int) -> None:
        """
        Inserts the instruction text into the text box for the specified listbox item clicked.

        :param selection: The index of the listbox item clicked.
        :return: None
        """

        # Get the label at the specified index in the list box
        instructionToInsertLabel = _TUTORIAL_LABELS[selection]

        # Attempt to get the instruction for the specified index
        instructionToInsert = ""

        try:
            instructionToInsert = _INSTRUCTION_DICTIONARY[instructionToInsertLabel]

        # If a key error occurred, then a divider was clicked, in which case, do nothing.
        except KeyError:
            return

        # Enable the text area for edits
        self.currentInstructionTextArea["state"] = "normal"

        # Remove the text currently in the text area
        self.currentInstructionTextArea.delete("1.0", tkinter.END)

        # Add the instruction text to the text area
        self.currentInstructionTextArea.insert("1.0", instructionToInsert)

        # Disable the text area for edits so that the user cannot change the book text
        self.currentInstructionTextArea["state"] = "disabled"

        return

        # End of insertInstruction()

    def draw(self) -> None:
        """
        Draws the InstructionsFrame widgets to the window.

        :return: None
        """

        # Construct the frame
        self.instructionsFrame = tkinter.Frame(self.window, pady=20)

        # Construct the text box to show different instructions
        # Text setup adapted from https://tkdocs.com/tutorial/text.html
        textFrame = tkinter.Frame(self.instructionsFrame)

        self.currentInstructionTextArea = tkinter.Text(textFrame, bg="white", width=70, height=25, wrap="none",
                                                       font="TkFixedFont")

        scrollBar = tkinter.Scrollbar(textFrame, orient=tkinter.VERTICAL, command=self.currentInstructionTextArea.yview)
        self.currentInstructionTextArea["yscrollcommand"] = scrollBar.set
        self.currentInstructionTextArea["wrap"] = "word"

        self.currentInstructionTextArea\
            .insert("1.0", _WELCOME_INSTRUCTION)
        self.currentInstructionTextArea["state"] = "disabled"

        self.currentInstructionTextArea.grid(row=0, column=0)
        scrollBar.grid(row=0, column=2, sticky=(tkinter.N, tkinter.S))
        textFrame.grid(row=0, column=1)

        # Construct the list box for selecting the different tutorial points
        self.tutorialListBox = tkinter.Listbox(self.instructionsFrame, listvariable=self.tutorialLabels,
                                               height=6, font="TkFixedFont")
        self.tutorialListBox.bind("<<ListboxSelect>>",
                                  lambda e: self._insertInstruction(self.tutorialListBox.curselection()[0]))

        self.tutorialListBox.grid(row=0, column=0, padx=10, sticky=(tkinter.N, tkinter.S))

        # Create the back button
        backButton = \
            tkinter.Button(self.instructionsFrame, text="BACK", command=self.backFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        backButton.grid(row=1, column=1, pady=10)

        # Draw the frame to the window
        self.instructionsFrame.pack(padx=5, pady=5)

        # End of build()

    def destroy(self) -> None:
        """
        Destroys the widgets held by this frame. This effectively un-draws the frame from the GUI.

        :return: None
        """

        self.instructionsFrame.destroy()
        self.instructionsFrame = None

        # End of destroy()

    # End of MainMenuFrame
