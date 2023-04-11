# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 11/12/2022
# Description: takes lists of employee attributes and returns a dictionary
#                of the employeeID and the corresponding Employee object

class Employee:

    def __init__(self, name, ID_number, salary, email_address):
        """
        Constructor for the Employee class
        :param name:
        :param ID_number:
        :param salary:
        :param email:
        """
        self._name = name
        self._ID_number= ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """
        Getter for the emp_name
        :return:
        """
        return self._name

    def get_ID_number(self):
        """
        Getter for the emp_id
        :return:
        """
        return self._ID_number

    def get_salary(self):
        """
        Getter for the emp_salary
        :return:
        """
        return self._salary

    def get_email_address(self):
        """
        Getter for the emp_email
        :return:
        """
        return self._email_address


def make_employee_dict(emp_name, emp_id, emp_salary, emp_email):
    """
    takes lists of employees and their attributes, creates Employee object, and stores the ID and
        the object in a dictionary
    :param emp_name: a list of employee names
    :param emp_id: a list of employee IDs
    :param emp_salary: a list of employee salaries
    :param emp_email: a list of employee email addresess
    :return: emp_dict - a dictionary of employee ID's and the corresponding Employee object
    """
    counter = 0
    emp_dict = {}

    while counter < len(emp_id):
        for emp in emp_id:
            emp = Employee(emp_name[counter], emp_id[counter], emp_salary[counter], emp_email[counter])
            emp_dict[emp_id[counter]] = emp
            counter = counter + 1

    return emp_dict
