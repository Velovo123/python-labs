from typing import List, Dict, Any

# Створення бази даних (двовимірний список) з інформацією про пиво
beer_database: List[Dict[str, Any]] = [
    {"Назва": "Оболонь", "Виробник": "Україна", "Міцність": 5.0, "Ціна": 30, "Термін зберігання": 180},
    {"Назва": "Львівське", "Виробник": "Україна", "Міцність": 4.5, "Ціна": 25, "Термін зберігання": 150},
    {"Назва": "Heineken", "Виробник": "Нідерланди", "Міцність": 5.0, "Ціна": 50, "Термін зберігання": 365},
    {"Назва": "Corona", "Виробник": "Мексика", "Міцність": 4.6, "Ціна": 45, "Термін зберігання": 300},
    {"Назва": "Budweiser", "Виробник": "США", "Міцність": 5.0, "Ціна": 40, "Термін зберігання": 180}
]

# a. Вивести весь список
def print_database(db: List[Dict[str, Any]]) -> None:
    print(f"{'Назва':<12}{'Виробник':<15}{'Міцність':<10}{'Ціна':<10}{'Термін зберігання':<15}")
    for beer in db:
        print(f"{beer['Назва']:<12}{beer['Виробник']:<15}{beer['Міцність']:<10}{beer['Ціна']:<10}{beer['Термін зберігання']:<15}")

# b. Додавати елементи до списку
def add_beer(db: List[Dict[str, Any]], name: str, manufacturer: str, strength: float, price: int, storage: int) -> None:
    db.append({"Назва": name, "Виробник": manufacturer, "Міцність": strength, "Ціна": price, "Термін зберігання": storage})

# c. Відсортувати список за заданим атрибутом
def sort_database(db: List[Dict[str, Any]], attribute: str) -> None:
    db.sort(key=lambda beer: beer[attribute])

# d. Видаляти елементи за заданим атрибутом
def delete_by_attribute(db: List[Dict[str, Any]], attribute: str, value: Any) -> None:
    db[:] = [beer for beer in db if beer[attribute] != value]

# e. Видаляти елемент за заданим індексом
def delete_by_index(db: List[Dict[str, Any]], index: int) -> None:
    if 0 <= index < len(db):
        db.pop(index)

# f. Виводити всі елементи за заданим атрибутом
def filter_by_attribute(db: List[Dict[str, Any]], attribute: str, value: Any) -> None:
    print(f"{'Назва':<12}{'Виробник':<15}{'Міцність':<10}{'Ціна':<10}{'Термін зберігання':<15}")
    for beer in db:
        if beer[attribute] == value:
            print(f"{beer['Назва']:<12}{beer['Виробник']:<15}{beer['Міцність']:<10}{beer['Ціна']:<10}{beer['Термін зберігання']:<15}")

# Основне меню
def main() -> None:
    while True:
        print("\nМеню")
        print("1 - Друк списку")
        print("2 - Додати елемент до списку")
        print("3 - Відсортувати список за заданим атрибутом")
        print("4 - Видалити елемент за заданим атрибутом")
        print("5 - Видалити елемент за заданим індексом")
        print("6 - Вивести елементи із заданим атрибутом")
        print("7 - Вихід")

        choice = input("Виберіть операцію натиснувши відповідну цифру: ")
        if choice == "1":
            print_database(beer_database)
        elif choice == "2":
            name = input("Назва: ")
            manufacturer = input("Виробник: ")
            strength = float(input("Міцність: "))
            price = int(input("Ціна: "))
            storage = int(input("Термін зберігання: "))
            add_beer(beer_database, name, manufacturer, strength, price, storage)
        elif choice == "3":
            attribute = input("Атрибут для сортування (Назва, Виробник, Міцність, Ціна, Термін зберігання): ")
            sort_database(beer_database, attribute)
        elif choice == "4":
            attribute = input("Атрибут для видалення (Назва, Виробник, Міцність, Ціна, Термін зберігання): ")
            value = input("Значення атрибуту для видалення: ")
            delete_by_attribute(beer_database, attribute, value)
        elif choice == "5":
            index = int(input("Введіть індекс для видалення: "))
            delete_by_index(beer_database, index)
        elif choice == "6":
            attribute = input("Атрибут для фільтрації (Назва, Виробник, Міцність, Ціна, Термін зберігання): ")
            value = input("Значення атрибуту для фільтрації: ")
            filter_by_attribute(beer_database, attribute, value)
        elif choice == "7":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
main()
