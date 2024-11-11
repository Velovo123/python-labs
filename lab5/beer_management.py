# Початковий список пива
beers = [
    ["Corona", "Grupo Modelo", 4.5, 30.5, 180],
    ["Budweiser", "Anheuser-Busch", 5.0, 25.0, 120],
    ["Heineken", "Heineken International", 5.0, 27.5, 150],
    ["Stella Artois", "AB InBev", 5.2, 29.0, 180],
    ["Guinness", "Diageo", 4.2, 35.0, 240]
]

# Функція для форматованого виводу списку
def print_beers(beers):
    print(f"{'№':<3} {'Назва':<15} {'Виробник':<20} {'Міцність':<10} {'Ціна':<10} {'Термін зберігання (дні)':<25}")
    print("=" * 85)  # Розділювальна лінія для таблиці
    for i, beer in enumerate(beers, start=1):
        print(f"{i:<3} {beer[0]:<15} {beer[1]:<20} {beer[2]:<10} {beer[3]:<10} {beer[4]:<25}")

# Головне меню
while True:
    print("\nМеню")
    print("1 - Друк списку")
    print("2 - Додати елемент до списку")
    print("3 - Відсортувати список за заданим атрибутом")
    print("4 - Видалити елемент за заданим індексом")
    print("5 - Видалити елемент за заданим атрибутом")
    print("6 - Вивести елементи із заданим атрибутом")
    print("7 - Вихід")

    choice = input("Виберіть операцію натиснувши відповідну цифру: ")

    if choice == "1":
        # a. Вивести весь список
        print_beers(beers)

    elif choice == "2":
        # b. Додавати елементи до списку
        name = input("Введіть назву: ")
        manufacturer = input("Введіть виробника: ")
        strength = float(input("Введіть міцність (%): "))
        price = float(input("Введіть ціну: "))
        shelf_life = int(input("Введіть термін зберігання в днях: "))
        beers.append([name, manufacturer, strength, price, shelf_life])
        print("Елемент додано до списку.")

    elif choice == "3":
        # c. Відсортувати список за заданим атрибутом
        print("За яким атрибутом відсортувати:")
        print("1 - Назва")
        print("2 - Виробник")
        print("3 - Міцність")
        print("4 - Ціна")
        print("5 - Термін зберігання")
        attr_choice = input("Виберіть номер атрибуту: ")
        if attr_choice == "1":
            beers.sort(key=lambda x: x[0])
        elif attr_choice == "2":
            beers.sort(key=lambda x: x[1])
        elif attr_choice == "3":
            beers.sort(key=lambda x: x[2])
        elif attr_choice == "4":
            beers.sort(key=lambda x: x[3])
        elif attr_choice == "5":
            beers.sort(key=lambda x: x[4])
        print("Список відсортовано.")

    elif choice == "4":
        # d. Видаляти елементи за заданим індексом
        index = int(input("Введіть індекс для видалення (починаючи з 1): ")) - 1
        if 0 <= index < len(beers):
            beers.pop(index)
            print("Елемент видалено.")
        else:
            print("Невірний індекс.")

    elif choice == "5":
        # e. Видаляти елементи за заданим атрибутом
        print("За яким атрибутом видалити:")
        print("1 - Назва")
        print("2 - Виробник")
        print("3 - Міцність")
        print("4 - Ціна")
        print("5 - Термін зберігання")
        attr_choice = input("Виберіть номер атрибуту: ")
        attr_value = input("Введіть значення атрибуту: ")
        if attr_choice in ["3", "4", "5"]:
            attr_value = float(attr_value) if attr_choice in ["3", "4"] else int(attr_value)
        beers = [beer for beer in beers if beer[int(attr_choice) - 1] != attr_value]
        print("Елементи з заданим атрибутом видалені.")

    elif choice == "6":
        # f. Виводити всі елементи за заданим атрибутом
        print("За яким атрибутом вивести:")
        print("1 - Назва")
        print("2 - Виробник")
        print("3 - Міцність")
        print("4 - Ціна")
        print("5 - Термін зберігання")
        attr_choice = input("Виберіть номер атрибуту: ")
        attr_value = input("Введіть значення атрибуту: ")
        if attr_choice in ["3", "4", "5"]:
            attr_value = float(attr_value) if attr_choice in ["3", "4"] else int(attr_value)
        filtered_beers = [beer for beer in beers if beer[int(attr_choice) - 1] == attr_value]
        if filtered_beers:
            print_beers(filtered_beers)
        else:
            print("Не знайдено елементів із заданим атрибутом.")

    elif choice == "7":
        print("Вихід з програми.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
