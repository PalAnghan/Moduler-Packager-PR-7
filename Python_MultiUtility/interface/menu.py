from utilities.date_tools import *
from utilities.calculation_tools import *
from utilities.random_tools import *
from utilities.identifier_tools import generate_uuid
from utilities.storage_tools import *
from utilities.explore_tools import explore_module
from utilities.storage_tools import File_operation

def main_menu():

    while True:

        print("=" * 15)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 15)

        print("Choose an option:")
        print("1. Datetime and time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation ")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operation (Custom Module)")
        print("6. Explore Module Attribute (dir())")
        print("7. Exit")
        print("=" * 15)

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    datetime_menu()
                case 2:
                    math_menu()
                case 3:
                    random_menu()
                case 4:
                    print("\nGenerated UUID:", generate_uuid())
                case 5:
                    file_menu()
                case 6:
                    module_name = input("Enter module name: ")
                    explore_module(module_name)
                case 7:
                    print("=" * 15)
                    print("Thank you for using the Multi-Utility Toolkit!")
                    print("=" * 15)
                    break
                case _:
                    print("Invalid choice. Please try again.")

        except ValueError :
            print("Invalid input. Please enter a number between 1 and 7.")

