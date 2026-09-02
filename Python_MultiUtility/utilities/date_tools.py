import datetime as dt
import time

def display_current_datetime():
    now = dt.datetime.now()
    print("\nCurrent Date and Time:", now)
    print("=" * 30)

def calculate_difference():
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")

    try:
        date1 = dt.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = dt.datetime.strptime(date2_str, "%Y-%m-%d")
        difference = abs(date2 - date1)
        print(f"\nDifference: {difference.days} days")
    except ValueError:
        print("\nInvalid date format. Please use YYYY-MM-DD.")
    print("=" * 30)

def format_date():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    custom_format = input("Enter the desired format (e.g., %d/%m/%Y): ")

    try:
        date = dt.datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date.strftime(custom_format)
        print(f"\nFormatted Date: {formatted_date}")
    except ValueError:
        print("\nInvalid date format. Please use YYYY-MM-DD.")
    print("=" * 30)

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = dt.datetime.now()
    input("Press Enter to stop the stopwatch...")
    end_time = dt.datetime.now()
    elapsed_time = end_time - start_time
    print(f"\nElapsed Time: {elapsed_time}")
    print("=" * 30)

def countdown_timer():
    seconds = int(input("Enter countdown time in seconds: "))
    print("\nCountdown started...")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    print("=" * 30)



def datetime_menu():
    
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display Current Date and Time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        try:
            choice_datetime = input("Enter your choice: ")

            match choice_datetime:
                case "1":
                    display_current_datetime()
                case "2":
                    calculate_difference()
                case "3":
                    format_date()
                case "4":
                    stopwatch()
                case "5":
                    countdown_timer()
                case "6":
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
       