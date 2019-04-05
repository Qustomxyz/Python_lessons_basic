# Эти задачи необходимо решить используя регулярные выражения!

import re

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.


check_name = re.compile(r'[А-ЯA-Z]')
check_mail = re.compile(r'[a-z_0-9]+@[a-z0-9]+\.(?:ru|org|com)')


def check_inputs(first_name, last_name, mail):
    if not check_name.match(first_name):
        print('Неверно указано имя. Имя должно начинаться с большой буквы')
    if not check_name.match(last_name):
        print('Неверно указана фамилия. Фамилия должна начинаться с большой буквы')
    if not check_mail.match(mail):
        print('Неверно указано e-mail')


print('Задание 1')
first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
mail = input('Введите e-mail: ')
check_inputs(first_name, last_name, mail)
print('')


# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!


dot_plus = re.compile(r'\.\.+')

print('Задание 2: ')
if dot_plus.search(some_str):
    print('В тексте встречается подряд более одной точки.')
else:
    print('В тексте не встречается подряд более одной точки.')
