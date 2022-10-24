# 4. Count the vowels in a string
'''
https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.
'''
vowels_list = ["a", "e", "i", "o", "u"]
user_word = input("Please, enter a word: ")


def vowels_count(user_word):
    v_count = 0

    for i in user_word:
        if i in vowels_list:
            v_count = v_count + 1

    return print(f"There is {v_count} vowels in your word.")


vowels_count(user_word)
