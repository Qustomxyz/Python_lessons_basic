import os
import hw05_easy

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def main():
    while True:
        try:
            choice = int(input('Выберите пункт:\n'
                               '1. Перейти в папку\n'
                               '2. Просмотреть содержимое текущей папки\n'
                               '3. Удалить папку\n'
                               '4. Создать папку\n'
                               '5. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:'))
            if choice == 5:
                break
            process_user_choice(choice)
        except ValueError:
            print('\nНеверный ввод, попробуйте еще раз\n')


def process_user_choice(choice):
    if choice == 1:
        dir_name = input('В какую папку надо перейти: ')
        if dir_name:
            change_dir(dir_name)
    elif choice == 2:
        list_dir(os.getcwd())
    elif choice == 3:
        dir_name = input('Какую папку надо удалить: ')
        hw05_easy.del_dir(dir_name)
    elif choice == 4:
        dir_name = input('Какую папку надо создать: ')
        hw05_easy.make_dir(dir_name)


def change_dir(dir_name):
    try:
        os.chdir(dir_name)
        print('Текущая директория:')
        print(os.getcwd())
    except OSError:
        print('\nУказан неверный путь или такой директории не существует.\n')


def list_dir(dir_name):
    print('\nСодержимое текущей дериктории:')
    for item in os.listdir(dir_name):
        print(item)
    print('')


if __name__ == '__main__':
    main()
