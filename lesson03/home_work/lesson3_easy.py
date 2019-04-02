# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def make_registration(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'


print('Задание 1:')
print(make_registration('Василий', 21, 'Москва'))
print('')

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def define_max_num(a, b, c):
    max_num = a if a > b else b
    if c > max_num:
        max_num = c
    return max_num


print('Задание 2, тестируем все три позиции для MAX числа:')
print(define_max_num(100, 20, 30))
print(define_max_num(10, 200, 30))
print(define_max_num(10, 20, 300))
print('')

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def find_longest_string(*strings):
    max_string = ''
    for string in strings:
        if len(string) > len(max_string):
            max_string = string
    return max_string


print('Задание 3:')
with open('lesson3_easy.py', encoding='utf-8') as file:
    print(find_longest_string(*file))
