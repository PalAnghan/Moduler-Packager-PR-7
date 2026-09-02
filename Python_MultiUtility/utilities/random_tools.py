import random

def generate_random_number():
    return random.randint(1, 100)

def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

def create_random_password(length):
    characters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*()"
    )

    return "".join(random.choice(characters) for _ in range(length))

def generate_random_otp():
    return random.randint(100000, 999999)





if __name__ == "__main__":
    print("Random Number:", generate_random_number())
    print("Random List:", generate_random_list(5))
    print("Random Password:", create_random_password(8))
    print("Random OTP:", generate_random_otp())


def random_menu():
    while True:
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Craete Random Password")
        print("4. Genarate Random Otp")
        print("5. Back to Main Menu")

        try:

            choice_random = int(input("Enter your choice: "))

            match choice_random:
                case 1:

                    print("Random Number:", generate_random_number())
                case 2:
                    size = int(input("Enter list size: "))
                    generate_random_list(size)
                case 3:
                    length = int(input("Enter password length: "))
                    create_random_password(length)
                case 4:
                    generate_random_otp()
                case 5:
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
        