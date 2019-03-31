import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


def list_itemizer(some_list):
    max_word_len = max(some_list, key=lambda x: len(x))
    order_number = 1
    for item in some_list:
        print(f'{order_number}. {item.rjust(len(max_word_len))}')
        order_number += 1


print('Задача-1, результат:')
L = ["яблоко", "банан", "киви", "арбуз"]
list_itemizer(L)
print('')


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

def list_clearing(list1, list2):
    for item in list1[:]:
        if item in list2:
            while item in list1:
                list1.remove(item)
    return list1


list1 = [1, 1, 1, 2, 2, 3, 4, 5, 6]
list2 = [1, 2, 2, 3, 10]
print('Задача-2, результат:')
print(list_clearing(list1, list2))
print('')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def new_list_maker(some_int_list):
    new_list = []
    for number in some_int_list:
        if number % 2 == 0:
            new_list.append(number/4)
        else:
            new_list.append(number*2)
    return new_list


int_list = [random.randint(0, 1000) for _ in range(20)]
new_list = new_list_maker(int_list)
print('Задача-3, результат:')
for item1, item2 in zip(int_list, new_list):
    print(f'Было: {item1}, стало: {item2}')
