# MainMenuScreen.py

import tkinter

# Constants for the button length and width
_BUTTON_WIDTH = 15
_BUTTON_LENGTH = 2


class MainMenuFrame:
    """
    Defines MainMenuFrame objects.

    Contains the widgets needed to operate the Main Menu for the LibraryCollectionGUI.

    The frame can be drawn to the GUI using draw(), or removed from the GUI using destroy().

    """

    def __init__(self, window: tkinter.Tk, openCollectionFunction, instructionsFunction, creditsFunction, quitFunction):
        """
        Constructs the MainMenuFrame for the specified window.

        :param window: The window to set as the master for this frame.
        :param openCollectionFunction: The function to invoke when the user selects "OPEN COLLECTION".
        :param instructionsFunction: The function to invoke when the user selects "INSTRUCTIONS".
        :param creditsFunction: The function to invoke when the user selects "CREDITS".
        :param quitFunction: The function to invoke when the user selects "QUIT".
        """

        self.window = window
        self.mainMenuFrame = None

        self.openCollectionFunction = openCollectionFunction
        self.instructionsFunction = instructionsFunction
        self.creditsFunction = creditsFunction
        self.quitFunction = quitFunction

        # End of init()

    def draw(self) -> None:
        """
        Draws the MainMenuFrame widgets to the window.

        :return: None
        """

        # Construct the frame
        self.mainMenuFrame = tkinter.Frame(self.window, pady=150)

        # Construct the introductory label
        titleLabel = tkinter.Label(self.mainMenuFrame, text="Library Collection Manager", font="TkFixedFont")

        titleLabel.grid(row=0, column=0, pady=50)

        # Construct the frame of buttons to transition to the GUI's different screens (or quit)
        mainMenuButtonFrame = tkinter.Frame(self.mainMenuFrame)
        mainMenuButtonFrame.grid(row=1, column=0)

        openLibraryCollectionButton = \
            tkinter.Button(mainMenuButtonFrame, text="OPEN COLLECTION", command=self.openCollectionFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        instructionsButton = \
            tkinter.Button(mainMenuButtonFrame, text="INSTRUCTIONS", command=self.instructionsFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        creditsButton = \
            tkinter.Button(mainMenuButtonFrame, text="CREDITS", command=self.creditsFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)
        quitButton = \
            tkinter.Button(mainMenuButtonFrame, text="QUIT", command=self.quitFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        openLibraryCollectionButton.grid(row=0, column=0, pady=10)
        instructionsButton.grid(row=1, column=0, pady=10)
        creditsButton.grid(row=2, column=0, pady=10)
        quitButton.grid(row=3, column=0, pady=10)

        # Draw the frame to the window
        self.mainMenuFrame.pack(padx=5, pady=5)

        # End of build()

    def destroy(self) -> None:
        """
        Destroys the widgets held by this frame. This effectively un-draws the frame from the GUI.

        :return: None
        """

        self.mainMenuFrame.destroy()
        self.mainMenuFrame = None

        # End of destroy()

    # End of MainMenuFrame
