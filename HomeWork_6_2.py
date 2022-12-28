
"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться
"""

from memory_profiler import  profile
from random import randint, randrange, uniform
from functools import reduce

@profile
def list1():
    '''Формирование списка через цикл
    '''
    lst_new = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            lst_new.append(lst[i])
    print(lst_new)

# Вариант с LC
@profile
def list2():
    '''Формирование списка через LC'''
    list_new_2 = [lst[el] for el in range(1, len(lst)) if lst[el] > lst[el - 1]]
    print(list_new_2)


@profile
def list3():
    """Функция формирования списка четных чисел в диапазоне от 100 до 1000 и
    подсчет произведения всех элементов списка

    Проверяем использование памяти при использовании лямбда функции и генератора
    списка
    """
    print(reduce((lambda x, y: x * y),
             (el for el in range(100, 1001) if el % 2 == 0)))

@profile
def list4():
    """Функция формирования списка четных чисел в диапазоне от 100 до 1000 и
        подсчет произведения всех элементов списка

        Проверяем использование памяти при использовании стандартного списка и
        умножения через цикл.
        """
    list_multi = [el for el in range(100, 1001) if el % 2 == 0]
    multiplication = 1
    for el in list_multi:
        multiplication*=el
    print(multiplication)
n = 100
lst = [randrange(100) for el in range(n)]
print(lst)
list1()
list2()
list3()
list4()