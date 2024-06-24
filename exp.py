import os
import time

directory = './.venv'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_time))
        parent_dir = os.path.dirname(file_path)

        print(f"Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {file_time},"
              f"Родительская директория: {parent_dir}")


