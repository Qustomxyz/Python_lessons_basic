# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import json


class Rival:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 50


player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
player = Rival(player1)
enemy = Rival(player2)


def attack(person1, person2):
    person2.health -= person1.damage
    return person2.health


print(f'{player.name} атакует!')
attack(player, enemy)
print(f'Теперь здоровье {enemy.name} стало - {enemy.health}')


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

class Rival2(Rival):
    armor = 1.2


def make_armor_amortization(damage, armor):
    return int(damage/armor)


def attack2(person1, person2):
    damage_it = make_armor_amortization(person1.damage, person2.armor)
    person2.health -= damage_it
    return person2.health


player = Rival2(player1)
enemy = Rival2(player2)
print(f'{enemy.name} атакует!')
attack2(enemy, player)
print(f'Теперь здоровье {player.name} стало - {player.health}')

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


class Rival3(Rival2):
    def save_player(self):
        file = self.name + '.txt'
        json_object = {'name': self.name, 'health': self.health, 'damage': self.damage, 'armor': self.armor}
        with open(file, 'w') as f:
            json.dump(json_object, f)


player = Rival3(player1)
enemy = Rival3(player2)
player.save_player()
enemy.save_player()


def game_horror():

    def open_player(some_player):
        file = some_player.name + '.txt'
        with open(file) as f:
            player_dict = json.load(f)
        return player_dict

    def attack3(person1, person2):
        damage_it = make_armor_amortization(person1['damage'], person2['armor'])
        person2['health'] -= damage_it
        return person2['health']

    monster1 = open_player(player)
    monster2 = open_player(enemy)
    print('\n\nBIG GAME STARTS!!!\n\n')
    while True:
        result = attack3(monster1, monster2)
        if result < 0:
            name = monster1['name']
            health = monster1['health']
            print(f'Победил монстр {name}\nОстаток здоровья: {health}')
            break
        else:
            name1 = monster1['name']
            name2 = monster2['name']
            health = monster2['health']
            print(f'{name1} атакует!')
            print(f'Теперь здоровье {name2} стало - {health}')
            print('')
            monster1, monster2 = monster2, monster1


game_horror()
