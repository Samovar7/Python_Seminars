'''
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
'''

my_file = open("task-1.txt", "w")
my_file.write(input("Введите числа через пробел: "))
my_file.close()
my_file = open("task-1.txt", "r")
sum = 0
for line in my_file:
    for i in line.split():
        try:
            sum = sum + float(i)
        except:
            sum = sum + 0
print(f'Сумма чисел введенных вами равна = {round(sum, 2)}')
my_file.close()
