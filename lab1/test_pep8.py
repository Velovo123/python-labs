'''Тестовий файл для ознайомлення з правилами форматування і оформлення коду згідно Python Enhancement Proposals PEP 8 – Style Guide for Python Code.'''


import string
import os
import math, time  # Порушення: імпорти повинні бути в окремих рядках, один модуль на рядок.

shift = 3
PI= 3.14  # Порушення: відсутній пробіл до і після знака присвоєння `=`.
def PrintTime(x):  # Порушення: назви функцій мають бути у форматі snake_case, тобто `print_time`.
   if x == True:  # Порушення: порівняння з `True` потрібно виконувати через `if x:` або `if not x:`.
      print( time.ctime() )  # Порушення: зайві пробіли всередині дужок `()`.
   return  # Порушення: return без значення не потрібен, якщо немає чого повертати.

def main ():  # Порушення: зайвий пробіл перед `()` у визначенні функції.


    Choice_mode = input("would you like to encode or decode?")  # Порушення: назва змінної повинна бути в форматі snake_case.
    word = input("Please enter text")
    LETTERS = string.ascii_letters + string.punctuation + string.digits  # Порушення: великі літери зазвичай використовуються для констант. Це не єдина загальноприйнята константа, тому краще використовувати малі літери.
    encoded = ""
    if Choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " "  # Порушення: для конкатенації рядків краще використовувати `+=`.
            else:
                x = LETTERS.index(letter) + shift
                encoded = encoded + LETTERS[x]  # Порушення: для конкатенації рядків краще використовувати `+=`.
                y=x + 5  # Порушення: відсутній пробіл до і після знака `=`.



    if Choice_mode is "decode":  # Порушення: для порівняння рядків використовуйте `==`, а не `is`.
        for letter in word:
            if letter == " ":
                encoded = encoded+" "  # Порушення: для конкатенації рядків краще використовувати `+=`.
            else:
                x = LETTERS.index(letter)- shift  # Порушення: відсутній пробіл до і після оператора `-`.
                encoded=encoded + LETTERS[x]  # Порушення: для конкатенації рядків краще використовувати `+=`.
                y= x - 5  # Порушення: відсутній пробіл до і після оператора `=`.

    print(encoded)
    print(Word)  # Порушення: змінна `Word` не визначена. Можливо, мала бути `word`.


if __name__ == '__main__':  # Порушень немає, цей рядок відповідає PEP 8.
    main()
