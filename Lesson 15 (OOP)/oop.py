# Класс - шаблон для создание объекта
# Объект - экземпляр класса
# Атрибут - данные пренадлежащие объекту и его состояние (цвет велосипеда, скорость автомобиля)
# Метод - функция внутри класса (увеличить/уменьшить громкость)
# self - специальный объект на получение объекта экземпляра класса

# public private protected ?

# Класс и объект в python
class UAZHunter:
    max_speed = 12
    color = 'Khaki'

    # Волшебный класс, self - ссылка на этот объект, сможем обращаться к любому метода этого объекта через self ?
    # . - обращение к членам класса
    def __init__(self):
        self.current_speed = 0

    def accelerate(self):
        self.current_speed += min(self.current_speed + 10, self.max_speed)


my_car = UAZHunter()
print(my_car.current_speed)
my_car.accelerate()
print(my_car.current_speed)


# OOP Парадигмы
# наследование - создать новый класс на основе существующего, може что-то изменить добавить, обновить


class Vehicle:
    def __init__(self):
        self.horn = "beeeep"
        self.engine = "zoomzoom"

    def start_engine(self):
        print(self.engine)


# class Car(Vehicle, Boat): -  множественное наследование
class Car(Vehicle):
    def make_some_noise(self):
        self.start_engine()
        print(self.horn)


my_car = Car()
my_car.make_some_noise()


class Car2:
    max_speed = 100

    def __init__(self):
        self.current_speed = 0

    def accelerate(self):
        self.current_speed += 10
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed


class Convertible(Car2):
    def __init__(self):
        # super().__init__() - унаследовать init от родителя
        super().__init__()
        self.is_roof_closed = True

    def change_roof_state(self):
        self.is_roof_closed = not self.is_roof_closed


c = Convertible()
print(c.is_roof_closed)

c.change_roof_state()
print(c.is_roof_closed)

c.accelerate()


# инапсуляция - сокрытие функционала или данных с представлением только входа и выхода
# public protected private


# полиморфизм

class Car3:
    def honk(self):
        print("beep")


class Truck(Car3):
    def honk(self):
        print('beep')


class Ship:
    def honk(self):
        print("hoooooonk")


transports = [Car3(), Truck(), Ship()]
for t in transports:
    t.honk()


# Абстракция - абстракция не должна зависеть от конкретики
# предварительное описание интерфейса без реализации

