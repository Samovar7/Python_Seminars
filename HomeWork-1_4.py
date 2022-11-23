'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в
числе. Для решения используйте цикл while и арифметические операции.
'''
num = int(input('Введите целое положительное число: '))
n = num
max_number = 0
while n > 0:
    number = n % 10
    n = n // 10
    if number > max_number:
        max_number = number
print(f'В числе {num} наибольшая цифра: {max_number}')
