'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def Summ_2max_number(num1, num2, num3):
    if num1 >= num3 and num2 >= num3:
        result = num1 + num2
    elif num1 >= num2 and num3 >= num2:
        result = num1 + num3
    else:
        result = num2 + num3
    return result

num1 = int(input('Введите 1-е число: '))
num2 = int(input('Введите 2-е число: '))
num3 = int(input('Введите 3-е число: '))
print(f'Сумма наибольших двух элементов равна {Summ_2max_number(num1, num2, num3)}')
