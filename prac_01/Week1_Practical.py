""" TEST """
print("\033[4mTesting\033[0m...")
print("Hello World")
print(" ")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" PRELIMINARY """
"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
print("\033[4mPreliminary Activity: Temperature Converter\033[0m")
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
print(" ")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: Celsius = 5 / 9 * (Fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
print(" ")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ACTIVITY 1 """
"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""
print("\033[4mActivity 1: Sales Bonus\033[0m")
MENU1 = """WELCOME TO THE SALES BONUS CALCULATOR!"""
print(MENU1)
choice1 = input("Would you like to calculate bonus? (y/n) ").upper()
while choice1 != "N":
    if choice1 == "Y":
        print("Please enter sales amount:")
        sales = float(input(">>> $"))
        if sales < 1000:
            bonus = sales*0.1
            print(f"Bonus amount: $ {bonus:.2f}")
            print(" ")
        elif sales >= 1000:
            bonus = sales*0.15
            print(f"Bonus amount: $ {bonus:.2f}")
            print(" ")
        else:
            print("Invalid option")
        print(MENU1)
        choice1 = input("Would you like to calculate bonus? (y/n) ").upper()
    else:
        print("Invalid option")
print("Thank you.")
print(" ")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ACTIVITY 2 """
print("\033[4mActivity 2: Debugging\033[0m")
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
"""
*** OLD CODE ***
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""
if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
elif score < 50 and score >= 0:
    print("Bad")
elif score >= 50 and score < 90:
    print("Passable")
elif score >= 90 and score <= 100:
    print ("Excellent")

print(" ")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ACTIVITY 3 """
print("\033[4mActivity 3: Loops\033[0m")

print("Preliminary: Display all the odd numbers between 1 and 20 with a space between each one.")
for i in range(1, 21, 2):
    print(i, end=' ')
print()
print(" ")

print("a) Count in 10s between 1 and 100 with a space between each one.")
for i in range(0, 110, 10):
    print(i, end=' ')
print()
print(" ")

print("b) Count down from 20 to 1 with a space between each one.")
for i in range(20, 0, -1):
    print(i, end=' ')
print()
print(" ")

print("c) Ask user for a number then print that many stars.")
stars_num = int(input("How many stars?: "))
for i in range(0, stars_num, 1):
    print("*", end="")
print()
print(" ")

print("d) Ask user for a number then print lines of increasing stars to that number.")
stars_num = int(input("How many stars?: "))
for i in range(0, stars_num+1, 1):
    for j in range(0, i, 1):
        print("*", end="")
    print("")
print()
print(" ")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ACTIVITY 4 """
print("\033[4mActivity 4: Shop Calculator\033[0m")
print(" ")

#Input
Total_Cost = 0
Item_Count = -1
while Item_Count <0:
    Item_Count = int(input("How many items do you have?: "))
    if Item_Count < 0:
        print("Invalid number of items!")


for i in range(1, Item_Count+1, 1):
    print("Item ",i," cost?: ", end="")
    Item = int(input("$"))
    Total_Cost = Item+Total_Cost

print(" ")

#Calculator
if Total_Cost >= 100:
    print("Congrats, you earned a 10% discount!")
    print("Total cost without your 10% discount: $", Total_Cost)
    Total_Cost = Total_Cost * 0.9
    print("Total cost with a 10% discount: $", Total_Cost)
else:
    print("Total Cost: $", Total_Cost)

print(" ")
print("Thank you for using Shop Calculator!~ ")
print(" ")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ACTIVITY 5 """
print("\033[4mActivity 5: Menus\033[0m")
print(" ")

name = input("What is your name? ")

print(" ")
print("Please select and option below:")
MENU2 = """(H) Hello
(G) Goodbye
(Q) Quit"""
print(MENU2)

Option = input(">>>").upper()
while Option != "Q":
    if Option == "H":
        print("Hello", name)
    elif Option == "G":
        print("Goodbye", name)
    else:
        print("Invalid option! (type H,G or Q)")
    print(" ")
    print(MENU2)
    Option = input(">>>").upper()
print("Nice meeting you ", name, "!")
print(" ")