# პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა.
# დაბეჭდოს შეყვანილი სტრიქონის ყველა ლუწი ინდექსის მქონე სიმბოლო,
# გარდა "e"- სიმბოლოს

# user_input = input("Enter a string: ")
#
# for index, char in enumerate(user_input):
#     if index % 2 == 0 and char != "e":
#         print(char)

# input_string = input("Input you string: ")
# new_string = ""
#
# for char in input_string:
#     if char.lower() != "e" and char.lower() != "o":
#         new_string += char
#
# print(new_string)

# import random
#
# random_number = random.randrange(1, 500)
# random_number2 = random.randrange(1, 500)
#
# result = random_number + random_number2
#
# print("Random number: ", random_number)
# print("Random number 2: ", random_number2)
# print(sum, result)

# import random
#
# random_number1 = random.randint(1, 1000)
# random_number2 = random.randint(10, 600)
#
# print("Random number 1: ", random_number1)
# print("Random number 2: ", random_number2)
#
# if random_number1 > random_number2:
#     print("Random number 1 is more than random number 2 ")
# elif random_number1 < random_number2:
#     print("Random number 2 is more than random number 1 ")
# else:
#     print("Random numbers are equal ")

# import random
# number1 = int(input("Enter number 1: "))
# number2 = random.randint(1, 1000)
#
# print("Number 1 is: ", number1)
# print("Number 2 is: ", number2)
#
# if number1 % 2 == 0 and number2 % 2 == 0:
#     print("Given numbers are even ")
# elif number1 % 2 == 1 and number2 % 2 == 1:
#     print("Numbers are odd ")
# else:
#     print("At least one of the given numbers is even ")
#

# import random
#
# random_number = random.uniform(1, 100)
# rounded_integer = round(random_number)
#
# print("Random number: ", random_number)
#
# if rounded_integer % 2 == 0:
#     print("Random number is even ")
# else:
#     print("Random number is odd ")

# for i in range(2,8,3):
#     print("The value of I currently is ", i)
#     pass

# fact = 1
# num = 10
#
# for i in range(1, num+1):
#     fact = fact * i
# print(fact)

# name = input("Enter a name: ")
#
# for _ in range(10):
#     print(name)

# name = input("Enter a name: ")
# num = int(input("Enter a number: "))
#
# for _ in range(num):
#     print(name)

# import random
#
# num1 = int(input("Enter number 1: "))
# num2 = random.randint(1,17)
#
# for _ in range(num2):
#     print(num1)
#
# name = input("Enter a name: ")
#
# for line_number in range(1,11):
#     print(f"{line_number} : {name}")

# summ = 0
#
# for i in range(0,10):
#     summ = summ + i
# print(summ)
#
# summ = 0
#
# for i in range(5,12):
#     summ = summ + i
# print(summ)

# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
#
# summ = 0
#
# for number in range(num1,num2 + 1):
#     summ = summ + number
# print(summ)

# დაწერეთ პროგრამა, რომელიც დათვლის რიცხვების ჯამს შემთხვევითი რიცხვიდან (0-10), შემთხვევით რიცხვამდე (10-20)

# import random
#
# num1 = random.randrange(0,10)
# num2 = random.randrange(10,20)
#
# summ = 0
#
# for number in range(num1,num2 + 1):
#     summ += number
# print(summ)


# odd_numbers = 0
# even_numbers = 0
#
# number = int(input("Enter a number or type 0 to stop: "))
#
# while number != 0:
#     if number % 2 == 1:
#         odd_numbers += 1
#     else:
#         even_numbers += 1
#     number = int(input("Enter a number or type 0 to stop "))
#
# print("Odd number count ", odd_numbers)
# print("Even numbers count ", even_numbers)

# pass_count = 0
# while True:
#     password = input("Enter a password: ")
#     pass_count += 1
#     if password == "User":
#         print("Welcome ")
#         break
#     if pass_count == 3:
#         print("Your account is blocked ")
#         break

#
# num = int(input("Enter a number: "))
# name = input("Enter a name: ")
#
# while num > 0:
#     print(name)
#     num -= 1

# პროგრამამ გამოიმუშავოს 2 რიცხვი 0-დან 10-მდე.
# პირველი რიცხვი დაიბეჭდოს იმდენჯერ, რასაც პროგრამა გამოიმუშავებს მეორე რიცხვში(while)
#

# import random
#
# num1 = random.randrange(0,10)
# num2 = random.randrange(0,10)
#
# print("Num1 is ", num1)
# print("Num2 is ", num2)
#
# while num2 > 0:
#     print(num1)
#     num2 -= 1


# დაბეჭდეთ "ჰელლო" 5-ჯერ, სტრიქონები დაინომროს(while

# name = "Hello"
# x = 1
#
# while x <= 5:
#     print(f" {x} ", name)
#     x += 1

# პროგრამამ გამოიმუშავოს რიცხვი და შეგვაყვანინოს სიტყვა,
# პროგრამამ დაბეჭდოს ეს სიტყვა ინდენჯერ, რა რიცხვსაც გამოიმუშავებს(while)
#
# import random
#
# num = random.randrange(0,10)
# word = input("Enter a word: ")
#
# print("Number is ", num)
# print("Word is", word)
#
# while num > 0:
#     print(word)
#     num -= 1
# პროგრამამ დათვალოს 0-დან 10-მდე რიცხვების ჯამი(while)

# num1 = 0
# summ = 0
#
# while num1 <= 11:
#     summ += num1
#     num1 += 1
# print(summ)
# პროგრამამ დათვალოს 1-დან 20-მდე რიცხვების ნამრავლი(while)

# num = 1
# multiplication = 1
#
# while num <= 20:
#     multiplication *= num
#     num += 1
# print(multiplication)

# user_input = input("Enter a word: ")
# vowel = ['A', 'E', 'O', 'U', 'I', 'a', 'e', 'o', 'u', 'i']
#
# consonants = ""
#
# for char in user_input:
#     if char.isalpha() and char not in vowel:
#         consonants += char
#
# print(consonants)

# user_input = input("Enter a word: ")
# index = 0
# while index < len(user_input) - 1:
#     index += 1
#
# print(user_input[0])
# print(user_input[index])

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = []
# for i in fruits:
#     if 'a' in i:
#         new_list.append(i)
# print(new_list)

# numbers = input("Enter numbers: ")
# numbers = numbers.split(',')
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# summ = 0
#
# for numbers in numbers:
#     summ += numbers
# print(summ)

# x = int(input("Enter a number: "))
# binary = ""
#
# while x > 0:
#     mod = x % 2
#     binary += str(mod)
#     x = x // 2
#
# binary = reversed(binary)
# print(str(binary))

# def mult(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b-1)
#
# # print(mult(2,5))
# def mult(a, b):
#     if b == 1:
#         return a
#
#     else:
#         return a + mult(a, b - 1)
#
#
# print(mult(2,5))

