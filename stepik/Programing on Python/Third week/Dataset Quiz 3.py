'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из
себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для
каждого абитуриента выводит его среднюю оценку по этим трём предметам
на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние
баллы по математике, физике и русскому языку по всем абитуриентам.

В качестве ответа на задание прикрепите полученный файл со средними оценками.

'''

def average_value(a):
    math, fiz, lan = 0, 0, 0
    quant = 0

    for line in a:
        words = line.strip().split(';')
        # For each person
        name = words[0]
        m, f, ln = int(words[1]), int(words[2]), int(words[3])
        av_value = (m + f + ln) / 3
        print(av_value)
        #For main value of subject
        math += m
        fiz += f
        lan += ln
        quant += 1

    print(math / quant, fiz / quant, lan / quant)

file = 'D:\in.txt'
with open(file, 'r') as file_in, open('out.txt', 'w') as file_out:
    text = file_in.readlines()
    average_value(text)
