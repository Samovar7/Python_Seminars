"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road():
    """

    """
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_road(self):
        """

        :return:
        """
        massa = self._length * self._width * 25 * 5 / 1000
        print(
            f"Для укладки дороги длиной {self._length} м и шириной {self._width} м, необходимо асфальта {massa} т.")


road1 = Road(10000, 20)
road1.mass_road()
