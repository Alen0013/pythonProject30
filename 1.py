from abc import ABC, abstractmethod

class House:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)


class Builder(ABC):
    @abstractmethod
    def prepare_floor(self):
        pass

    @abstractmethod
    def lay_tiles(self):
        pass

    @abstractmethod
    def apply_putty(self):
        pass

    @abstractmethod
    def plaster_walls(self):
        pass

    @abstractmethod
    def prime_walls(self):
        pass

    @abstractmethod
    def paint_walls(self):
        pass


class Tiler(Builder):
    def __init__(self):
        self.house = House()

    def prepare_floor(self):
        self.house.add_part("Подготовка пола")

    def lay_tiles(self):
        self.house.add_part("Укладка плитки")

    def apply_putty(self):
        pass

    def plaster_walls(self):
        pass

    def prime_walls(self):
        pass

    def paint_walls(self):
        pass

    def get_result(self):
        return self.house

class Finisher(Builder):
    def __init__(self):
        self.house = House()

    def prepare_floor(self):
        pass

    def lay_tiles(self):
        pass

    def apply_putty(self):
        self.house.add_part("Нанесение шпаклевки")

    def plaster_walls(self):
        self.house.add_part("Оштукатуривание стен")

    def prime_walls(self):
        pass

    def paint_walls(self):
        pass

    def get_result(self):
        return self.house

# Конкретный строитель - Маляр
class Painter(Builder):
    def __init__(self):
        self.house = House()

    def prepare_floor(self):
        pass

    def lay_tiles(self):
        pass

    def apply_putty(self):
        pass

    def plaster_walls(self):
        pass

    def prime_walls(self):
        self.house.add_part("Грунтовка стен")

    def paint_walls(self):
        self.house.add_part("Покраска стен")

    def get_result(self):
        return self.house

# Директор - Прораб
class Foreman:
    def __init__(self, builder):
        self.builder = builder

    def make_floors(self):
        self.builder.prepare_floor()
        self.builder.lay_tiles()

    def level_walls(self):
        self.builder.apply_putty()
        self.builder.plaster_walls()

    def paint_walls(self):
        self.builder.prime_walls()
        self.builder.paint_walls()

    def turnkey_work(self):
        self.make_floors()
        self.level_walls()
        self.paint_walls()

# Клиентский код
if __name__ == "__main__":
    # Создаем строителей
    tiler = Tiler()
    finisher = Finisher()
    painter = Painter()

    # Прораб управляет плиточником
    foreman = Foreman(tiler)
    foreman.make_floors()
    print("Плиточник сделал: ", tiler.get_result().list_parts())

    # Прораб управляет отделочником
    foreman = Foreman(finisher)
    foreman.level_walls()
    print("Отделочник сделал: ", finisher.get_result().list_parts())

    # Прораб управляет маляром
    foreman = Foreman(painter)
    foreman.paint_walls()
    print("Маляр сделал: ", painter.get_result().list_parts())

    # Прораб делает все работы под ключ
    foreman = Foreman(tiler)
    foreman.turnkey_work()
    print("Работы под ключ: ", tiler.get_result().list_parts())