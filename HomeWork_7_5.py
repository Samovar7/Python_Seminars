"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationary():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print("Запуск записи")


class Pencil(Stationary):
    def draw(self):
        print("Запуск чертежа")


class Handle(Stationary):
    def draw(self):
        print("Запуск выделения")


Pen = Pen("Ручка")
Pencil = Pencil("Карандаш")
Handle = Handle("Маркер")
print(f"{Pen.title}:", end=" ")
Pen.draw()
print(f"{Pencil.title}:", end=" ")
Pencil.draw()
print(f"{Handle.title}:", end=" ")
Handle.draw()

