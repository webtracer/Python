# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/25/2023
# Description: Program to Run a Library, handling items, Patrons, Check outs, returns, fines, payments and hold requests

class LibraryItem:
    """
        Class for storing Items that are found in the Library
    """
    def __init__(self, library_item_id, title):
        """
        Constructor for the Library Item Class
        :param library_item_id:
        :param title:
        """
        self._library_item_id = library_item_id
        self._title = title
        self._location = "On Shelf"
        self._checked_out_by = ""
        self._requested_by = ""
        self._date_checked_out = 0

    def get_location(self):
        """
        Getter for the library item location
        :return:
        """
        return self._location

    def get_library_item_id(self):
        """
        Getter for the library item_id
        :return:
        """
        return self._library_item_id

    def get_requested_by(self):
        """
        Getter for the patron that has the book on hold
        :return:
        """
        return self._requested_by

    def get_checkout_by(self):
        """
        Getter for the patron that has the item checked out
        :return:
        """
        return self._checked_out_by

    def get_date_checked_out(self):
        """
        Getter for the date the item was checked out
        :return:
        """
        return self._date_checked_out

    def set_item_checked_out(self, patron_id, date_checked_out):
        """
        Setter for marking an item as checked out
        :param patron_id:
        :param date_checked_out:
        :return:
        """
        self._location = "Checked Out"
        self._checked_out_by = patron_id
        self._date_checked_out = date_checked_out

    def set_location(self, location):
        """
        Setter for changing the location
        :param location: The new (changed) location
        :return:
        """
        self._location = location

    def set_requested_by(self, patron):
        """
        Setter for the patron wanting to put the item on hold
        :param patron:
        :return:
        """
        self._requested_by = patron

    def increment_check_out_time(self, days):
        """
        Setter for incrementing the number of days the item has been checked out
        :param days:
        :return:
        """
        self._date_checked_out += days

    def clear_requested_by(self):
        """
        Clears the item of being on hold
        :return:
        """
        self._requested_by = ""

    def clear_checked_out_by(self):
        """
        Clears an item from being checked out
        :return:
        """
        self._checked_out_by = ""


