
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
class WokerMetaClass(type):

    def __init__(self, clsname, bases, clsdict):
        """Контроль за наличием в созданных классах Docstrings"""
        for key, value in clsdict.items():
            if key.startswith("__"):
                continue
            if not hasattr(value, "__call__"):
                continue
            if not getattr(value, "__doc__"):
                raise TypeError(f"Метод {key} должен иметь строку документации")
        type.__init__(self, clsname, bases, clsdict)


class Critical_err(Exception):
    """Отлавливаем ошибки критичные для дальнейших расчетов или которые
    противоречат основной концепции.
    код ошибки 5 указывает на критическую ошибку и прерывает выполнение
    программы"""

    def __init__(self, txt):
        self.txt = txt
        print(self.txt)
        exit(5)

class Woker(metaclass=WokerMetaClass):
    """Создаем базовый класс Woker, для учета работников компании.
    При вызове указываем только Имя, Фамилию и должность.
    Зарплату и Премию устанавливаем в клиентском коде"""
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": None, "bonus": None}

    @property
    def wage(self):
        return self._income["wage"]

    @property
    def bonus(self):
        return self._income["bonus"]

    @wage.setter
    def wage(self, value):
        """Сеттер.
        Проверяем что Зарпалта больше 0"""
        if value < 0:
            raise  Critical_err("Зарплата должна быть больше нуля")
        self._income["wage"] = value

    @bonus.setter
    def bonus(self, value):
        """Сеттер
        Контролируем основные параметры премии"""
        if value < 0:
            raise Critical_err("Премия должна быть больше нуля")
        if self.wage is None:
            raise Critical_err("Задайте сначала зарплату сотрудника")
        if value > self.wage:
            raise   Critical_err("В нашей компании премия не может быть больше 100% от заработной платы сотрудника.")
        self._income["bonus"] = value


class Position(Woker):
    """Класс на базе Родительского Woker.
    Вычисляет общий доход сотрудника."""
    def get_full_name(self):
        """Вычисляем полное имя"""
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income (self):
        #"""Считаем общий доход за месяц: зп+бонус"""
        total_income = self.wage + self.bonus
        return total_income

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def total_income(self):
        return self.get_total_income()

Ivanov = Position("Сергей", "Иванов", "Слесарь")
Ivanov.wage = 20000.00
Ivanov.bonus = 5000.00
print(f"Доход сотрудника {Ivanov.full_name} в текущем месяце составляет: {Ivanov.total_income} руб.")