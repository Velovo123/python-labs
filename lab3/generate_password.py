import random

# Інформація про студента
print("Семенчук Анатолій Анатолійовчи, КБ-305, 2024. Варіант 27")

# Введення кількості символів
upp_count = int(input("Введіть кількість великих латинських літер в паролі: "))
low_count = int(input("Введіть кількість малих латинських літер в паролі: "))
num_count = int(input("Введіть кількість цифр в паролі: "))
spc_count = int(input("Введіть кількість спеціальних символів !@#$%^&*_- в паролі: "))

# Символи для паролю
low_char = "abcdefghijklmnopqrstuvwxyz"
upp_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_char = "0123456789"
spc_char = "!@#$%^&*_-"

# Формування паролю
password = (
    random.sample(low_char, low_count) +
    random.sample(num_char, num_count) +
    random.sample(spc_char, spc_count) +
    random.sample(upp_char, upp_count)
)

# Перемішування символів і виведення паролю
random.shuffle(password)
print("Password:", "".join(password))
