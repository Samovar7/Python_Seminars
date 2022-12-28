'''
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться
'''

from timeit import timeit
import math
from HomeWork_3_4 import negative_pow, negative_pow2, num, pow



def testing_time_execute ():
    """Проверка скорости выполнения функций возведения в отрицательную степень.

    Сравниваются три функции: 
    1 - negative_pow, считает через умножение и однократное деление с использованием цикла
    2 - negative_pow2, считает через деление  в цикле
    3 - math.pow(), встроенная функция библиотеки math
    :note Тестирование показало что операция умножения делается быстрее чем операция деления,
    а встроенная функция исполняется более чем в 2 раза быстрее.
    Вывод: максимально использовать встроенные функции и библиотеки, не выдумывать велосипед заново.
    """
    print(timeit("negative_pow(num, pow)", globals=globals()))
    print(timeit("negative_pow2(num, pow)", globals=globals()))
    print(timeit("math.pow(num, pow)", globals=globals()))




testing_time_execute()
print(testing_time_execute.__doc__)