# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random

"""
Иван, давайте не буду наследоваться от Person, мы же знаем, что я умею это делать, но в данной задаче
обе сущности практически не отличаются друг от друга и делать для каждого новый класс не поднимается рука :)

Подсчет урона у меня имеет внешний фактор, т.е. по логике игры зависит от атакующего минус амортизация брони.
Поэтому не стал инкапсулировать этот метод. Но, если чего, то сделал бы так: def _take_damage ....
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(100, 1000)
        self.damage = random.randint(30, 300)
        self.armor = round(1 + random.random(), 2)

    def take_damage(self, damage_from_enemy):
        self.health -= int(damage_from_enemy/self.armor)

    def attack(self, enemy):
        enemy.take_damage(self.damage)

    def __str__(self):
        return f'Name: {self.name}\nHealth: {self.health}\nDamage power: {self.damage}\nArmor resistance: {self.armor}\n'


class Game:
    def __init__(self):
        self.player1 = input('Введите имя первого игрока: ')
        self.player2 = input('Введите имя второго игрока: ')

        self.player1 = Player(self.player1) if self.player1 else Player('Player')
        self.player2 = Player(self.player2) if self.player2 else Player('Enemy')

    def game_over(winner):
        print('GAME OVER!')
        print(f'Победу одержал {winner.name}!')

    def start(self):
        print('\nПредставляем бойцов на ринге!\n')
        print('В красном углу:')
        print(self.player1, '')
        print('В синем углу:')
        print(self.player2, '')
        if random.choice((1, 2)) == 1:
            first_attacker = self.player1
            second_attacker = self.player2
        else:
            first_attacker = self.player2
            second_attacker = self.player1
        print(f'Первым нападает {first_attacker.name}!')

        def health_update(player):
            return player.health if player.health > 0 else 0

        while True:
            print('BooM!!')
            first_attacker.attack(second_attacker)
            print(f'Противнику нанесен урон {first_attacker.damage}')
            print(f'Здоровье {second_attacker.name} теперь {health_update(second_attacker)} ...')
            if second_attacker.health < 0:
                Game.game_over(first_attacker)
                break
            print('Ответный удар!')
            print('BaaaM!')
            print(f'Противнику нанесен урон {second_attacker.damage}')
            print(f'Здоровье {first_attacker.name} теперь {health_update(first_attacker)} ...')
            if first_attacker.health < 0:
                Game.game_over(second_attacker)
                break


go_game = Game()
go_game.start()
