# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
import os


def make_salary_dict(names_list, salary_list):
    return dict(zip(names_list, salary_list))


def make_salary_txt(salary_dict, big_salary=False):

    def file_writer(name, salary):
        with open('salary.txt', 'a', encoding='utf-8') as file:
            file.writelines(sting_template.format(name, salary))

    BIG_SALARY = 500000
    sting_template = '{} - {}\n'
    if os.path.exists('salary.txt'):
        os.remove('salary.txt')
    for name, salary in salary_dict.items():
        if big_salary:
            file_writer(name, salary)
        else:
            if salary < BIG_SALARY:
                file_writer(name, salary)


def make_net_salary_list():
    with open('salary.txt', encoding='utf-8') as file:
        for line in file:
            line_list = line.strip().split(' - ')
            print(f'{line_list[0].upper()} - {int(int(line_list[1])*0.87)}')


print('Задание 1:')
names_list = ('Вася', 'Иван', 'Сергей', 'Надежда', 'Александр', 'Дмитрий', 'Анастасия', 'Владимир', 'Семен', 'Ваган')
salary_list = (5000, 10000, 20000, 50000, 100000, 150000, 200000, 300000, 500000, 600000)
print('а) Проверяем словарь с зарплатами:')
print(make_salary_dict(names_list, salary_list))
print('б) Делаем полный файл salary.txt:')
salary_dict = make_salary_dict(names_list, salary_list)
make_salary_txt(salary_dict, big_salary=True)
with open('salary.txt', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
print('в) Делаем файл salary.txt с малыми зарплатами:')
salary_dict = make_salary_dict(names_list, salary_list)
make_salary_txt(salary_dict)
with open('salary.txt', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
print('г) Финальный вывод файла с учетом налогов:')
make_net_salary_list()
