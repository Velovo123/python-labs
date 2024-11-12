import random

# Інформація про студента
def display_student_info():
    print("Семенчук Анатолій Анатолійович, КБ-305, 2024. Варіант 27")

# Функція для введення кількості символів
def get_symbol_counts():
    upp_count = int(input("Введіть кількість великих латинських літер в паролі: "))
    low_count = int(input("Введіть кількість малих латинських літер в паролі: "))
    num_count = int(input("Введіть кількість цифр в паролі: "))
    spc_count = int(input("Введіть кількість спеціальних символів !@#$%^&*_- в паролі: "))
    return upp_count, low_count, num_count, spc_count

# Функція для генерації паролю
def generate_password(upp_count, low_count, num_count, spc_count):
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
    
    # Перемішування символів і повернення паролю
    random.shuffle(password)
    return "".join(password)

# Основна програма
display_student_info()
upp_count, low_count, num_count, spc_count = get_symbol_counts()
password = generate_password(upp_count, low_count, num_count, spc_count)
print("Password:", password)
