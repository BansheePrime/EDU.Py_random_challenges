# 2. Sort a list
'''
https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.

'''


def sorting_machine(*args):

    if sort_type == "2":
        numbers_list.sort(reverse=True)
    elif sort_type == "1":
        numbers_list.sort()
    else:
        numbers_list

    return numbers_list


numbers_list = [7, 98, 658, 54, 4545, 566, 89794, 98, 5421]
sort_type = input("Please enter 1 for ascending or 2 for descending order of your list: ")
print(sorting_machine(numbers_list, sort_type))
