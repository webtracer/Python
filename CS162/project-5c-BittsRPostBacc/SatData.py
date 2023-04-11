# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date:  02/05/2023
# Description: A program to load SAT Results from a JSON file and return the information for selected records
#                   to a csv file

import json


class SatData:
    """
    Class to import and work with SAT data from a json file
    """

    def __init__(self):
        """
        Constructor for the SatData class, imports JSON file and assigns it to a dictionary
        """
        # Private class member for storing the SAT data from the JSON file
        self._sat_dict = {}
        # Opens the JSON file for reading and assigns it to the sat_dict dictionary
        with open("sat.json", 'r') as infile:
            self._sat_dict = json.load(infile)

    def save_as_csv(self, list_of_dbns):
        """
        Function to take a list of dbns and output a csv file to disk of the relevant data
        :param list_of_dbns: a list of DBNs - District Bureau Numbers to lookup
        :return: Nothing, outputs a CSV file named output.csv
        """

        # Opens the output.csv file for writing
        with open("output.csv", 'w') as outfile:
            # Sets the Static Headers for the csv file
            header = 'DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean'
            outfile.write(header + '\n')   # writes the headers at the top of the file
            for item in self._sat_dict['data']:  # Loops through the dictionary of SAT data
                for record in list_of_dbns:  # pulls each record we are searching for
                    if item[8] == record:  # compares the DBN record to the one we are searching for
                        if ',' in item[9]:  # If the School name contains a , we need to put it in quotes then write
                            school_data = item[8] + ',"' + item[9] + '",' + item[10] + "," + item[11] + "," + item[12] + "," + item[13]
                            outfile.write(school_data + '\n')
                        else:  # School name does not contain a , so we can just write the string
                            school_data = item[8] + "," + item[9] + "," + item[10] + "," + item[11] + "," + item[12] + "," + item[13]
                            outfile.write(school_data + '\n')


# sd = SatData()
# dbns = ["02M303", "02M294", "01M450", "02M418", "15K462"]
# sd.save_as_csv(dbns)