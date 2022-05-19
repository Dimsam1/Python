import pandas as pd
#import numpy as np
import os
import shutil

import sys
import json

##############################Задание 1########################################

#1. Создать программный файл в текстовом формате, записать в него построчно 
#данные, вводимые пользователем. Об окончании ввода данных будет 
#свидетельствовать пустая строка.

os.getcwd() #Это я для поиска "где я?" 
print(os.getcwd())
dir()
path = 'G:/IT/DIMAGB'

os.chdir(path)

os.getcwd()
print(os.getcwd())

def new_directory(directory):
    try:
        os.mkdir(directory)
    except:
        pass
        
# создать новую папку

directory = 'G:\\IT\\DIMAGB'

directory = os.path.join(os.getcwd(),'LES5')

new_directory(directory) 

# перейти в рабочую папку
os.chdir(directory)

print(os.getcwd())

with open(os.path.join(os.getcwd(), "task1.txt"), "w") as file1:
    vvod = str(input('Введите первую строку текста:'))
    print(vvod, file = file1)
    while len(vvod) > 0:
        vvod = str(input('Введите следующую строку текста:'))
        print(vvod, file = file1)
    else:
        print('Ввод закончен.')

############################Задание 2##########################################
os.listdir(os.getcwd())
#Out[39]: ['task1.txt', 'task2.txt']

#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, 
#выполнить подсчёт строк и слов в каждой строке.

with open("task2.txt", "r", encoding = 'utf-8') as file2:
    q_line = 0
    for line in file2:
        print(f'{line} Cлов: {len(line.split())}')
        q_line += 1
    print('Итого строк:', q_line)
#Out:
#Создать текстовый файл
# слов: 3
#не программно
# слов: 2
#сохранить в нём
# слов: 3
#несколько строк
# слов: 2
#выполнить подсчёт
# слов: 2
#строк и
# слов: 2
#слов в каждой строке и так далее и далее слов: 9
#Итого строк 7
    
#############################Задание 3#########################################
#3. Создать текстовый файл (не программно). Построчно записать фамилии 
#сотрудников и величину их окладов (не менее 10 строк). Определить, 
#кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
#Выполнить подсчёт средней величины дохода сотрудников.
os.listdir(os.getcwd())
#Out[70]: ['task1.txt', 'task2.txt', 'task3.txt']

#with open('файл в тек дир', 'способ открытия (r,w,a и т.д.)', encoding = 'utf-8') аs file_1
g={}
keys2 = ['Имя', 'Зарплата']
approx = 0
import mmap
import os

