# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/18/2023
# Description: Unittest cases for the LemonadeStand program

# Import the UnitTest class
import unittest

# Import the LemonadeStand file
import LemonadeStand


class LemonadeStandTester(unittest.TestCase):
    """
        Class for running the Unittest cases
    """

    def test_stand_object(self):
        """
            Function to test that the Lemonade Stand is created correctly
        :return: Pass/Fail
        """
        test_stand = LemonadeStand.LemonadeStand("Test Stand")
        self.assertEqual(LemonadeStand.LemonadeStand.get_name(test_stand), "Test Stand")

    def test_menu_item_object(self):
        """
            Function to test that Menu objects are created correctly by name
        :return: Pass/Fail
        """
        test_menu_item = LemonadeStand.MenuItem('Sweet Tea', 1.5, 3)
        self.assertEqual(LemonadeStand.MenuItem.get_name(test_menu_item), "Sweet Tea")

    def test_second_menu_object(self):
        """
            Function to test if Menu objects are created correctly by wholesale cost
        :return: Pass/Fail
        """

        test_menu_item_2 = LemonadeStand.MenuItem('Kolache', 2.25, 4.5)
        self.assertAlmostEqual(LemonadeStand.MenuItem.get_wholesale_cost(test_menu_item_2), 2.25)

    def test_third_menu_object(self):
        """
            Function to test if Menu objects are created correctly by selling price
        :return: Pass/Fail
        """

        test_menu_item_3 = LemonadeStand.MenuItem('Oreos', 1.25, 2.5)
        self.assertAlmostEqual(LemonadeStand.MenuItem.get_selling_price(test_menu_item_3), 2.5)

    def test_exception(self):
        """
            Function to test that the InvalidSalesItemError exception is raised
        :return:  Pass/Fail
        """
        self.assertRaises(LemonadeStand.InvalidSalesItemError)
