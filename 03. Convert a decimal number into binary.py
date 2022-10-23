# 3. Convert a decimal number into binary
'''
https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.

'''

a = int(input("Please, enter the number: "))


def my_bin_calc(user_number):
    user_number = a
    div_result = []
    bin_result = []

    div_result.append(user_number)

    while user_number // 2 != 0:
        user_number = user_number // 2
        div_result.append(user_number)

    for i in div_result:
        b = i % 2
        bin_result.append(b)

    bin_result.reverse()
    return print(*bin_result, sep='')


my_bin_calc(a)