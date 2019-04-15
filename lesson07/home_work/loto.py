#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import re


class Lotto:
    def __init__(self):
        self.step = 90
        self.card_1 = self.make_player_card(player='player')
        self.card_2 = self.make_player_card()
        empty_pattern = re.compile(r'^\D+$')
        human_winner_message = 'Стоп игра!\nПобеду одержал Человек!'
        computer_winner_message = 'Стоп игра!\nПобеду одержал Компьютер!'
        tie_message = 'Стоп игра!\nУникальный случай!!!\n!!!НИЧЬЯ!!!\n'

        for keg in self.take_keg():
            self.step -= 1
            print(f'Новый бочонок: {keg} (осталось {self.step})')
            print(self.card_1)
            print(self.card_2)
            player_answer = input('Зачеркнуть цифру? (y/n): ')
            if player_answer in ('y', 'yes', 'да', 'д'):
                if self.check_answer('yes', keg):
                    if empty_pattern.search(self.card_1) and empty_pattern.search(self.card_2):
                        print(tie_message)
                        break
                    elif empty_pattern.search(self.card_1):
                        print(human_winner_message)
                        break
                    elif empty_pattern.search(self.card_2):
                        print(computer_winner_message)
                        break
                else:
                    print(computer_winner_message)
                    break
            else:
                if not self.check_answer('no', keg):
                    print(computer_winner_message)
                    break
        else:
            print('Game over!')

    def check_answer(self, answer, keg):
        for_search = re.compile(r'\b' + f'{keg}' + r'\b')
        repl_pattern = ' -' if len(str(keg)) == 2 else '-'
        if answer == 'yes':
            if for_search.search(self.card_1):
                self.card_1 = for_search.sub(repl_pattern, self.card_1)
                self.card_2 = for_search.sub(repl_pattern, self.card_2)
                return True
            else:
                return False
        else:
            if for_search.search(self.card_1):
                return False
            else:
                self.card_2 = for_search.sub(repl_pattern, self.card_2)
                return True

    @staticmethod
    def take_keg():
        lotto_kegs = list(range(1, 91))
        random.shuffle(lotto_kegs)
        for keg in lotto_kegs:
            yield keg

    @staticmethod
    def make_player_card(player='computer'):
        card_numbers = '------ Ваша карточка -----\n' if player == 'player' else '-- Карточка компьютера ---\n'
        numbers = random.sample(range(1, 91), 15)
        slice_start = 0
        for i in range(3):
            slice_stop = slice_start + 5
            numbers_for_line = numbers[slice_start:slice_stop]
            slice_start += 5
            spaces = random.sample(range(9), 4)
            numbers_for_line.sort(reverse=True)
            for j in range(9):
                if j in spaces:
                    card_numbers += '   '
                else:
                    number = str(numbers_for_line.pop())
                    number = number if len(number) == 2 else ' ' + number
                    card_numbers += number + ' '
            else:
                card_numbers += '\n'
        card_numbers += '--------------------------\n'
        return card_numbers


if __name__ == '__main__':
    game_start = Lotto()
