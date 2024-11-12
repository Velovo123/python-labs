import os
import shutil

# Довідник для каталогів
base_dir = 'folder_1'
folder_2 = os.path.join(base_dir, 'folder_2')
folder_3 = os.path.join(base_dir, 'folder_3')
folder_4 = os.path.join(base_dir, 'folder_4')

# 1. Вивести вміст каталогу folder_1 і його підкаталогів.
def list_contents(directory: str) -> None:
    for root, dirs, files in os.walk(directory):
        print(f"Directory: {root}")
        for dir_name in dirs:
            print(f"  [DIR] {dir_name}")
        for file_name in files:
            print(f"  [FILE] {file_name}")

# 2. Створити в каталогу folder_1 підкаталог folder_4.
def create_folder(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)
    print(f"Created folder: {directory}")

# 6. Скопіювати в підкаталог folder_4 всі файли з каталогу folder_2 з розширенням *.pdf.
def copy_files_with_extension(source_folder: str, target_folder: str, extension: str) -> None:
    for filename in os.listdir(source_folder):
        if filename.endswith(extension):
            shutil.copy(os.path.join(source_folder, filename), target_folder)
            print(f"Copied {filename} to {target_folder}")

# 18. Перемістити в підкаталог folder_4 всі файли з каталогу folder_3 з розширенням *.txt.
def move_files_with_extension(source_folder: str, target_folder: str, extension: str) -> None:
    for filename in os.listdir(source_folder):
        if filename.endswith(extension):
            shutil.move(os.path.join(source_folder, filename), target_folder)
            print(f"Moved {filename} to {target_folder}")

# 23. Перейменувати в каталогу folder_1 всі файли з розширенням *.txt в ім’я файлу_2024.txt
def rename_files_in_folder(directory: str, extension: str, suffix: str) -> None:
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            name, _ = os.path.splitext(filename)
            new_name = f"{name}_{suffix}{extension}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")

# 52. Видалити в підкаталогу folder_3 всі файли з розширенням .doc.
def delete_files_with_extension(directory: str, extension: str) -> None:
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            os.remove(os.path.join(directory, filename))
            print(f"Deleted {filename}")

# 56. Видалити підкаталог folder_2.
def delete_folder(directory: str) -> None:
    shutil.rmtree(directory, ignore_errors=True)
    print(f"Deleted folder: {directory}")

# Виконання операцій
print("1. Вміст каталогу folder_1 та його підкаталогів:")
list_contents(base_dir)
print("\n2. Створення каталогу folder_4:")
create_folder(folder_4)
print("\n6. Копіювання всіх файлів з розширенням *.pdf з folder_2 до folder_4:")
copy_files_with_extension(folder_2, folder_4, '.pdf')
print("\n18. Переміщення всіх файлів з розширенням *.txt з folder_3 до folder_4:")
move_files_with_extension(folder_3, folder_4, '.txt')
print("\n23. Перейменування всіх файлів з розширенням *.txt в folder_1:")
rename_files_in_folder(base_dir, '.txt', '2024')
print("\n52. Видалення всіх файлів з розширенням .doc в folder_3:")
delete_files_with_extension(folder_3, '.doc')
print("\n56. Видалення каталогу folder_2:")
delete_folder(folder_2)
