# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 02/07/2023
# Description: A program to keep track of Neighborhood Pets, their species and owner
#          Program has the ability to add and delete pets, as well as save and load from JSON file

# Import the json utility
import json


class DuplicateNameError(Exception):
    """
        Exception Class for Duplicate Pet Name entry attempt
    """
    pass


class NeighborhoodPets:
    """
    Class for storing Pets in the neighborhood, their names, type and owner
    """

    def __init__(self):
        """
        Base Constructor for Neighborhood Pets class
        """
        self._pet_name = ""
        self._pet_species = ""
        self._pet_owner = ""
        self._pets = {}
        self._new_pets = {}

    def add_pet(self, pets_name, pets_species, pets_owner):
        """
            Function to add a pet by name including its species and owner
        :param pets_name: name of the pet
        :param pets_species: breed / type of pet
        :param pets_owner: name of the pets' owner
        :return: Nothing
        """
        self._pet_name = pets_name
        self._pet_species = pets_species
        self._pet_owner = pets_owner

        try:
            for name in self._pets.keys():
                if name == self._pet_name:  # If the name sent is the same as an already entered name ...
                    raise DuplicateNameError
            else:  # Add the info to the dictionary
                self._pets[self._pet_name] = self._pet_species, self._pet_owner
        except DuplicateNameError:
            print('You tried to enter a pet with the same name as another pet.')

    def delete_pet(self, pets_name):
        """
            Function to delete a pet from the dictionary
        :param pets_name: name of the pet to delete
        :return: Nothing
        """
        try:
            self._pets.pop(pets_name)  # Remove the pets name, unless it doesn't exist in the dictionary
        except KeyError as error:
            print(f"Cannot delete pet {pets_name}, no such pet exists")

    def get_owner(self, pets_name):
        """
            Function to get the name of the pets' owner
        :param pets_name:  name of the pet whose owner we are looking for
        :return: Name of the pets owner
        """
        return self._pet_owner

    def save_as_json(self, file_name):
        """
            Function to save the dictionary of pet info to a json file on the disk
        :param file_name: Name of the json file to save to disk
        :return: Nothing
        """

        with open(file_name, 'w') as outfile:
            json.dump(self._pets, outfile)

    def read_json(self, file_name):
        """
            Function to read a json file and create the objects associated with each record in the file
        :param file_name:  Name of the json file to load from disk
        :return: Nothing
        """
        # Clear the currently loaded pets
        self._pets.clear()

        # open the json file
        with open(file_name, 'r') as infile:
            new_pets = json.load(infile)

        # read the loaded json file and create new pets from it
        for item in new_pets.keys():
            self.add_pet(item, new_pets[item][0], new_pets[item][1])

    def get_all_species(self):
        """
            Function to get all the species of the currently loaded pets
        :return: Set of Species
        """
        species_list = []

        for item in self._pets:
            species_list.append(self._pets[item][0])

        return set(species_list)


# np = NeighborhoodPets()
# try:
#     np.add_pet("Fluffy", "gila monster", "Oksana")
#     np.add_pet("Tiny", "stegasaurus", "Rachel")
#     np.add_pet("Spot", "zebra", "Farrokh")
# except DuplicateNameError:
#     print('You tried to enter a pet with the same name as another pet.')
# np.save_as_json("pets.json")
# np.delete_pet("Tiny")
# spot_owner = np.get_owner("Spot")
# print(spot_owner)
# np2 = NeighborhoodPets()
# np2.add_pet("Trooper", "German Shepherd", "Laura")
# np2.add_pet("Giselle", "German Shepherd / Husky", "George")
# np2.add_pet("Guinness", "Beagle", "Randy")
# np2.save_as_json("other_pets.json")
# np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
# spot_owner = np.get_owner("Guinness")
# print(spot_owner)
# species_set = np.get_all_species()
# print(species_set)
# print(type(species_set))