def get_num_lines():
    fp = open("task3.txt", "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines
#print(get_num_lines())
with open("task3.txt", "r", encoding = 'utf-8') as file3:
    N = int(get_num_lines())
    #print(N)
    #content = file3.read()
    #content.split()
    #print(content)      #При желании можно всех показать
    print('Зарплата меньше 20000:')
    for x in range(N):
        for line in file3:
            #print(len(line))
            g = dict(zip(keys2, line.split()))
            approx += int(g[keys2[1]])
                #print(g)
            if (int(g[keys2[1]]) < 20000):
                print(g[keys2[0]], g[keys2[1]])
        else:
            pass
    else:
        print('Средняя зарплата всех сотрудников:', int(approx) // N)

#############################Задание 4#########################################

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно 
#данные. При этом английские числительные должны заменяться на русские. 
#Новый блок строк должен записываться в новый текстовый файл.

from translate import Translator
# перейти в рабочую папку        
directory = 'G:\\IT\\DIMAGB\\LES5'

os.chdir(directory)

print(os.getcwd())

def get_num_lines():
    fp = open("task4.txt", "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines

def trans(line):
    tr = Translator(to_lang = "Russian")
    line[0] = tr.translate(line[0])
    return(line[0])

with open("task5.txt", "w", encoding = 'utf-8') as file5:
    
    with open("task4.txt", "r", encoding = 'utf-8') as file4:
        N1 = int(get_num_lines())
        
        for i in range(N1):
            
            for line in file4:
                line = line.split()
                #print(line, type(line))
                trans(line)
                new_line = ' '.join(line)
                print(new_line, file = file5)

#############################Задание 5#########################################

#5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
#разделённых пробелами. Программа должна подсчитывать сумму чисел в 
#файле и выводить её на экран.
import random as rnd

def str_to_int(x):
    if x.isdigit():
        return int(x)
    else:
        return(x)
# запись в файл
with open("task6.txt", "w", encoding = 'utf-8') as file6:
    my_List = [str(rnd.randint(0,100)) for e in range(12)]
    #print(type(my_List))
    #my_List1 = my_List.split()
    print(my_List)
    print(' '.join(my_List), file = file6)
# чтение данных из файла
with open("task6.txt", "r", encoding = 'utf-8') as file6:    
    content = file6.read().split()
    print(type(content))
    summa = 0
    for i in content:
        summa += str_to_int(i)
    print (content)
    print('Сумма всех чисел: ',summa)

#############################Задание 6#########################################

#6. Сформировать (не программно) текстовый файл. В нём каждая строка должна 
#описывать учебный предмет и наличие лекционных, практических и лабораторных 
#занятий по предмету. Сюда должно входить и количество занятий. 
#Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество 
#занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}            


import mmap
import os

os.listdir(os.getcwd())
def get_num_lines7():
    fp = open("task7.txt", "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines
    
keys_all = [] 
array_all = []  

N7 = int(get_num_lines7()) #Количество строк в файле

with open("task7.txt", "r", encoding = 'utf-8') as file7:
    for s in range(N7):
        summa1 = 0
        
        line = file7.readline()
        
        line = line.split()
        
        a = line.pop(0)    #pop возвращает удаленный элемент
        
        keys_all.append(a)
        
        for i in range(len(line)):
            line[i] = line[i].strip(' () —-лпраб.')
            
        line = list(filter(None, line)) #фильтруем пустые элементы после отбора лишних знаков
        
        for x in line:
            summa1 += int(x)
            
        array_all.append(summa1)
                                                                #print(line)
                                                               #print(keys_all)
    result = dict(zip(keys_all, array_all))
    
    print(result)

#x = '100(л)' - тест ы разные, отбор лишних символов строки (элементов листа)
#print(x.strip(' () лпраб.'))
#x = '20(пр)'
#print(x.strip(' () лпраб.'))
#x = '30(раб)'
#print(x.strip(' () лпраб.'))
#a = x.replace('л','')
#a.replace('()','')   
        
#############################Задание 7#########################################

#7. Создать вручную и заполнить несколькими строками текстовый файл, в котором
#каждая строка будет содержать данные о фирме: название, форма собственности, 
#выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а 
#также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также 
#добавить её в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

import os
import json 
#from statistics import mean
directory = 'G:\\IT\\DIMAGB\\LES5'
os.chdir(directory)
print(os.getcwd())

os.listdir(os.getcwd())

def str_to_int(x):
    if x.isdigit():
        return int(x)
    else:
        return(x)  
    
firms_profit = {}
firms_lost = {}
aver_profit = {}
av_prof = 0


with open("task8.txt", "r", encoding = 'utf-8') as file8:
    
    for line in file8:
                       
        line = line.strip('\n')
        
        firm, sob, plus, minus = line.split(' ')
        
        #print(line)
        
        profit = str_to_int(plus) - str_to_int(minus)
        
        if profit >= 0:
            
            av_prof += profit
            
            firms_profit[str(firm) + ' ' + sob] = profit
            
        else:
            
            firms_lost[str(firm) + ' ' + sob] = abs(profit)
            
    n = av_prof/int(len(firms_profit))  
    #n = mean(av_prof/firms_profit(values))
      
    print (f' Компании, сработавшие с прибылью (Фирма, прибыль): {firms_profit}')
    print (f' Компании, сработавшие с убытком (Фирма, убыток): {firms_lost}')
    print (f' Средняя прибыль составила: {n}')   
     
    aver_profit['average profit'] = n
    
    total = [firms_profit] + [aver_profit]
    
    print(total)
    
with open('les_5.json', 'w', encoding = 'utf-8') as filejs:
    json.dump(total, filejs, ensure_ascii=False)
    
    js_cont = json.dumps(total)
    
    print(f'Содержимое файла .json: \n '
      f' {js_cont}')   

                
































