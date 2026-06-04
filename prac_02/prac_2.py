
min_length = 8

password = input("Enter a password: ")

while len(password) < min_length:
    print("Password is too short.")
    password = input("Enter a password: ")

print("*" * len(password))