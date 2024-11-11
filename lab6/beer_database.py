# Початкова база даних пива
database = [
    {"Назва": "Corona", "Виробник": "Grupo Modelo", "Міцність": 4.5, "Ціна": 30.5, "Термін зберігання": 180},
    {"Назва": "Budweiser", "Виробник": "Anheuser-Busch", "Міцність": 5.0, "Ціна": 25.0, "Термін зберігання": 120},
    {"Назва": "Heineken", "Виробник": "Heineken International", "Міцність": 5.0, "Ціна": 27.5, "Термін зберігання": 150},
    {"Назва": "Stella Artois", "Виробник": "AB InBev", "Міцність": 5.2, "Ціна": 29.0, "Термін зберігання": 180},
    {"Назва": "Guinness", "Виробник": "Diageo", "Міцність": 4.2, "Ціна": 35.0, "Термін зберігання": 240}
]

# Функція для виводу всієї бази даних
def print_database(db):
    print(f"{'№':<3} {'Назва':<15} {'Виробник':<20} {'Міцність':<10} {'Ціна':<10} {'Термін зберігання (дні)':<25}")
    print("=" * 80)
    for i, entry in enumerate(db, start=1):
        print(f"{i:<3} {entry['Назва']:<15} {entry['Виробник']:<20} {entry['Міцність']:<10} {entry['Ціна']:<10} {entry['Термін зберігання']:<25}")

# Головне меню
while True:
    print("\nМеню")
    print("1 - Вивести всю БД")
    print("2 - Додати елемент до БД")
    print("3 - Відсортувати БД за заданим атрибутом")
    print("4 - Видалити елемент за заданим індексом")
    print("5 - Видалити елемент за заданим значенням")
    print("6 - Вивести всі елементи за заданим атрибутом")
    print("7 - Вихід")

    choice = input("Виберіть операцію натиснувши відповідну цифру: ")

    if choice == "1":
        # a. Вивести всю БД
        print_database(database)

    elif choice == "2":
        # b. Додавати елементи до БД
        name = input("Введіть назву: ")
        manufacturer = input("Введіть виробника: ")
        strength = float(input("Введіть міцність (%): "))
        price = float(input("Введіть ціну: "))
        shelf_life = int(input("Введіть термін зберігання в днях: "))
        database.append({"Назва": name, "Виробник": manufacturer, "Міцність": strength, "Ціна": price, "Термін зберігання": shelf_life})
        print("Елемент додано до бази даних.")

    elif choice == "3":
        # c. Відсортувати БД за заданим атрибутом
        print("За яким атрибутом відсортувати:")
        print("1 - Назва")
        print("2 - Виробник")
        print("3 - Міцність")
        print("4 - Ціна")
        print("5 - Термін зберігання")
        attr_choice = input("Виберіть номер атрибуту: ")
        attr_map = {"1": "Назва", "2": "Виробник", "3": "Міцність", "4": "Ціна", "5": "Термін зберігання"}
        if attr_choice in attr_map:
            database.sort(key=lambda x: x[attr_map[attr_choice]])
            print("База даних відсортована.")

    elif choice == "4":
        # d. Видаляти елементи за заданим індексом
        index = int(input("Введіть індекс для видалення (починаючи з 1): ")) - 1
        if 0 <= index < len(database):
            database.pop(index)
            print("Елемент видалено.")
        else:
            print("Невірний індекс.")

    elif choice == "5":
        # e. Видаляти елемент за заданим значенням
        print("За яким атрибутом видалити:")
        print("1 - Назва")
        print("2 - Виробник")
        print("3 - Міцність")
        print("4 - Ціна")
        print("5 - Термін зберігання")
        attr_choice = input("Виберіть номер атрибуту: ")
        attr_map = {"1": "Назва", "2": "Виробник", "3": "Міцність", "4": "Ціна", "5": "Термін зберігання"}
        if attr_choice in attr_map:
            attr_value = input("Введіть значення атрибуту: ")
            if attr_choice in ["3", "4", "5"]:
                attr_value = float(attr_value) if "." in attr_value else int(attr_value)
            database = [entry for entry in database if entry[attr_map[attr_choice]] != attr_value]
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
        attr_map = {"1": "Назва", "2": "Виробник", "3": "Міцність", "4": "Ціна", "5": "Термін зберігання"}
        if attr_choice in attr_map:
            attr_value = input("Введіть значення атрибуту: ")
            if attr_choice in ["3", "4", "5"]:
                attr_value = float(attr_value) if "." in attr_value else int(attr_value)
            filtered_entries = [entry for entry in database if entry[attr_map[attr_choice]] == attr_value]
            if filtered_entries:
                print_database(filtered_entries)
            else:
                print("Не знайдено елементів із заданим атрибутом.")

    elif choice == "7":
        print("Вихід з програми.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
