from colorama import Fore, Style

# Введення паролю
password = input("Введіть пароль довжиною не менше 10 символів: ")

# Вимоги до символів
upp_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_char = "abcdefghijklmnopqrstuvwxyz"
num_char = "0123456789"
spc_char = "!@#$%^&*_-"

# Перевірка довжини пароля
length_check = len(password) >= 10

# Перевірка дозволених символів
allowed_chars_check = all(c in (upp_char + low_char + num_char + spc_char) for c in password)

# Підрахунок кількості кожного типу символів
low_count = sum(1 for c in password if c in low_char)
upp_count = sum(1 for c in password if c in upp_char)
num_count = sum(1 for c in password if c in num_char)
spc_count = sum(1 for c in password if c in spc_char)

# Валідація кожного правила
rules = {
    "Довжина не менше 10 символів": length_check,
    "Пароль містить лише допустимі символи": allowed_chars_check,
    "Не менше 2 маленьких латинських літер": low_count >= 2,
    "Не більше 4 маленьких латинських літер": low_count <= 4,
    "Не менше 2 цифр": num_count >= 2,
    "Не більше 4 цифр": num_count <= 4,
    "Не менше 2 спеціальних символів": spc_count >= 2,
    "Не більше 3 спеціальних символів": spc_count <= 3,
    "Не менше 2 великих латинських літер": upp_count >= 2,
    "Не більше 5 великих латинських літер": upp_count <= 5,
    "Не більше 3 однакових великих латинських літер підряд": not any(password[i] == password[i+1] == password[i+2] for i in range(len(password) - 2) if password[i] in upp_char),
    "Не більше 3 однакових спеціальних символів підряд": not any(password[i] == password[i+1] == password[i+2] for i in range(len(password) - 2) if password[i] in spc_char)
}

# Вивід результатів перевірки для кожного правила
print("\nВимоги до паролю:")
for rule, passed in rules.items():
    color = Fore.GREEN if passed else Fore.RED
    status = "OK!" if passed else "FAIL!"
    print(f"{rule} - {color}{status}{Style.RESET_ALL}")

# Перевірка загальної валідності пароля
is_valid = all(rules.values())
print(Fore.GREEN + "Пароль валідний!" + Style.RESET_ALL if is_valid else Fore.RED + "Пароль не валідний!" + Style.RESET_ALL)
