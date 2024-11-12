import json
import pickle
from typing import List, Dict, Any

# Файл для збереження даних
TEXT_FILE = 'beer_database.txt'
OBJECT_FILE = 'beer_database.pkl'

# Створення бази даних (двовимірний список) з інформацією про пиво
beer_database: List[Dict[str, Any]] = [
    {"Назва": "Оболонь", "Виробник": "Україна", "Міцність": 5.0, "Ціна": 30, "Термін зберігання": 180},
    {"Назва": "Львівське", "Виробник": "Україна", "Міцність": 4.5, "Ціна": 25, "Термін зберігання": 150},
    {"Назва": "Heineken", "Виробник": "Нідерланди", "Міцність": 5.0, "Ціна": 50, "Термін зберігання": 365},
    {"Назва": "Corona", "Виробник": "Мексика", "Міцність": 4.6, "Ціна": 45, "Термін зберігання": 300},
    {"Назва": "Budweiser", "Виробник": "США", "Міцність": 5.0, "Ціна": 40, "Термін зберігання": 180}
]

# Функція для виведення бази даних
def print_database(db: List[Dict[str, Any]]) -> None:
    print(f"{'Назва':<12}{'Виробник':<15}{'Міцність':<10}{'Ціна':<10}{'Термін зберігання':<15}")
    for beer in db:
        print(f"{beer['Назва']:<12}{beer['Виробник']:<15}{beer['Міцність']:<10}{beer['Ціна']:<10}{beer['Термін зберігання']:<15}")

# Функція для додавання нового елемента
def add_beer(db: List[Dict[str, Any]], name: str, manufacturer: str, strength: float, price: int, storage: int) -> None:
    db.append({"Назва": name, "Виробник": manufacturer, "Міцність": strength, "Ціна": price, "Термін зберігання": storage})

# Функція для сортування за атрибутом
def sort_database(db: List[Dict[str, Any]], attribute: str) -> None:
    try:
        db.sort(key=lambda beer: beer[attribute])
    except KeyError:
        print("Неправильний атрибут для сортування.")

# Функція для видалення за атрибутом
def delete_by_attribute(db: List[Dict[str, Any]], attribute: str, value: Any) -> None:
    db[:] = [beer for beer in db if beer.get(attribute) != value]

# Функція для видалення за індексом
def delete_by_index(db: List[Dict[str, Any]], index: int) -> None:
    try:
        db.pop(index)
    except IndexError:
        print("Неправильний індекс.")

# Функція для фільтрації за атрибутом
def filter_by_attribute(db: List[Dict[str, Any]], attribute: str, value: Any) -> None:
    print(f"{'Назва':<12}{'Виробник':<15}{'Міцність':<10}{'Ціна':<10}{'Термін зберігання':<15}")
    for beer in db:
        if beer.get(attribute) == value:
            print(f"{beer['Назва']:<12}{beer['Виробник']:<15}{beer['Міцність']:<10}{beer['Ціна']:<10}{beer['Термін зберігання']:<15}")

# Завантаження списку з текстового файлу
def load_from_text_file() -> None:
    try:
        with open(TEXT_FILE, 'r', encoding='utf-8') as f:
            global beer_database
            beer_database = json.load(f)
        print("Список завантажено з текстового файлу.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Помилка завантаження з текстового файлу: {e}")

# Збереження списку у текстовий файл
def save_to_text_file() -> None:
    try:
        with open(TEXT_FILE, 'w', encoding='utf-8') as f:
            json.dump(beer_database, f, ensure_ascii=False, indent=4)
        print("Список збережено у текстовий файл.")
    except IOError as e:
        print(f"Помилка збереження у текстовий файл: {e}")

# Завантаження списку як об'єкт
def load_from_object_file() -> None:
    try:
        with open(OBJECT_FILE, 'rb') as f:
            global beer_database
            beer_database = pickle.load(f)
        print("Список завантажено як об'єкт.")
    except (FileNotFoundError, pickle.UnpicklingError) as e:
        print(f"Помилка завантаження як об'єкт: {e}")

# Збереження списку у файл як об'єкт
def save_to_object_file() -> None:
    try:
        with open(OBJECT_FILE, 'wb') as f:
            pickle.dump(beer_database, f)
        print("Список збережено як об'єкт.")
    except IOError as e:
        print(f"Помилка збереження як об'єкт: {e}")

# Основне меню
def main() -> None:
    load_from_text_file()  # Завантаження даних при запуску

    while True:
        print("\nМеню")
        print("1 - Друк списку")
        print("2 - Додати елемент до списку")
        print("3 - Відсортувати список за заданим атрибутом")
        print("4 - Видалити елемент за заданим атрибутом")
        print("5 - Видалити елемент за заданим індексом")
        print("6 - Вивести елементи із заданим атрибутом")
        print("7 - Зберегти список у текстовий файл")
        print("8 - Зберегти список у файл як об’єкт")
        print("9 - Завантажити список з текстового файлу")
        print("10 - Завантажити список як об’єкт")
        print("11 - Вихід")

        choice = input("Виберіть операцію натиснувши відповідну цифру: ")
        if choice == "1":
            print_database(beer_database)
        elif choice == "2":
            try:
                name = input("Назва: ")
                manufacturer = input("Виробник: ")
                strength = float(input("Міцність: "))
                price = int(input("Ціна: "))
                storage = int(input("Термін зберігання: "))
                add_beer(beer_database, name, manufacturer, strength, price, storage)
            except ValueError:
                print("Неправильний формат введених даних.")
        elif choice == "3":
            attribute = input("Атрибут для сортування (Назва, Виробник, Міцність, Ціна, Термін зберігання): ")
            sort_database(beer_database, attribute)
        elif choice == "4":
            attribute = input("Атрибут для видалення (Назва, Виробник, Міцність, Ціна, Термін зберігання): ")
            value = input("Значення атрибуту для видалення: ")
            delete_by_attribute(beer_database, attribute, value)
        elif choice == "5":
            try:
                index = int(input("Введіть індекс для видалення: "))
                delete_by_index(beer_database, index)
            except ValueError:
                print("Неправильний індекс.")
        elif choice == "6":
            attribute = input("Атрибут для фільтрації (Назва, Виробник, Міцність, Ціна, Термін зберігання): ")
            value = input("Значення атрибуту для фільтрації: ")
            filter_by_attribute(beer_database, attribute, value)
        elif choice == "7":
            save_to_text_file()
        elif choice == "8":
            save_to_object_file()
        elif choice == "9":
            load_from_text_file()
        elif choice == "10":
            load_from_object_file()
        elif choice == "11":
            print("Збереження перед виходом.")
            save_to_text_file()  # Зберігання при виході
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Виконання програми
main()
