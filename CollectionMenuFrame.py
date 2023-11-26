# CollectionMenuFrame.py
#
# GUI widget code and tkinter usage adapted from:
# https://realpython.com/python-gui-tkinter/
# https://tkdocs.com/tutorial
# https://docs.python.org/3/library/tkinter.html

import tkinter

# Constants for the button length and width
_BUTTON_WIDTH = 15
_BUTTON_LENGTH = 2


class CollectionMenuFrame:
    """
    Defines CollectionMenuFrame objects.

    Contains the widgets needed to operate the Collection Menu for the LibraryCollectionGUI.

    The frame can be drawn to the GUI using draw(), or removed from the GUI using destroy().

    """

    def __init__(self, window: tkinter.Tk, collectionName: str,
                 viewBooksFunction, addBookFunction, backFunction):
        """
        Constructs the CollectionMenuFrame for the specified window.

        :param window: The window to set as the master for this frame.
        :param collectionName: The name for the collection.
        :param viewBooksFunction: The function to invoke when the user selects "VIEW COLLECTION".
        :param addBookFunction: The function to invoke when the user selects "ADD BOOK".
        :param backFunction: The function to invoke when the user selects "BACK".
        """

        self.window = window
        self.collectionMenuFrame = None

        self.collectionName = collectionName

        self.addBookFunction = addBookFunction
        self.viewBooksFunction = viewBooksFunction
        self.backFunction = backFunction

        # End of init()

    def draw(self) -> None:
        """
        Draws the CollectionMenuFrame widgets to the window.

        :return: None
        """

        # Construct the frame
        self.collectionMenuFrame = tkinter.Frame(self.window, pady=150)

        # Construct the label to present the collection name
        collectionLabel = tkinter.Label(self.collectionMenuFrame,
                                        text=f"Collection: {self.collectionName}",
                                        font="TkFixedFont")

        collectionLabel.grid(row=0, column=0, pady=50)

        # Construct the frame of buttons to transition to the GUI's different screens (or back out)
        collectionMenuButtonFrame = tkinter.Frame(self.collectionMenuFrame)
        collectionMenuButtonFrame.grid(row=1, column=0)

        viewCollectionButton = \
            tkinter.Button(collectionMenuButtonFrame, text="VIEW COLLECTION", command=self.viewBooksFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        addBookButton = \
            tkinter.Button(collectionMenuButtonFrame, text="ADD BOOK", command=self.addBookFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)
        backButton = \
            tkinter.Button(collectionMenuButtonFrame, text="BACK", command=self.backFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        viewCollectionButton.grid(row=0, column=0, pady=10)
        addBookButton.grid(row=1, column=0, pady=10)
        backButton.grid(row=3, column=0, pady=10)

        # Draw the frame to the window
        self.collectionMenuFrame.pack(padx=5, pady=5)

        # End of build()

    def destroy(self) -> None:
        """
        Destroys the widgets held by this frame. This effectively un-draws the frame from the GUI.

        :return: None
        """

        self.collectionMenuFrame.destroy()
        self.collectionMenuFrame = None

        # End of destroy()

    # End of CollectionMenuFrame
