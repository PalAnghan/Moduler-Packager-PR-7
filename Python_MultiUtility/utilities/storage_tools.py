class File_operation:
    
    def add_file(self):
        filename = "files/" + input("Enter file name: ")
        try:
            with open(filename, "x") as file:
                print("\nFile created successfully!")
        except FileExistsError:
            print("Error: File already exists!")
        print("=======================")

    def write_file(self):
        filename = input("Enter file name: ")
        data = input("Enter data to write: ")

        with open("files/" + filename, "w") as file:
            file.write(data)
            
        print("\nData written successfully!")
        print("=======================")

    def read_file(self):
        filename = input("Enter file name: ")

        try:
            with open("files/" + filename, "r") as file:
                print("File Content:")
                print(file.read())
        except FileNotFoundError:
            print("Error: File not found.")
        print("=======================")

    def append_file(self):
        filename = input("Enter file name: ")
        data = input("Enter data to append: ")
        
        with open("files/" + filename, "a") as file:
            file.write("\n" + data)  
            
        print("\nData appended successfully!")
        print("=======================")


file1 = File_operation()


def file_menu():
        while True:

            print("File Operation:")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to Main Menu")

            try:
                choice_file_operation = int(input("Enter your choice: "))

                match choice_file_operation:
                    case 1:
                        file1.add_file()
                    case 2:
                        file1.write_file()
                    case 3:
                        file1.read_file()
                    case 4:
                        file1.append_file()
                    case 5:
                        break 
                    case _:
                        print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
