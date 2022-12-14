"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    """Создание класса для сложения матриц и представления их в табличном виде"""

    def __init__(self):
        self.matrix = []

    def __str__(self):
        """Вывод на печать в табличном виде"""
        for lst in self.matrix:
            for el in lst:
                print(f"{el}   ", end="")
            print()
        return ""

    def __add__(self, other):
        """Метод сложения двух матриц"""
        M3 = Matrix()
        M3.matrix = list(map(list, self.matrix))
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                M3.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return M3


M1 = Matrix()
M2 = Matrix()
M1.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M2.matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
M3 = M1 + M2
print(M1)
print(M2)
print(M3)
