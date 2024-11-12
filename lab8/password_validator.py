from colorama import Fore, Style

# Набори символів
upp_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_char = "abcdefghijklmnopqrstuvwxyz"
num_char = "0123456789"
spc_char = "!@#$%^&*_-"

# Функція для перевірки кожного правила
def check_rule(description: str, condition: bool) -> str:
    color = Fore.GREEN if condition else Fore.RED
    status = "OK!" if condition else "FAIL!"
    print(f"{description} - {color}{status}{Style.RESET_ALL}")
    return condition

# Функція для перевірки пароля на слабкість
def is_password_weak(password: str, filename: str = "weak_passwords.txt") -> bool:
    try:
        with open(filename, "r") as file:
            weak_passwords = {line.strip() for line in file}  # Зчитуємо слабкі паролі у множину
        return password in weak_passwords
    except FileNotFoundError:
        print(Fore.RED + "Файл зі слабкими паролями не знайдено!" + Style.RESET_ALL)
        return False

# Основна функція для валідації пароля
def validate_password(password: str) -> None:
    # Перевірка слабкості пароля
    if is_password_weak(password):
        print(Fore.RED + "Пароль слабкий! Він знаходиться у списку слабких паролів." + Style.RESET_ALL)
        return

    # Перевірка довжини пароля
    length_check = check_rule("Довжина не менше 10 символів", len(password) >= 10)

    # Перевірка дозволених символів
    allowed_chars_check = check_rule("Пароль містить лише допустимі символи",
                                     all(c in (upp_char + low_char + num_char + spc_char) for c in password))

    # Підрахунок кількості кожного типу символів
    low_count = sum(1 for c in password if c in low_char)
    upp_count = sum(1 for c in password if c in upp_char)
    num_count = sum(1 for c in password if c in num_char)
    spc_count = sum(1 for c in password if c in spc_char)

    # Валідація кожного правила
    rules = [
        ("Не менше 2 маленьких латинських літер", low_count >= 2),
        ("Не більше 4 маленьких латинських літер", low_count <= 4),
        ("Не менше 2 цифр", num_count >= 2),
        ("Не більше 4 цифр", num_count <= 4),
        ("Не менше 2 спеціальних символів", spc_count >= 2),
        ("Не більше 3 спеціальних символів", spc_count <= 3),
        ("Не менше 2 великих латинських літер", upp_count >= 2),
        ("Не більше 5 великих латинських літер", upp_count <= 5),
        ("Не більше 3 однакових великих латинських літер підряд",
         not any(password[i] == password[i+1] == password[i+2] for i in range(len(password) - 2) if password[i] in upp_char)),
        ("Не більше 3 однакових спеціальних символів підряд",
         not any(password[i] == password[i+1] == password[i+2] for i in range(len(password) - 2) if password[i] in spc_char))
    ]

    # Перевірка правил
    results = [check_rule(description, condition) for description, condition in rules]

    # Перевірка загальної валідності пароля
    is_valid = all([length_check, allowed_chars_check] + results)
    print(Fore.GREEN + "Пароль валідний!" + Style.RESET_ALL if is_valid else Fore.RED + "Пароль не валідний!" + Style.RESET_ALL)

# Запит на введення пароля
password = input("Введіть пароль довжиною не менше 10 символів: ")
validate_password(password)
