# Task 1
import random

while True:
    tries = 0
    word_list = ["python", "programming", "computer", "algorithm", "variable", "function", "loop", "conditional", "dictionary", "list"]
    random_list_member = random.choice(word_list)
    shuffled_member = ''.join(random.sample(random_list_member, len(random_list_member)))
    print("This is the shuffled list member: " + shuffled_member)
    answer = str(input("Guess the correct word: "))
    if answer.lower() == random_list_member:
        print("You provided correct answer!")
        break
    else:
        print("You provided incorrect answer, please try again!\nHint, The first letter of the word is: " + random_list_member[0])
        answer = str(input("Guess the correct word: "))
        if answer.lower() == random_list_member:
            print("You provided correct answer!")
            break
        else:
            print("Still incorrect answer, closing session!")
            break

# Task 2

client_text = str(input("Enter the text you want to encrypt: "))
shift = int(input("Enter shifting number: "))

encrypted_message = ""
for char in client_text:
    if char.isalpha():
        shifted = ord(char) + shift
        if char.islower():
            if shifted > ord('z'):
                shifted -= 26
        elif char.isupper():
            if shifted > ord('Z'):
                shifted -= 26
        encrypted_message += chr(shifted)
    else:
        encrypted_message += char

print("Encrypted message is " + "'" + encrypted_message + "'")

answer = input("Do you want to decrypt the text?  Y/N: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    decrypted_message = ""

    for char in client_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
        decrypted_message += char
    print("Decrypted message is " + "'" + decrypted_message + "'")

elif answer.upper() == "N" or answer.upper() == "NO":
    print("You choose not to decrypt the text! ")
else:
    print("'" + answer + "' is incorrect input, please use Y/N or Yes/No instead next time!")