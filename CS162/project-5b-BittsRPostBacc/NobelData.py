# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 02/02/2023
# Description: A program to read the Nobel Prize winner data and return the Surname of the winners
#                   in a specific year and category

import json


class NobelData:
    """
        A class for reading the JSON file of Nobel Prize winners
    """
    def __init__(self):
        """
        Constructor for the NobelData class
        """
        # Dictionary to hold the json file data
        self._prize_data = {}
        # list of dictionaries to hold the winners data
        self._winners = []
        # Opens the json file
        with open("nobels.json", 'r') as infile:
            self._prize_data = json.load(infile)

    def search_nobel(self, search_year, search_category):
        """
        Searches the JSON loaded data for the year and category
        :param search_year: A text year that is sent by the user
        :param search_category: the category to search for
        :return: self._winners = a list of surnames
        """
        # clear the list
        self._winners = []
        # Assign the JSON data to a new dictionary
        winners_by_year = self._prize_data['prizes']

        # Search the dictionary for the requested data
        for year in winners_by_year:
            if year['year'] == search_year:
                if year['category'] == search_category:
                    # Check for a winner in that category, if not, return No records found message
                    if year.get('laureates'):
                        for item in year['laureates']:
                            self._winners.append(item['surname'])
                    elif year.get('overallMotivation'):
                        return f"No Winners found for {search_year} in {search_category}"

        # Sort the list, in case it's not already correctly sorted
        self._winners.sort()

        # Return the populated list
        return self._winners


# nd = NobelData()
# print(nd.search_nobel("2001", "economics"))
# print(nd.search_nobel("2022", "chemistry"))
# print(nd.search_nobel("1971", "chemistry"))
# print(nd.search_nobel("1901", "literature"))
# print(nd.search_nobel("1916", "physics"))
# print(nd.search_nobel("1941", "physics"))
# print(nd.search_nobel("1942", "medicine"))
# print(nd.search_nobel("1940", "chemistry"))



