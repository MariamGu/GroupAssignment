import random
import string

# Task 1

num = random.randrange(1, 100)
print("Random number is: ", num)

num_count = 0
while True:
    client_number = int(input("Enter your number: "))
    num_count += 1
    if client_number > num:
        print("Too high, Try again ")
    elif client_number < num:
        print("Too low, Try again ")
    else:
        print("Win !")
        break
    if num_count == 5:
        print("Loss! ")
        break

# Task 2

password_complexity = str(input("Provide your password complexity level: "))
password_length = int(input("Provide your password length: "))

while password_length < 8:
    print("Password length should be equal or greater than 8! ")
    password_length = int(input("Provide your password length: "))

if password_complexity.upper() == "LOW":
    password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=password_length))
    print("Low complexity Password has been granted: " + password)
elif password_complexity.upper() == "MEDIUM":
    password = "".join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=password_length))
    print("Medium complexity Password has been granted: " + password)
elif password_complexity.upper() == "HIGH":
    password = "".join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
                       k=password_length))
    print("High complexity Password has been granted: " + password)
else:
    print("Incorrect complexity level have been provided! ")

# Task 3

while True:
    customer_input = str(input("Please enter a string: "))
    reversed_customer_input = customer_input[::-1]
    if customer_input == reversed_customer_input:
        print("Your string is Palindrome.")
    else:
        print("Your string is not Palindrome!")
    answer = input("Do you want to try with another string?  Y/N: ")
    if answer.upper() == "Y" or answer.upper() == "YES":
        continue
    elif answer.upper() == "N" or answer.upper() == "NO":
        print("You choose not to continue ")
        break
    else:
        print("'" + answer + "' is incorrect input, please use Y/N or Yes/No instead next time!")
        break
