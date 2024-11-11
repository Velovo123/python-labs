"""Тестовий файл для ознайомлення з правилами форматування і оформлення коду.

Згідно Python Enhancement Proposals PEP 8 – Style Guide for Python Code.
"""


import string
import time

SHIFT = 3
PI = 3.14

def print_time(x):
    """Виводить поточний час, якщо значення x є істинним."""
    if x:
        print(time.ctime())

def main():
    """Основна функція для кодування або декодування тексту."""
    choice_mode = input("Would you like to encode or decode? ")
    word = input("Please enter text: ")
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ""
    if choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                x = letters.index(letter) + SHIFT
                encoded += letters[x]

    elif choice_mode == "decode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                x = letters.index(letter) - SHIFT
                encoded += letters[x]

    print(encoded)
    print(word)

if __name__ == '__main__':
    main()
