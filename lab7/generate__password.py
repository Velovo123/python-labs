import random

# Набори символів
upp_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_char = "abcdefghijklmnopqrstuvwxyz"
num_char = "0123456789"
spc_char = "!@#$%^&*_-"

# Функція для генерації пароля
def generate_password(upp_count: int, low_count: int, num_count: int, spc_count: int) -> str:
    # Вибір випадкових символів з кожного набору
    password = (
        random.sample(upp_char, upp_count) +
        random.sample(low_char, low_count) +
        random.sample(num_char, num_count) +
        random.sample(spc_char, spc_count)
    )
    # Перемішування символів у паролі
    random.shuffle(password)
    return ''.join(password)

# Введення кількості символів для кожного типу
print("Введіть кількість символів для кожного типу:")
upp_count = int(input("Введіть кількість великих латинських літер у паролі: "))
low_count = int(input("Введіть кількість малих латинських літер у паролі: "))
num_count = int(input("Введіть кількість цифр у паролі: "))
spc_count = int(input("Введіть кількість спеціальних символів у паролі (!@#$%^&*-_): "))

# Генерація пароля
password = generate_password(upp_count, low_count, num_count, spc_count)

# Вивід результату
print("Згенерований пароль:", password)
