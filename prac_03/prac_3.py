import time
import random

def main():
    choice = menu_display()
    menu_selection(choice)

def menu_display():
    print("")
    print("\033[4mPrac 3\033[0m")
    print("""
            1 - String Formatting 
            2 - Random Numbers 
            3 - Capitalist Conrad 
            4 - Exceptions to Complete 
            5 - Password Checker 
            6 - Files 
            7 - File Size  
            Q - Quit (ends run)
                """)
    choice = input(">>> ").upper()
    return choice

def menu_selection(choice):
    while True:
        if choice == "1":
            string_formatting_q()
            choice = menu_display()
        elif choice == "2":
            random_numbers_q()
            choice = menu_display()
        elif choice == "3":
            capitalist_conrad_q()
            choice = menu_display()
        elif choice == "4":
            capitalist_conrad_q()
            choice = menu_display()
        elif choice == "5":
            password_checker_q()
            choice = menu_display()
        elif choice == "6":
            files_q()
            choice = menu_display()
        elif choice == "7":
            files_size_q()
            choice = menu_display()
        elif choice == "Q":
            break
        else:
            print("Not a valid choice. Insert an available option")
            time.sleep(2)
            choice = menu_display()

# String Formatting
def string_formatting_q():

    end_of_loop = 10
    last_value = 2**end_of_loop
    digit_count = len(str(abs(end_of_loop+1)))
    digit_count2 = len(str(last_value))

    for i in range (end_of_loop+1):     # from 0 to 10
        answer = 2**i
        print(f"2 ^ {i:^{digit_count}} is {answer:>{digit_count2}}")

    time.sleep(5) # Gives user time to read output

# Random Numbers
def random_numbers_q():

    print(random.randint(5, 20))                    # line 1 (integer increment, low and high inclusive)
    print(random.randrange(3, 10, 2))      # line 2 (step increment, low and high inclusive)
    print(random.uniform(2.5, 5.5))                  # line 3 (random float between low and high)

    time.sleep(5) # Gives user time to read output

# Capitalist Conrad
def capitalist_conrad_q():
    print("\033[4mCapitalist Conrad\033[0m")
    starting_price = float(input("How much to start with investing? >>>").upper())
    digit_count_price = len(str(starting_price))
    days_tracked = int(input("And how long would you like to invest? >>>").upper())
    print("")
    print(f"Starting price is ${starting_price:<{digit_count_price}.2f}")
    price = float(starting_price)
    out_file = open("Trading_History.txt", 'w')

    for days in range(days_tracked+1):
        multiplier = float(capitalist_conrad_multiplier())
        price = price*(1+multiplier)
        digit_count_days = len(str(days))
        digit_count_price = len(str(price))
        digit_count_days_tracked = len(str(days_tracked))
        print(f"On day {days:^{digit_count_days_tracked}} price is ${price:<{digit_count_price}.2f}", file=out_file)

        if days == 1:
            print(f"On day {days:^{digit_count_days}} price is ${price:<{digit_count_price}.2f}")
            print("...")

        if days == days_tracked -1:
            print(f"On day {days:^{digit_count_days}} price is ${price:<{digit_count_price}.2f}")

        elif days == days_tracked:
            digit_count_days = len(str(days))
            digit_count_price = len(str(price))
            print(f"On day {days:^{digit_count_days}} price is ${price:<{digit_count_price}.2f}")

    out_file.close()

def capitalist_conrad_multiplier():

    profit  = random.uniform(0, 10)              # Scales between values for a profit (percent)
    loss    = random.uniform(0, -5)                 # Scales between values for a loss (percent)
    multiplier = random.choice([profit,loss])/100      # Into scale value from percent

    # NOTE: Zero cannot appear and neither can upper limits as result is non-inclusive
    return multiplier

# Exceptions
def exceptions_q():
    print("test")

# Password Checker
def password_checker_q():
    print("test")

# Files
def files_q():
    print("test")

# Files Size
def files_size_q():
    print("test")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
main()