# Абстрактный класс Pasta (паста)
class Pasta:
    def __init__(self, type_: str, sauce: str, filling: str, add_ons: list):
        self.type = type_
        self.sauce = sauce
        self.filling = filling
        self.add_ons = add_ons

    def __str__(self):
        return f'{self.type} с соусом {self.sauce}, начинка: {self.filling}, добавки: {", ".join(self.add_ons)}'


# Конкретные реализации пасты
class Spaghetti(Pasta):
    def __init__(self, sauce: str, add_ons: list):
        super().__init__("Спагетти", sauce, "нет", add_ons)


class Penne(Pasta):
    def __init__(self, sauce: str, filling: str, add_ons: list):
        super().__init__("Пенне", sauce, filling, add_ons)


class Ravioli(Pasta):
    def __init__(self, sauce: str, filling: str, add_ons: list):
        super().__init__("Равиоли", sauce, filling, add_ons)


# Фабрика для создания пасты
class PastaFactory:
    @staticmethod
    def create_pasta(type_: str, sauce: str, filling=None, add_ons=None):
        if add_ons is None:
            add_ons = []

        if type_ == "Спагетти":
            return Spaghetti(sauce, add_ons)
        elif type_ == "Пенне":
            return Penne(sauce, filling, add_ons)
        elif type_ == "Равиоли":
            return Ravioli(sauce, filling, add_ons)
        else:
            raise ValueError("Неизвестный тип пасты")


# Пример использования
if __name__ == "__main__":
    pasta1 = PastaFactory.create_pasta("Спагетти", "Томатный", add_ons=["Пармезан", "Базилик"])
    pasta2 = PastaFactory.create_pasta("Пенне", "Сливочный", filling="Мясо", add_ons=["Укроп"])
    pasta3 = PastaFactory.create_pasta("Равиоли", "Альфредо", filling="Сыр", add_ons=["Петрушка"])

    print(pasta1)
    print(pasta2)
    print(pasta3)
