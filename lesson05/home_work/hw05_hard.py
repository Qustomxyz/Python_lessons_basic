# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not path_chunk:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), path_chunk)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(path_chunk))
    except FileExistsError:
        print('директория {} уже существует'.format(path_chunk))


def ping():
    print("pong")


def copy_file():
    if not path_chunk:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        file = os.path.basename(path_chunk)
        shutil.copy(f'{file}', f'copy_{file}')
        print(f'Файл copy_{file} создан')
    except FileNotFoundError:
        print('Нет файла для копирования')


def del_file():
    if not path_chunk:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        file = os.path.basename(path_chunk)
        if os.path.isfile(file):
            print(f'Вы действительно хотите удалить файл {file}?')
            answer = input('да/нет: ')
            if answer in ('да', 'y', 'yes'):
                os.remove(file)
                print("\nФайл ", path_chunk, " был удален")
            else:
                print("\nУдаление отменено")
        else:
            print('\nТакой файл не существует')
    except PermissionError:
        print('Нет прав для удаления файла')


def change_directory():
    if not path_chunk:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(path_chunk)
        print('Текущая директория:')
        print(os.getcwd())
    except OSError:
        print('\nУказан неверный путь или такой директории не существует.\n')


def show_full_path():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "cd": change_directory,
    "ls": show_full_path
}

try:
    path_chunk = sys.argv[2]
except IndexError:
    path_chunk = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
