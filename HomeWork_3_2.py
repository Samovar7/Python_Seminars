'''
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой.
'''


def User_data(first_name=input('Введите свое имя: '),
              last_name=input('Введите свою фамилию: '),
              year_of_born=input('Введите свой год рождения: '),
              live_town=input('Укажите город проживания: '),
              email=input('Укажите свой e-mail: '),
              phone=input('Укажите свой контактный телефон: ')):
    return f'Данные пользователя {first_name} {last_name}: дата рождения: {year_of_born}; город проживания: {live_town}; e-mail: {email}; Контактный номер телефона: {phone}'


print(User_data())
