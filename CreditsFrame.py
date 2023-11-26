# CreditsFrame.py
#
# GUI widget code and tkinter usage adapted from:
# https://realpython.com/python-gui-tkinter/
# https://tkdocs.com/tutorial
# https://docs.python.org/3/library/tkinter.html

import tkinter


_BUTTON_WIDTH = 15
_BUTTON_LENGTH = 2


class CreditsFrame:
    """
    Defines CreditsFrame objects.

    Contains the widgets needed to operate the Credits screen for the LibraryCollectionGUI.

    The frame can be drawn to the GUI using draw(), or removed from the GUI using destroy().

    """

    def __init__(self, window: tkinter.Tk, backFunction):
        """
        Constructs the CreditsFrame for the specified window.

        :param window: The window to set as the master for this frame.
        :param backFunction: The function to invoke when the user selects "BACK".
        """

        self.window = window
        self.creditsFrame = None

        self.backFunction = backFunction

        # End of init()

    def draw(self) -> None:
        """
        Draws the CreditsFrame widgets to the window.

        :return: None
        """

        # Construct the frame
        self.creditsFrame = tkinter.Frame(self.window, pady=0)

        # Construct the label to present the credits
        creditsLabel = tkinter.Label(self.creditsFrame,
                                     text="CREDITS:" +
                                          "\n\nInterface by:                    Nathanael Scudder" +
                                          "\n\nCollection management by:               Jeff Hover" +
                                          "\n\nDate of Completion:            December 17th, 2020",
                                     justify="left",
                                     bg="white",
                                     width=80,
                                     height=15,
                                     font="TkFixedFont")

        creditsLabel.grid(row=0, column=0, pady=80)

        # Construct the back button
        backButton = \
            tkinter.Button(self.creditsFrame, text="BACK", command=self.backFunction,
                           width=_BUTTON_WIDTH, height=_BUTTON_LENGTH)

        backButton.grid(row=1, column=0)

        # Draw the frame to the window
        self.creditsFrame.pack(padx=5, pady=5)

        # End of build()

    def destroy(self) -> None:
        """
        Destroys the widgets held by this frame. This effectively un-draws the frame from the GUI.

        :return: None
        """

        self.creditsFrame.destroy()
        self.creditsFrame = None

        # End of destroy()

    # End of CreditsFrame
