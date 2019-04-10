import os
import inspect
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def make_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print("Директория ", dir_name, " была создана")
    except FileExistsError:
        print('Такая директория уже существует')


def del_dir(dir_name):
    try:
        if os.path.isdir(dir_name):
            os.rmdir(dir_name)
            print("Директория ", dir_name, " была удалена")
    except FileNotFoundError:
        print('Такой директории не существует')
    except PermissionError:
        print('Нет прав для удаления директории')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dir(dir_name):
    try:
        if os.path.isdir(dir_name):
            for item in os.listdir(dir_name):
                if os.path.isdir(item):
                    print(item)
    except FileNotFoundError:
        print('Такой директории не существует')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def make_copy():
    try:
        file = os.path.basename(inspect.stack()[1][1])
        shutil.copy(f'{file}', f'copy_{file}')
        print(f'Файл copy_{file} создан')
    except FileNotFoundError:
        print('Нет файла для копирования')


if __name__ == '__main__':
    print('Задача-1:')
    print('Первая часть задачи 1. Создание директорий:')
    for i in range(1, 10):
        make_dir(f'dir_{i}')
    print('Задача-2:')
    print('Отобразить папки текущей директории:')
    show_dir(os.getcwd())
    print('Вторая часть задачи 1. Удаление директорий:')
    for i in range(1, 10):
        del_dir(f'dir_{i}')
    print('Задача-3:')
    print('Создать копию файла, из которого запущен скрипт:')
    make_copy()
