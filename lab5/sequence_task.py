# Спосіб 1: Створення списку за допомогою циклу
n = -2
step = 2
length = 15

# Створення списку за допомогою циклу
list_1 = []
for i in range(length):
    list_1.append(n ** 2)
    n += step

print("Список, створений циклом:", list_1)

# Спосіб 2: Створення списку за допомогою генератора списків
n = -2
list_2 = [(n + i * step) ** 2 for i in range(length)]
print("Список, створений генератором списків:", list_2)

# Пункт a: Виведення елементів з індексами від 3 до 5
print("Елементи з індексами від 3 до 5:", list_1[3:6])

# Пункт b: Замінити перший елемент останнім
modified_list = list_1.copy()
modified_list[0] = modified_list[-1]
print("Список після заміни першого елемента останнім:", modified_list)

# Пункт c: Об'єднання початкового списку і списку з пункту b
combined_list = list_1 + modified_list
print("Об'єднаний список:", combined_list)

# Пункт d: Додавання трьох елементів, рівних першим трьом елементам
extended_list = combined_list + combined_list[:3]
print("Список після додавання перших трьох елементів:", extended_list)

# Пункт e: Виведення максимального і мінімального значення в списку
max_value = max(extended_list)
min_value = min(extended_list)
print("Максимальне значення:", max_value)
print("Мінімальне значення:", min_value)

# Пункт f: Видалення всіх елементів менших за середнє значення
average_value = sum(extended_list) / len(extended_list)
filtered_list = [x for x in extended_list if x >= average_value]
print("Список після видалення елементів, менших за середнє значення:", filtered_list)
