'''
Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
'''


list_user = []
list_user = [int(ele) for ele in (input("Введите целые числа через пробел:").split())]
print(list_user)
end_list = len(list_user)
if end_list%2 != 0: end_list-=1
for ele in range(1, end_list, 2):
    tmp = list_user[ele-1]
    list_user[ele-1] = list_user[ele]
    list_user[ele] = tmp
print(list_user)



