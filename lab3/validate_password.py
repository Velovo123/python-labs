from colorama import Fore, Style

# Введення паролю
password = input("Введіть пароль (мінімум 8 символів): ")

# Змінні для повідомлень
length_message = ("Довжина не менше 8 символів – FAIL!", "Довжина не менше 8 символів – OK!")
upp_message = ("Великі літери – FAIL!", "Великі літери – OK!")
low_message = ("Маленькі літери – FAIL!", "Маленькі літери – OK!")
num_message = ("Цифри – FAIL!", "Цифри – OK!")
spc_message = ("Спеціальні символи – FAIL!", "Спеціальні символи – OK!")
valid_message = ("Пароль не валідний!", "Пароль валідний!")

# Перевірки
length_check = len(password) >= 8

# Перевірка на наявність великих літер
upp_check = sum([
    "A" in password, "B" in password, "C" in password, "D" in password, "E" in password,
    "F" in password, "G" in password, "H" in password, "I" in password, "J" in password,
    "K" in password, "L" in password, "M" in password, "N" in password, "O" in password,
    "P" in password, "Q" in password, "R" in password, "S" in password, "T" in password,
    "U" in password, "V" in password, "W" in password, "X" in password, "Y" in password,
    "Z" in password
]) >= 1

# Перевірка на наявність маленьких літер
low_check = sum([
    "a" in password, "b" in password, "c" in password, "d" in password, "e" in password,
    "f" in password, "g" in password, "h" in password, "i" in password, "j" in password,
    "k" in password, "l" in password, "m" in password, "n" in password, "o" in password,
    "p" in password, "q" in password, "r" in password, "s" in password, "t" in password,
    "u" in password, "v" in password, "w" in password, "x" in password, "y" in password,
    "z" in password
]) >= 1

# Перевірка на наявність цифр
num_check = sum([
    "0" in password, "1" in password, "2" in password, "3" in password, "4" in password,
    "5" in password, "6" in password, "7" in password, "8" in password, "9" in password
]) >= 1

# Перевірка на наявність спеціальних символів
spc_check = sum([
    "!" in password, "@" in password, "#" in password, "$" in password, "%" in password,
    "^" in password, "&" in password, "*" in password, "_" in password, "-" in password
]) >= 1

# Вивід результатів перевірки
print(Fore.GREEN + length_message[length_check] + Style.RESET_ALL)
print(Fore.GREEN + upp_message[upp_check] + Style.RESET_ALL)
print(Fore.GREEN + low_message[low_check] + Style.RESET_ALL)
print(Fore.GREEN + num_message[num_check] + Style.RESET_ALL)
print(Fore.GREEN + spc_message[spc_check] + Style.RESET_ALL)

# Вивід загальної валідності пароля
valid = length_check * upp_check * low_check * num_check * spc_check
print(Fore.GREEN + valid_message[valid] + Style.RESET_ALL)
