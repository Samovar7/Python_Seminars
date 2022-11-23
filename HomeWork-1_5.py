'''
Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма (прибыль — выручка больше
издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
'''
revenue = float(input('Введите выручку компании за период: '))
costs = float(input('Введите издержки компании за период: '))
profit = round(revenue - costs, 2)
if profit < 0:
    print(f'Компания отработала в убыток, размер убытка = {profit} руб.')
elif profit == 0:
    print(f'Компания отработала с нулевой прибылью!')
else:
    print(f'Компания отработала с прибылью = {profit} руб.')
    staff = int(input('Введите количество сотрудников в компании: '))
    print(f'Прибыль компании в расчете на одного сотрудника составляет: {round(profit/staff, 2)} руб./чел.')