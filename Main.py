# Main.py

from LibraryCollectionGUI import LibraryCollectionGUI


def main() -> None:
    """
    Starts the Library Collection GUI.

    :return: None
    """

    interface = LibraryCollectionGUI()

    interface.start()

    # End of main()


if __name__ == '__main__':
    main()
