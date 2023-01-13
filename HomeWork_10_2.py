
"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Создать класс
Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ. Создать метакласс.
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


class WageControl:
    """Дескриптор для атрибута wage.
    Контроль отрицательного значения и типа данных."""

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if isinstance(value, str):
            raise TypeError("Значение не может быть строкой")
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value


class BonusControl:
    """Дескриптор для атрибута bonus.
    Контроль отрицательного значения, размера премии и типа данных"""

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if isinstance(value, str):
            raise  TypeError("Значение не может быть строкой")
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        if value > instance.wage:
            raise   ValueError("В нашей компании премия не может быть больше "
                               "100% от заработной платы сотрудника.")
        instance.__dict__[self.my_attr] = value


class Woker(metaclass=WokerMetaClass):
    """Создаем базовый класс Woker, для учета работников компании.
    При вызове указываем только Имя, Фамилию и должность.
    Зарплату и Премию устанавливаем в клиентском коде"""

    wage = WageControl('wage')
    bonus = BonusControl('bonus')

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Woker):
    """Класс на базе Родительского Woker.
    Вычисляет общий доход сотрудника."""

    def get_full_name(self):
        """Вычисляем полное имя"""
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income (self):
        """Считаем общий доход за месяц: зп+бонус"""
        
        total_income = self.wage + self.bonus
        return total_income

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def total_income(self):
        return self.get_total_income()


ivanov = Position("Сергей", "Иванов", "Слесарь", 20000.00, 5000.00)
print(f"Доход сотрудника {ivanov.full_name} в текущем месяце составляет:"
      f" {ivanov.total_income} руб.")
ivanov.wage = 20000.00
ivanov.bonus = 15000.00
print(f"Доход сотрудника {ivanov.full_name} в текущем месяце составляет: "
      f"{ivanov.total_income} руб.")
petrov = Position("Петр", "Петров", "Сантехник", 25000.00, 17000.00)
print(f"Доход сотрудника {petrov.full_name} в текущем месяце составляет: "
      f"{petrov.total_income} руб.")
