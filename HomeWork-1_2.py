'''
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''
time_sec = int(input('Введите время в секундах:'))
time_hour = time_sec // 3600
time_minute = (time_sec % 3600) // 60
sec = time_sec % 60
if time_hour < 10 :
    time_hour = str(f'0{time_hour}')
if time_minute < 10 :
    time_minute = str(f'0{time_minute}')
if sec < 10 :
    sec = str(f'0{sec}')
print(f'Время введенное в секундах {time_sec} составляет {time_hour}:{time_minute}:{sec}')
