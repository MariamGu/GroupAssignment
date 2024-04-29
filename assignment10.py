# Task 1
def recursive_mult(a, b):
    if b == 1:
        return a
    else:
        return a + recursive_mult(a, b - 1)


# Task 2

def reversed_string(string):
    if string == "":
        return string
    else:
        return reversed_string(string[1:]) + string[0]


# Task 3

def sum_of_list(lst):
    if isinstance(lst, int):
        return lst
    summ = 0
    for item in lst:
        summ += sum_of_list(item)
    return summ

