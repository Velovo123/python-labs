# Кількість елементів, початкове значення та крок
n_elements = 15
initial_value = -2
step = 2

# Створення кортежу з n елементів за формулою n^2
numbers = tuple((initial_value + i * step) ** 2 for i in range(n_elements))
print("Початковий кортеж:", numbers)

# a. Виведіть елементи з індексами від 3 до 5
print("Елементи з індексами від 3 до 5:", numbers[3:6])

# b. Замініть перший елемент останнім
modified_numbers = (numbers[-1],) + numbers[1:-1] + (numbers[0],)
print("Кортеж після заміни першого елемента останнім:", modified_numbers)

# c. Об’єднайте початковий кортеж і отриманий на кроці b
combined_numbers = numbers + modified_numbers
print("Об'єднаний кортеж:", combined_numbers)

# d. Додайте до кортежу ще три елементи зі значеннями перших трьох
extended_numbers = combined_numbers + numbers[:3]
print("Кортеж після додавання трьох перших елементів:", extended_numbers)

# e. Виведіть максимальне і мінімальне значення в кортежі
max_value = max(extended_numbers)
min_value = min(extended_numbers)
print("Максимальне значення:", max_value)
print("Мінімальне значення:", min_value)

# f. Видаліть всі елементи менші за середньоарифметичне значення
average_value = sum(extended_numbers) / len(extended_numbers)
filtered_numbers = tuple(x for x in extended_numbers if x >= average_value)
print("Кортеж після видалення елементів менших за середнє:", filtered_numbers)
