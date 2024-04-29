# Task 1
def find_longest_word():
    punctuation_chars = [',', '.', '!', '?', ';', ':']
    while True:
        input_string = input("Provide a string or enter 'exit' to exit the program: ")
        if input_string.lower() == 'exit':
            print("Exiting the program ")
            return
        else:
            for char in punctuation_chars:
                input_string = input_string.replace(char, '')

                words = input_string.split()
                max_length = len(max(words, key=len))
                longest_words = []

                for word in words:
                    if len(word) == max_length:
                        longest_words.append(word)

            print(f"The longest words are {longest_words} with the length of {max_length} characters ")


find_longest_word()


# Task 2
def simple_database():
    data_base = [1, 'nina', 5, 10, 2, 3, 4, 3, 4, 6, 6, 7, 8, 8, 9, 9]
    while True:
        command = input("Provide a command or enter 'exit' to exit the program: ").strip()
        if command.lower() == 'exit':
            print("Exiting the program")
            break
        elif command == 'SELECT *':
            print(data_base)
        elif command == 'SELECT 0':
            print(data_base[0])
        elif command == 'INSERT 0 "Apple"':
            data_base.insert(0, 'Apple')
            print(data_base)
        elif command == 'UPDATE 0 "Peach"':
            index_from_command = command.split(' ')[1]
            data_base[int(index_from_command)] = 'Peach'
            print(data_base)
        elif command == 'DELETE *':
            data_base.clear()
            print(data_base)
        elif command == 'DELETE 0':
            data_base.pop(0)
            print(data_base)
        elif command == 'SUM *':
            summ = 0
            for item in data_base:
                if isinstance(item, int) or isinstance(item, float):
                    summ += item
            print(summ)
        elif command == 'SUM 10':
            summ_of_numbers = 0
            numbers_found = 0
            for item in data_base:
                if isinstance(item, int) or isinstance(item, float):
                    summ_of_numbers += item
                    numbers_found += 1
                if numbers_found == 10:
                    break
            print(summ_of_numbers)
        elif command == 'AVG':
            average = 0
            summ = 0
            for item in range(len(data_base)):
                if isinstance(item, int) or isinstance(item, float):
                    summ += item
                average = summ / len(data_base)
            print(average)
        elif command == 'COUNT *':
            count = 0
            for i in data_base:
                count += 1
            print(count)
        elif command == 'COUNT "APPLE"':
            x = data_base.count('APPLE')
            print(x)
        else:
            print("Unknown command provided!")


simple_database()
