# Task 1
# integer to Roman
client_number = int(input("Enter a number to convert to Roman number: "))

numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
i = 0
roman_number = ""

while client_number > 0:

    for _ in range(client_number // numbers[i]):
        roman_number += roman[i]
        client_number -= numbers[i]
    i += 1
print(roman_number)

# Roman to integer
roman_numeral = input("Enter a Roman numeral to convert into integer: ")

is_valid = True
valid_characters = 'MDCLXVI'

for char in roman_numeral.upper():
    if char not in valid_characters:
        is_valid = False
        break
    if not is_valid:
        print("Invalid Roman numeral, please enter valid one ")
    else:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        previous_value = 0

        for i in reversed(roman_numeral.upper()):
            value = roman_numerals[i]
            if value < previous_value:
                number -= value
            else:
                number += value
            previous_value = value
print(f"The Roman numeral {roman_numeral} converted to the number is {number}.")

# Task 2
nikos_input = input("Enter the apples sizes for Niko, separated by spaces: ")
nikos_sizes_str = nikos_input.split()
nikos_sizes = []

for n in nikos_sizes_str:
    nikos_sizes.append(int(n))

sopos_input = input("Enter the apples sizes for Sopo, separated by spaces: ")
sopos_sizes_str = sopos_input.split()
sopos_sizes = []

for s in sopos_sizes_str:
    sopos_sizes.append(int(s))

sum_niko = sum(nikos_sizes)
sum_sopo = sum(sopos_sizes)

if sum_niko > sum_sopo:
    difference = sum_niko - sum_sopo
    exchange_from = nikos_sizes
    exchange_to = sopos_sizes
    giver = 'Niko'
    receiver = 'Sopo'
else:
    difference = sum_sopo - sum_niko
    exchange_from = sopos_sizes
    exchange_to = nikos_sizes
    giver = 'Sopo'
    receiver = 'Niko'

for size_from in exchange_from:
    for size_to in exchange_to:
        if size_from - size_to == difference // 2:
            print(f"{giver} needs to give {size_from} apples and {receiver} needs to give {size_to} apples.")
            print([size_from, size_to])
            break
        else:
            continue
            