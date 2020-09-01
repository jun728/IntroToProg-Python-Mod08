# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <JLi>,<8.31.2020>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strProduct = ""  # Captures the user task data
strPrice = ""  # Captures the user priority data
strStatus = ""


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)

    @property
    def product_name(self):
        return str(self.product_name)

    @product_name.setter
    def product_name(self, value):
        if value.isnumeric(value, str):
            self._product_name = value
        else:
            raise Exception("Error: Product Name Cannot be a number")

    @property
    def product_price(self):
        return float(self.product_price)

    @product_price.setter
    def product_price(self, value):
        if value.isnumeric(value, float):
            self._product_price = float(value)
        else:
            raise Exception("Error: Product Price must be a number.")


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            name, price = line.split(",")
            row = {"Product": name.strip(), "Price": price.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        file = open(file_name, "w")
        for product in list_of_product_objects:
            file.write(product.__str__() + "\n")
        file.close()
        return list_of_product_objects, 'Success'


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #


class IO:


    # TODO: Add docstring

    # print(IO.__doc__)
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add a New Product
            2) Save Data
            3) Exit      
            ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The Current Products are: *******")
        for row in list_of_rows:
            print(str(row))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

            :return: string
            """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

            :param optional_message:  An optional message you want to display
            :return: nothing
            """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    # TODO: Add code to get product data from user

    @staticmethod
    def add_data_to_list(name, price, lstOfProductObjects):
        row = {"Product": name, "Price": price}
        lstOfProductObjects.append(row)
        print("New Product Added.")
        return lstOfProductObjects, 'Success'

    @staticmethod
    def input_new_product_and_price():
        try:
            name = str(input("Enter the Name of Your Product:"))
            price = float(input("Enter Product Price:"))
        except Exception as e:
            print(e)
        return name, price




    # Presentation (Input/Output)  -------------------------------------------- #

    # Main Body of Script  ---------------------------------------------------- #
    # TODO: Add Data Code to the Main body


# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data

while True:
    # Show user current data in the list of product objects
    IO.print_current_products_in_list(lstOfProductObjects)

    # Show user a menu of options
    IO.print_menu_Tasks()  # Shows menu

    # Get user's menu option choice
    strChoice = IO.input_menu_choice()  # Get menu option

    # Let user add data to the list of product objects
    if strChoice.strip() == '1':  # Add a new Task
        addData = IO.input_new_product_and_price()
        IO.add_data_to_list(addData[0], addData[1], lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu


    # let user save current data to file and exit program
    elif strChoice == '2':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save Data to File (y/n) ? ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("Data Saved to File!")
            continue
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '3':
        print('Goodbye!')
        break
# let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
