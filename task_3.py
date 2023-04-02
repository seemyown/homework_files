file_path_1 ='1.txt'
string_num = 0
with open(file_path_1, 'r', encoding='UTF-8') as file:
    counter_f1 = 0
    strings1 = []
    file_num1 = 1
    for i in file.readlines():
        string_num += 1
        strings1.append(f'Строка номер {string_num} файл номер {file_num1}')
        counter_f1 += 1
    # print(strings1)
string1 = '\n'.join(strings1)

file_path_2 = '2.txt'
string_num = 0    
with open(file_path_2, 'r', encoding='UTF-8') as file:
    strings2 = []
    file_num2 = 2
    counter_f2 = 0
    for i in file.readlines():
        counter_f2 += 1
        string_num += 1
        strings2.append(f'Строка номер {string_num} файл номер {file_num2}')
string2 = ' '.join(strings2)
file_path_3 = '3.txt'
string_num = 0
with open(file_path_3, 'r', encoding='UTF-8') as file:
    strings3 = []
    file_num3 = 3
    counter_f3 = 0
    for i in file.readlines():
        counter_f3 += 1
        string_num += 1
        strings3.append(f'Строка номер {string_num} файл номер {file_num3}')
string3 = '\n'.join(strings3)

minimum = min(counter_f1, counter_f2, counter_f3)
maximum = max(counter_f1, counter_f2, counter_f3)

with open ('itog.txt', 'w', encoding='UTF-8') as file:
    if counter_f1 == minimum:
        file.write(f'{file_path_1}\n{counter_f1}\n{string1}\n')
    elif counter_f2 == minimum:
        file.write(f'{file_path_2}\n{counter_f2}\n{string2}\n')
    elif counter_f3 == minimum:
        file.write(f'{file_path_3}\n{counter_f3}\n{string3}\n')

with open('itog.txt', 'a', encoding='UTF-8') as file:
    if (counter_f1 != minimum) and (counter_f1 != maximum):
        file.write(f'{file_path_1}\n{counter_f1}\n{string1}\n')
    elif (counter_f2 != minimum) and (counter_f2 != maximum):
        file.write(f'{file_path_2}\n{counter_f2}\n{string2}\n')
    elif (counter_f3 != minimum) and (counter_f3 != maximum):
        file.write(f'{file_path_3}\n{counter_f3}\n{string3}\n')

with open('itog.txt', 'a', encoding='UTF-8') as file:
    if counter_f1 == maximum:
        file.write(f'{file_path_1}\n{counter_f1}\n{string1}\n')
    elif counter_f2 == maximum:
        file.write(f'{file_path_2}\n{counter_f2}\n{string2}\n')
    elif counter_f3 == maximum:
        file.write(f'{file_path_3}\n{counter_f3}\n{string3}\n')