'''Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

my_file = open("task-5_3.txt", "r", encoding='utf-8')
sum = 0
count = 0
for line in my_file:
    count += 1
    for i in line.split():
        try:
            temp = float(i)
            sum = sum + float(i)
        except:
            sum = sum + 0
            temp = 0
    if temp > 0 and temp < 20000.0:
        print(line, end="")
print()
print(f'Средняя величина дохода сотрудников равна = {round(sum / count, 2)}')
my_file.close()
