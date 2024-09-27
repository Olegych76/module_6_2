class Vehicle:
    # цвета, доступные для покраски:
    __COLOR_VARIANTS = ['голубой виталик', 'оранжевое небо', 'трава у дома', 'квадрат малевича', 'парное молоко']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan("Некто Иванов", 'Приора на подрезанных пружинах', "голубой виталик", 250)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('малиновый рассвет')
vehicle1.set_color('квадрат Малевича')
vehicle1.owner = 'Виталик'

# Проверяем что поменялось
vehicle1.print_info()
