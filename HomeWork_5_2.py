'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

my_file = open("task_5_2.txt", "r", encoding='utf-8')
content = my_file.readlines()
print('Файл содержит ', len(content), ' строк.')
my_file.close()
my_file = open("task_5_2.txt", "r", encoding='utf-8')
count = 0
for line in my_file:
    count += 1
    sum = 0
    for i in line.split():
        sum += 1
    print(f"Строка {count} содержит {sum} слов. ")
my_file.close()
