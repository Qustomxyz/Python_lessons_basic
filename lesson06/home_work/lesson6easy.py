# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, max_speed, color, name, is_police=0):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Внимание, еду')

    def stop(self):
        print('Торможу!')

    def turn(self, direction):
        self.direction = direction
        print(f'Поворачиваю {direction}')

    def __str__(self):
        self.answer = ''
        for item, value in self.__dict__.items():
            if item != 'answer':
                self.answer += f'{item}: {value}\n'
        return self.answer


class TownCar(Car):
    def __init__(self, max_speed, color, name, is_police=0):
        super().__init__(max_speed, color, name, is_police)
        self.gear = 'automatic'
        self.seats_number = 5


class SportCar(Car):
    def __init__(self, max_speed, color, name, is_police=0):
        super().__init__(max_speed, color, name, is_police)
        self.seats_number = 2


class WorkCar(Car):
    def __init__(self, max_speed, color, name, is_police=0):
        super().__init__(max_speed, color, name, is_police)
        self.seats_number = 2
        self.load_capacity = 1500


porche = SportCar(300, 'red', '911')
citroen = WorkCar(150, 'white', 'Jumpy')
bmw = TownCar(220, 'blue', '320')
mercedes_police = TownCar(250, 'white', '300', is_police=1)


print(porche)
citroen.turn('налево')
bmw.go()
mercedes_police.stop()
print(mercedes_police.is_police)
