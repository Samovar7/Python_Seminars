'''
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
from random import randint, randrange, uniform
n = 20

lst = [randrange(100) for el in range(n)]
print(lst)
lst_new = []
for i in range(1,len(lst)):
    if lst[i] > lst[i-1]:
        lst_new.append(lst[i])
print(lst_new)

  
# Вариант с LC
list_new_2 = [lst[el] for el in range(1, len(lst)) if lst[el] > lst[el-1]]
print(list_new_2)