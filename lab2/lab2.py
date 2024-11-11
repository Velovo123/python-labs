import math

# Інформація про студента
variant_number = 27
first_name = "Семенчук"
last_name = ""

# Виведення інформації про студента
print(f"Номер варіанту: {variant_number}")
print(f"Прізвище та ім'я: {first_name} {last_name}")

# Введення значень змінних
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))
z = float(input("Введіть значення z: "))

# Виведення формули для обчислення
print("Формула: ln(x^4 + y^5 + z^6) - tg(cos(z)) + ⁴√(z + x + y^2)")

# Обчислення виразу
try:
    result = (  
        math.log(x**4 + y**5 + z**6) 
        - math.tan(math.cos(z)) 
        + (z + x + y**2)**(1/4)
    )
    result = round(result, 2)
    # Виведення результату
    print(f"Результат: {result}")
except ValueError as e:
    print(f"Помилка в обчисленні: {e}")
