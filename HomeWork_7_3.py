"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Woker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": None, "bonus": None}


class Position(Woker):
    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income (self):
        total_income = self._income["wage"] + self._income["bonus"]
        return total_income

Ivanov = Position("Сергей", "Иванов", "Слесарь")
Ivanov._income["wage"] = 25000.00
Ivanov._income["bonus"] = 5000.00
print(f"Доход сотрудника {Ivanov.get_full_name()} в текущем месяце составляет: {Ivanov.get_total_income()} руб.")


