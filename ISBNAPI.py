# API implemented from: https://openlibrary.org/dev/docs/api/books

import urllib, json
from urllib import request, error


class URLError(Exception):
    pass


class ConnectionError(Exception):
    pass


class InputError(Exception):
    pass


class BookAPI:
    # Each key has a try/except statement as not every book contains every piece of info requested
    # the except statements allow for assign of empty strings temporarily so that crashes don't occur during assignment
    def __init__(self, ISBN):
        self.ISBN = ISBN
        self.url = "https://openlibrary.org/isbn/" + ISBN + ".json"
        self.title = ""
        self.author = ""
        self.yearPub = ""
        self.pageCount = ""
        try:
            new_object = _download_url(self.url)

        except urllib.error.URLError:  # Catches if connection drops while processing
            raise ConnectionError("There was a problem with your internet connection while processing your request")

        except URLError:
            raise URLError("Book not found. The ISBN provided either does not exist or is not stored in our library")

        except:  # All other errors raised will be treated as input errors
            raise InputError("An unknown error occurred while processing your input")

        try:
            self.title = new_object['title']
        except:
            self.title = ""

        try:
            # the API returns a key for the author, this key needs to be sent to a new _download_url in order for the actual author to be returned
            authorKey = new_object['authors'][0]['key']
            url = "https://openlibrary.org" + str(
                authorKey) + ".json"  # creates the new link needed to download the author's name
            temp = _download_url(url)
            self.author = temp['name']
        except:
            self.author = ""

        try:
            # The format of publish date is often inconsistent. Sometimes it gives (MM/DD/YYYY), (Month D, YYYY), but the year published
            # has always been the last 4 digits, so this gets the last 4 digits from the date returned
            publishDate = new_object['publish_date']
            publishDate = publishDate[-4] + publishDate[-3] + publishDate[-2] + publishDate[-1]
            self.yearPub = publishDate
        except:
            self.yearPub = ""
        try:
            self.pageCount = new_object['number_of_pages']
        except:
            self.pageCount = ""


def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None
    error = 0
    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        error = e.code

    finally:
        if response != None:
            response.close()

    if error == 404:
        raise URLError()

    return r_obj


'''
used for testing purposes
def start():
    number = input("ISBN number: ")
    book = BookAPI(number)
    print(book.author)
'''

