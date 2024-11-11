import math

# Функція для обчислення значення ряду з похибкою
def calculate_series(x, d):
    n = 1
    term = x / ((3 * n - 1) ** 3 * math.sin(n + 2))
    total_sum = 1 + term
    while abs(term) >= d:
        n += 1
        term = x / ((3 * n - 1) ** 3 * math.sin(n + 2))
        total_sum += term
    return total_sum

# Параметри
a, b = 0.1, 0.6  # Інтервал для x
h = 0.05         # Крок табуляції
d = 0.001        # Допустима похибка

# Табулювання
x = a
print(f"{'x':<10}{'y':<15}{'error':<15}")
while x <= b:
    y = calculate_series(x, d)
    error = d
    print(f"{x:<10.2f}{y:<15.5f}{error:<15.5f}")
    x += h
