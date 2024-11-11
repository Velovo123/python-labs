import math

# Функція для обчислення значення залежно від x
def calculate_function(x):
    if x < 4:
        return (1 + math.cos(x)) / (1 - math.sin(x ** 2))
    elif 4 <= x < 5:
        return math.atan(math.log(x + math.sin(x)))
    else:
        return 1 / (x ** 2) + 1 / (x ** 3) + 1 / (x ** 4)

# Параметри
a, b = 3, 6
h = 0.2

# Табулювання
x = a
print(f"{'x':<10}{'y':<15}")
while x <= b:
    y = calculate_function(x)
    print(f"{x:<10.1f}{y:<15.4f}")
    x += h
