# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:
    """
    Класс по производству игрушек
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self._buy_materials()

    def _buy_materials(self):
        """
        Закупает материалы
        """
        print(f'Закупаем материал для производства {self.name}')
        self._colorise_toy()

    def _colorise_toy(self):
        """
        Красит ткань
        """
        print(f'Красим ткань в {self.color} цвет')
        self._make_toy()

    def _make_toy(self):
        """
        Пошив игрушки
        """
        print(f'Шьем {self.name} на нашей производственной базе')
        print('*'*15)
        print('')

    def __str__(self):
        return f'Привет, я {self.name}. Мой цвет {self.color}. Приятно познакомиться!'


class AnimalToy(Toy):
    """
    Производство игрушек типа 'Животное'
    """
    serial_number = 0

    def __init__(self, name, color, toy_type):
        super().__init__(name, color)
        self.type = toy_type
        AnimalToy.serial_number += 1
        self.serial = AnimalToy.serial_number


class CartoonToy(Toy):
    """
    Производство игрушек типа 'Персонаж мультфильма'
    """
    serial_number = 0

    def __init__(self, name, color, toy_type):
        super().__init__(name, color)
        self.type = toy_type
        CartoonToy.serial_number += 1
        self.serial = CartoonToy.serial_number


class ToysFactory:
    """
    Фабрика игрушек типов: 'Животное', 'Персонаж мультфильма'
    """
    def __init__(self):
        self.toys_order = dict()
        self.make_toy()

        if len(self.toys_order) > 0:
            for item, value in self.toys_order.items():
                print(f'\nМы сделали для Вас следующие игрушки типа "{item}". Они сами расскажут о себе')
                for toy in value:
                    print(toy.serial, toy)
            print('\nЕсли хотите забрать игрушки к себе на склад, вызовите метод .get_toys()\n')

    def get_toys(self):
        """
        Передает созданные объекты
        :return:
        dict('Животное': массив созданных объектов, 'Персонаж мультфильма': массив созданных объектов)
        """
        return self.toys_order

    def stop(stop=0):
        """
        Делает сообщение об остановке производства.
        stop=0 штатный режим остановки
        stop=1 аварийный режим остановки
        :return: сообщение об остановке производства (type str)
        """
        message = ''
        if stop:
            message += '\nСожалею, этого нет в нашей производственной линейке.\n'
        message += 'Производство остановлено\n'
        return message

    def make_toy(self):
        """
        Функция управления производственным циклом в режиме диалога с заказчиком
        """
        print('Привет. Это фабрика игрушек.')

        while True:
            if len(self.toys_order) > 0:
                print('Какой ещё тип игрушки хотите сделать?')
            else:
                print('Какой тип игрушки хотите сделать?')
            print(
                """
                1. Животное\n
                2. Персонаж мультфильма\n
                3. Остановить производство
                """
            )
            self.toy_type = input('Введите номер из списка: ')
            try:
                if int(self.toy_type) in (1, 2):
                    print(f'Ваш выбор: {self.toy_type}')
                    self.toy_name = input(f'Какое у игрушки будет имя?: ')
                    self.toy_color = input(f'Какой у игрушки будет цвет?: ')
                    if self.toy_type == '1':
                        if self.toys_order.get('Животное', 0):
                            the_toy = AnimalToy(self.toy_name, self.toy_color, 'Животное')
                            self.toys_order[the_toy.type].append(the_toy)
                        else:
                            the_toy = AnimalToy(self.toy_name, self.toy_color, 'Животное')
                            self.toys_order[the_toy.type] = [the_toy]
                    elif self.toy_type == '2':
                        if self.toys_order.get('Персонаж мультфильма', 0):
                            the_toy = CartoonToy(self.toy_name, self.toy_color, 'Персонаж мультфильма')
                            self.toys_order[the_toy.type].append(the_toy)
                        else:
                            the_toy = CartoonToy(self.toy_name, self.toy_color, 'Персонаж мультфильма')
                            self.toys_order[the_toy.type] = [the_toy]
                elif self.toy_type == '3':
                    print(ToysFactory.stop())
                    break
                else:
                    print(ToysFactory.stop(1))
                    break
            except ValueError:
                print(ToysFactory.stop(1))
                break


if __name__ == '__main__':
    my_toys = ToysFactory()  # запускаем интерактивную фабрику игрушек
    my_warehouse = my_toys.get_toys()  # забираем объекты с фабрики

    if my_warehouse:  # показываем игрушки на нашем складе
        print('Увезли на наш склад:')
        for key, item_list in my_warehouse.items():
            print(f'### Тип {key} ###')
            for item in item_list:
                print(f'серийный номер: {item.serial} название: "{item.name}" цвет: "{item.color}"')
