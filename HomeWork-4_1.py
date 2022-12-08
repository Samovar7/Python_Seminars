'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

script_name, employee_name, hours, hourly_rate, bonus = argv  # передаются аргументы: имя файла, ФИО сотрудника, отработанные часы в месяц, часовая ставка, премия в виде процентов числом от 0 до 100

salary_calculation = float(hours) * float(hourly_rate)
salary_calculation = salary_calculation + salary_calculation / 100 * float(bonus)
print(
    f'Заработная плата сотрудника {employee_name} составляет: {salary_calculation} руб.')

print("Отработано часов:", hours)
print("Часовая ставка:  ", hourly_rate)
print("Премия в %:      ", bonus)