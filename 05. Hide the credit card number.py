# 5. Hide the credit card number
'''
https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "4444444444444444", then it should return "4444".
'''

card_number = input("Please, enter the credit card number: ")


def hiding_numbers(card_number):
    secret_string = ['*', '*', '*', '*', ' ', '*', '*', '*', '*', ' ', '*', '*', '*', '*']
    # number_string = str(card_number)
    # number_list = list(number_string)
    number_list = list(card_number)
    for i in str(number_list[-4:]):
        secret_string.append(i)
    return print(secret_string)


hiding_numbers(card_number)
