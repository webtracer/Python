# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/18/2023
# Description: File for the operation of a Lemonade Stand that contains

class InvalidSalesItemError(Exception):
    """
        Class for raising a custom exception for invalid sales item entry attempts
    """
    pass


class MenuItem:
    """
        Class to create menu items for the Lemonade Stand
    """
    def __init__(self, name, wholesale_cost, selling_price):
        """
            Default Constructor for the MenuItem Class
        :param name:
        :param wholesale_cost:
        :param selling_price:
        """
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """
            Getter for the MenuItem Name
        :return: MenuItem Name
        """
        return self._name

    def get_wholesale_cost(self):
        """
            Getter for the MenuItem wholesale cost
        :return: MenuItem Wholesale cost
        """
        return self._wholesale_cost

    def get_selling_price(self):
        """
            Getter for the MenuItem selling price
        :return: MenuItem selling price
        """
        return self._selling_price


class SalesForDay:
    """
        Class for recording Lemonade Stand Daily Sales
    """

    def __init__(self, days_open, sales_for_day):
        """
            Default Constructor for the SalesForDay class
        :param days_open: Records the daily sakes for the stand
        :param sales_for_day: dictionary that contains the MenuItem and Qty sold for each day
        """
        self._days_open = days_open
        self._sales_for_day = sales_for_day

    def get_day(self):
        """
            Getter for the sales day
        :return: requested sales day number
        """
        return self._days_open

    def get_sales_dict(self):
        """
            Getter for the daily sales dictionary
        :return: dictionary of daily sales
        """
        return self._sales_for_day


class LemonadeStand:
    """
        Class for recording the activities of the Lemonade Stand
    """

    def __init__(self, name):
        """
            Default Constructor for the LemonadeStand class
        :param name: Takes the specified name
         Other Parameters below are initialized at program startup to their blank defaults
        """
        self._name = name
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        """
            Getter for the LemonadeStand name
        :return: LemonadeStand name
        """
        return self._name

    def add_menu_item(self, menu_object):
        """
            This function adds an item to the Lemonade Stand menu
        :param menu_object: a MenuItem object
        :return: nothing
        """
        self._menu[menu_object.get_name()] = menu_object

    def enter_sales_for_today(self, sales_for_the_day):
        """
            Function for recording the daily sales of the lemonade stand
        :param sales_for_the_day: a dictionary of Items and quantities sold for the day
        :return: nothing
        """
        try:
            for item_sold in sales_for_the_day:
                try:
                    if item_sold in self._menu:
                        self._sales_record.append(SalesForDay(self._current_day, sales_for_the_day))
                    else:
                        raise InvalidSalesItemError
                except InvalidSalesItemError:
                    print(f"Error - you sold an item not in Inventory - {item_sold}")
        finally:
            print("Done entering sales")
            self._current_day += 1

    def sales_of_menu_item_for_day(self, day, menu_item):
        """
            Function that calculates if an item was sold on a particular day
        :param day: the day of sales to be checked
        :param menu_item: the item to check for sales
        :return: the number of items sold of that type for that day
        """
        items_sold = self._sales_record
        for items in items_sold:
            if day == SalesForDay.get_day(items):
                items_for_day = SalesForDay.get_sales_dict(items)
                for item_sold in items_for_day:
                    if item_sold == menu_item:
                        return items_for_day[item_sold]

    def total_sales_for_menu_item(self, menu_item):
        """
            Function to calculate the total overall number sold for a particular item
        :param menu_item: Name of the item to get the total sold for
        :return: number of items sold
        """
        number_sold = 0
        day = 0

        while day <= self._current_day -1:
            if self.sales_of_menu_item_for_day(day, menu_item):
                number_sold += self.sales_of_menu_item_for_day(day, menu_item)
            day += 1

        return number_sold

    def total_profit_for_menu_item(self,menu_item):
        """
            Function to calculate the total profit of a particular menu item
        :param menu_item: Name of the item to the profit for
        :return: total profit ((selling price - wholesale cost) * qty sold) of the item
        """
        profit = 0.0
        profit_counter = 0

        while profit_counter <= self._current_day-1:
            total_sold = self.total_sales_for_menu_item(menu_item)
            profit += total_sold * (MenuItem.get_selling_price(self._menu[menu_item]) - MenuItem.get_wholesale_cost(self._menu[menu_item]))
            profit_counter += 1

        return profit

    def total_profit_for_stand(self):
        """
            Function to calculate the total profit that the stand has made
        :return: total profit ((selling price - wholesale cost) * qty sold) of each item sold overall
        """

        total_profit = 0.0
        counter = 0
        items_sold = 0

        while counter <= self._current_day -1:
            for items in self._menu:
                item = self._menu[items]
                items_sold += self.total_sales_for_menu_item(items)
                if MenuItem.get_selling_price(item):
                    total_profit = items_sold * (MenuItem.get_selling_price(self._menu[items]) - MenuItem.get_wholesale_cost(self._menu[items]))
            counter += 1

        return total_profit


def main():
    """
        Function that runs the program
    :return:
    """
    # stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
    # item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    # stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    # item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    # stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    # item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    # stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'
    #
    # # # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
    # day_0_sales = {
    #     'lemonade' : 5,
    #     'cookie'   : 2,
    #     'nori' : 2
    # }
    # #
    # stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    # day_1_sales = {
    #     'lemonade' : 10,
    #     'cookie'   : 5,
    #     'sweet tea' : 2
    # }
    # stand.enter_sales_for_today(day_1_sales)
    # print(f"lemonade profit = ${stand.total_profit_for_menu_item('lemonade'): .2f}")  # print the total profit for lemonade so far
    # print(f"Sales for the day 0 = {stand.sales_of_menu_item_for_day(0,'lemonade')}")
    # print(f"Sales for the day 1 = {stand.sales_of_menu_item_for_day(1, 'cookie')}")
    # print(f"Total quantity sold of lemonade = {stand.total_sales_for_menu_item('lemonade')}")
    # print(f"The total profit for Lemonade Stand {stand.get_name()} is ${stand.total_profit_for_stand(): .2f}")


if __name__ == "__main__":
    main()
