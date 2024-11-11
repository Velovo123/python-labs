# Початковий вміст каталогу
dir_content = (
    "_file1.doc\n"
    "file2.pdf\n"
    "file222_.docx\n"
    "cmd.exe\n"
    "sys.dll\n"
    "FiLe7_5.txt\n"
    "foto1.jpg\n"
    "song1.mp3\n"
    "!!!song2.mp3\n"
    "video.avi\n"
    "file9.txt\n"
    "file_3_document.docx\n"
    "my_document!!!.ppt\n"
    "main.c\n"
    "lab3.py\n"
    "lookup.xml\n"
    "pic1.png\n"
    "pic2.bmp\n"
)

# Перетворення на список для обробки
files = dir_content.strip().split("\n")

# Підрахунок загальної кількості файлів
total_files = len(files)
print("У каталозі є", total_files, "файлів")

# Підрахунок файлів з розширеннями mp3 і png
mp3_files = sum(file.endswith(".mp3") for file in files)
png_files = sum(file.endswith(".png") for file in files)
print("Файлів з розширенням mp3:", mp3_files)
print("Файлів з розширенням png:", png_files)

# Заміна розширення .avi на .xml
files = [file.replace(".avi", ".xml") if file.endswith(".avi") else file for file in files]
print("\nКаталог після заміни розширення .avi на .xml:")
print("\n".join(files))

# Приведення імен файлів до "T" - перша велика літера
files = [file.title() for file in files]
print("\nКаталог після приведення імен файлів до формату 'T':")
print("\n".join(files))

# Видалення файлів з розширенням xml
files = [file for file in files if not file.endswith(".xml")]
print("\nКаталог після видалення файлів з розширенням xml:")
print("\n".join(files))
