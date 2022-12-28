'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

my_file = open("task_5_4.txt", "r", encoding='utf-8')
content = my_file.readlines()
my_file.close()
print(content)
i = -1
for str in content:
    i += 1
    if str.find('One') != -1:
        content[i] = str.replace('One', 'Один')
        continue
    elif str.find('Two') != -1:
        content[i] = str.replace('Two', 'Два')
        continue
    elif str.find('Three') != -1:
        content[i] = str.replace('Three', 'Три')
        continue
    elif str.find('Four') != -1:
        content[i] = str.replace('Four', 'Четыре')
        continue
print(content)
my_file = open("task_5_4_ru.txt", "w", encoding='utf-8')
my_file.writelines(content)
my_file.close()
