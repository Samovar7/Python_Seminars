'''
Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который результат
спортсмена составит не менее b километров. Программа должна принимать значения
параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

start = float(input('Введите результат пробежки в первый день в км.: '))
end = float(input('Введите конечную дистанцию в км.: '))
count_day = 2
next_day_result = start * 1.1
while next_day_result < end:
    count_day += 1
    next_day_result *= 1.1
print(
    f'На {count_day}-й день спортсмен достигнет результата не менее {round(end, 3)} км.')
