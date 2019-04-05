# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


def list_sqrt_transform(some_list):
    return [x**2 for x in some_list]

print('Задание 1:')
print(list_sqrt_transform([1, 2, 4, 0]))
print('')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


def find_common_fruits(list1, list2):
    common = list1 + list2
    return [fruit for fruit in common if fruit in list1 and fruit in list2]


list1 = ['Apples', 'Apricots', 'Avocados', 'Bananas', 'Boysenberries', 'Blueberries', 'Bing Cherry']
list2 = ['Apples', 'Avocados', 'Bananas', 'Blueberries', 'Bing Cherry', 'Grapefruit', 'Grapes', 'Gooseberries', 'Guava']
print('Задание 2:')
print(find_common_fruits(list1, list2))
print('')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


def list_custom_transform(some_list):
    return [x for x in some_list if x % 3 == 0 and x > 0 and x % 4 != 0]


numbers_list = [random.randint(-100, 100) for x in range(100)]
print('Задание 3:')
print(list_custom_transform(numbers_list))
