# Task 1

num1 = float(input("Enter first number: "))
action = input("Enter action: ")
num2 = float(input("Enter second number: "))

if action == "+":
    result = num1 + num2
    print(result)
elif action == "-":
    result = num1 - num2
    print(result)
elif action == "/":
    result = num1 / num2
    print(result)
elif action == "*":
    result = num1 * num2
    print(result)
elif action == "**":
    result = num1 ** num2
    print(result)
elif action == "%":
    result = num1 % num2
    print(result)
else:
    print("Incorrect action provided ")

# Task 2

color = input("Enter color: ")
if color.upper() == "RED":
    print("Stop!")
elif color.upper() == "YELLOW":
    print("Get Ready ")
elif color.upper() == "GREEN":
    print("Go! ")
else:
    print("Incorrect Color ")

# Task 3

num = int(input("Please enter the number: "))
noun = input("Please enter the noun: ")

if num > 1:
    noun = noun + "s"
print(num)
print(noun)
