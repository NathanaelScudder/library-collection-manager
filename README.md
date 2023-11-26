# library-collection-manager

<p>Posted for the purpose of showcasing previous coursework using Python. This project was completed in collaboration with Jeff Hover.</p>


## Functionality

<ul>
    <li>When clicking "OPEN COLLECTION" on the main menu, you will have the opportunity to designate a directory to use as the destination for any added books.

Newly added books will be entered into the designated directory as .book files (these .book files are not meant to be tampered with outside the program).

Any directory can be designated, regardless of its contents.

Alternatively, a new directory can be created using the opened file explorer window and used as the destination for any new books.

After designating a directory, any .book files that exist in the directory (but not inner-directories) will be loaded into the collection, which can then be viewed and or deleted.</li>
    <li>Once a collection has been opened (see "Opening a Collection"), you can click "VIEW COLLECTION" to view the list of books in the current collection.

If the collection does not contain any books yet, you will not be able to view the collection.

After selecting "VIEW COLLECTION", you can click "NEXT BOOK" to advance through the collection and viewthe different book's title, author, year published, page length, and date added to the collection. You can also click "PREVIOUS BOOK" to go backwards through the collection. However, the collection does not wrap.

Additionally from this menu, you can click "DELETE BOOK" to delete books.</li>
    <li>Once a collection has been opened, you can click "ADD BOOK" to enter a book's details in the form of its title, author, publishing year, and page length.

To enter these details for a book, simply fill in the corresponding entry fields with the proper information, and click "ADD BOOK"

Alternatively, some or all of the book's information can be automatically filled using its ISBN number.</li>
    <li>Once a collection has been viewed you can click "DELETE BOOK" todelete the currently viewed book from the collection.

Deleting the book will set the view screen to the previous book.

If the last book in a collection is deleted, you will be sent back to the previous screen.</li>
    <li>Once a collection has been viewed, you can click the five different radio buttons to change the collection's sorting methodology.

Changing the sorting methodology will also affect the book currently being viewed. E.g. if book 1 is being viewed, whatever book is first in the new sorting methodology will be the one to appear in the view screen.

By default, the collection is sorted according to each book's title (in alphabetical order).

Selecting "Author" will sort the collection according to each book's author name (in alphabetical order).

Selecting "Year Published" will sort the collection according to each book's year published name (in ascending order).

Selecting "Page Length" will sort the collection according to each book's page length (in ascending order).

Selecting "Date Added" will sort the collection according to each book's date added to the collection (in ascending order).</li>
</ul>

## Instructions

<p>Run Main.py to start the project:</p>

```bash
python Main.py
```