class Patron:
    """
    Class that hold the Patrons of a Library
    """
    def __init__(self, patron_id, name):
        """
        Constructor for the Patron Class
        :param patron_id:
        :param name:
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = {}
        self._fine_amount = 0.0

    def get_patron_id(self):
        """
        Getter for the Patron ID
        :param name:
        :return:
        """
        return self._patron_id

    def get_name(self):
        """
        Getter for the patrons name
        :return:
        """
        return self._name

    def get_patron_id_by_name(self):
        """
        Return the Patron ID from the name
        :return:
        """
        return self._patron_id

    def get_fine_amount(self):
        """
        Getter for a patrons fine amount if any
        :return:
        """

        return self._fine_amount

    def get_patron_checked_out_item(self):
        """
        Getter for items that a patron has checked out
        :return:
        """
        return self._checked_out_items

    def add_library_item(self, item_id):
        """
        Adds a library item to a Patrons checked out items
        :param item_id:
        :return:
        """
        self._checked_out_items[item_id] = self._patron_id
        return print(f"Check out successful")

    def remove_library_item(self, item_id):
        """
        Removes a library item from the Patrons acount
        :param item_id:
        :return:
        """

        self._checked_out_items.pop(item_id)
        return print(f"Return successful")

    def amend_fine(self, amount):
        """
        Updates a Patrons fine
        :param amount:
        :return:
        """
        current_fine = self.get_fine_amount()
        current_fine += amount
        self._fine_amount = current_fine


class Library:
    """
    Class for handling all of a libraries tasks
    """
    def __init__(self):
        """
        Constructor for the Library class
        """
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def add_library_item(self, library_item):
        """
        Adds an item to the library
        :param library_item:
        :return:
        """
        self._holdings[library_item.get_library_item_id()] = library_item

    def add_patron(self, patron):
        """
        Adds a patron to the library
        :param patron:
        :return:
        """
        self._members[patron] = patron.get_name()

    def lookup_library_item_from_id(self, library_item):
        """
        Gets the library items name from the item_id
        :param library_item:
        :return:
        """
        item_found = False
        for item in self._holdings:
            if library_item == item:
                item_found = True
                return self._holdings[item]

        if not item_found:
            return "None"

    def lookup_patron_from_id(self, patron_id):
        """
        Gets the Patron name from the id
        :param patron_id:
        :return:
        """

        patron_found = False

        for item in self._members:
            found_id = Patron.get_patron_id(item)
            if patron_id == found_id:
                return item

        if not patron_found:
            return "None"

    def check_out_library_item(self, patron_id, library_item_id):
        """
        Checks out a library item to a Patron
        :param patron_id:
        :param library_item_id:
        :return:
        """
        # Look up the Patron object from the Patron ID
        patron = self.lookup_patron_from_id(patron_id)
        if patron == "None":
            return print("Patron not found")

        # Look up the library item object
        item_id = self.lookup_library_item_from_id(library_item_id)
        if item_id == "None":
            return print("Library Item not found")

        # Check if the item has been checked out or reserved by a Patron
        if LibraryItem.get_location(item_id) == "Checked Out":
            return print("Item already Checked Out")
        # If item is not checked out, check if there is a hold
        elif LibraryItem.get_location(item_id) == "On Hold Shelf":
            # Check if the hold is for this patron
            if LibraryItem.get_requested_by(item_id) != patron_id:
                return print("Item is on hold by other patron")
            else:
                LibraryItem.clear_requested_by(item_id)
        else:
            LibraryItem.set_item_checked_out(item_id, patron, self._current_date)
            return print(Patron.add_library_item(patron, item_id))

    def return_library_item(self, library_item_id):
        """
        Returns a library item to the shelf and off the Patrons account
        :param library_item_id:
        :return:
        """
        # Look up the library item object
        item_id = self.lookup_library_item_from_id(library_item_id)
        if item_id == "":
            return print("Item not found")

        # Check if the item has been checked out or reserved by a Patron
        if LibraryItem.get_location(item_id) != "Checked Out":
            return print(f"Item already in Library")
        else:
            patron_id = LibraryItem.get_checkout_by(item_id)
            LibraryItem.clear_checked_out_by(item_id)
            if LibraryItem.get_requested_by(item_id):
                LibraryItem.set_location(item_id, "On Hold")
            else:
                LibraryItem.set_location(item_id, "On Shelf")
            # return_status = Patron.remove_library_item(patron_id, item_id)
            return Patron.remove_library_item(patron_id, item_id)  # print(return_status)

    def request_library_item(self, patron_id, library_item_id):
        """
        Puts a library item on hold if possible
        :param patron_id:
        :param library_item_id:
        :return:
        """
        # Check to see if patron exists
        if self.lookup_patron_from_id(patron_id) == "None":
            return print("Patron not found")
        # Check to see if Library Item exists
        elif self.lookup_library_item_from_id(library_item_id) == "None":
            return print("Item not found")
        # Check to see if item is already on hold
        elif LibraryItem.get_checkout_by(self.lookup_library_item_from_id(library_item_id)) != "":
            return print("Item already on hold")
        # Set the item to on hold, and move to Hold Shelf
        else:
            LibraryItem.set_requested_by(library_item_id, patron_id)
            LibraryItem.set_location(self.lookup_library_item_from_id(library_item_id), "On Hold Shelf")

    def pay_fine(self, patron_id, payment_amount):
        """
        Pays a Patrons fine
        :param patron_id:
        :param payment_amount:
        :return:
        """
        if self.lookup_patron_from_id(patron_id):
            Patron.amend_fine(self.lookup_patron_from_id(patron_id), (-payment_amount))
            return print("Payment Successful")
        else:
            return print("Patron not found")

    def increment_current_date(self):
        """
        Adds 1 to the current date, and increments any fines as needed
        :return:
        """
        self._current_date += 1
        for patron in self._members:
            for item in Patron.get_patron_checked_out_item(patron):
                if item != "None":
                    LibraryItem.increment_check_out_time(item, 1)
                    if isinstance(item, Book):
                        if self._current_date > Book.get_checkout_length(item):
                        # if Book.get_checkout_length(item) <= self._current_date:
                            Patron.amend_fine(patron, 0.10)
                    elif isinstance(item, Album):
                        if Album.get_checkout_length(item) <= self._current_date:
                            Patron.amend_fine(patron, 0.10)
                    elif isinstance(item, Movie):
                        if Movie.get_checkout_length(item) <= self._current_date:
                            Patron.amend_fine(patron, 0.10)


class Book(LibraryItem):
    """
    Class for storing Book items in the Library
    """
    def __init__(self, item_id, title, author):
        """
        Constructor for the Book, inherits from LibraryItem plus Author
        :param item_id:
        :param title:
        :param author:
        """
        super().__init__(item_id, title)
        self._author = author

    def get_author(self):
        """
        Getter for the Books Author
        :return:
        """
        return self._author

    def get_checkout_length(self):
        """
        Getter for the length a book can be checked out before being overdue
        :return:
        """
        return 21


class Album(LibraryItem):
    """
    Class for storing Albums in the Library
    """
    def __init__(self, item_id, title, artist):
        """
        Constructor for the Album, inherits from LibraryItem plus Artist
        :param item_id:
        :param title:
        :param artist:
        """
        super().__init__(item_id, title)
        self._artist = artist

    def get_artist(self):
        """
        Getter for the Albums artist
        :return:
        """
        return self._artist

    def get_checkout_length(self):
        """
        Getter for the length an album can be checked out before being overdue
        :return:
        """
        return 14


class Movie(LibraryItem):
    """
    Class for storing Movie items in the Library
    """
    def __init__(self, item_id, title, director):
        """
        Constructor for the Movie, inherits from LibraryItem plus Director
        :param item_id:
        :param title:
        :param director:
        """
        super().__init__(item_id, title)
        self._director = director

    def get_director(self):
        """
        Getter for the director of the movie
        :return:
        """
        return self._director

    def get_checkout_length(self):
        """
        Getter for the length a movie can be checked out before being overdue
        :return:
        """
        return 7


# One limited example of how your classes might be used is:
b1 = Book("345", "Phantom Tollbooth", "Juster")
b2 = Album("456", "...And His Orchestra", "The Fastbacks")
# m1 = Movie("567", "Laputa", "Miyazaki")
# print(b1.get_author())
# print(a1.get_artist())
# print(m1.get_director())
# #
p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")
p3 = Patron("xyz", "Laura")
# #
lib = Library()
lib.add_library_item(b1)
lib.add_library_item(b2)
# lib.add_library_item(m1)
lib.add_patron(p1)
lib.add_patron(p2)
lib.add_patron(p3)
# #
lib.check_out_library_item("bcd", "456")
# lib.check_out_library_item("xxx", "457")
# for _ in range(7):
#     lib.increment_current_date()  # 7 days pass
# lib.check_out_library_item("abc", "567")
lib.check_out_library_item("xyz", "345")
# loc = a1.get_location()
# lib.request_library_item("abc", "456")
for _ in range(57):
    lib.increment_current_date()  # 57 days pass
p2_fine = p2.get_fine_amount()
print(p2_fine)
lib.pay_fine("bcd", p2_fine)
p2_fine_2 = p2.get_fine_amount()
print(p2_fine_2)
lib.return_library_item("456")
