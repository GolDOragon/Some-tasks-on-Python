'''
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на
наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть
больше одной строки) и выводит самое частое слово в этом тексте и через
пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3

'''

def most_referance_word(a):
    dic = {}
    for word in a:
        if word in dic:
            dic[word] += 1
        elif word not in dic:
            dic[word] = 1
    most_ref_word = word

    for key in dic.keys():
        if dic[key] > dic[most_ref_word]:
            most_ref_word = key
        elif dic[key] == dic[most_ref_word]:
            if key < most_ref_word:
                most_ref_word = key
    print(most_ref_word, dic[most_ref_word])

import time
text = ''
file_name = input()
start_time = time.time()

with open(file_name, 'r') as file_in:
    text = file_in.read().lower().strip("!?,.").split()
    most_referance_word(text)

print("time elapsed: {:.10f}s".format(time.time() - start_time))
'''
for i in open('D:\in.txt'):
    text += i.lower().split()
    print(text)
    '''