'''Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на
наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть
больше одной строки) и выводит самое частое слово в этом тексте и через
пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.'''

def score_word(a):

    words = []
    word = ''
    i = 0

    while i < len(a):

        if a[i] != ' ':

            word += a[i]

            i += 1

        elif a[i] == ' ':

            if word in words:

                words[word] += 1

            elif word not in words:

                words[word] = 1

            word = ''
            i += 1

    for _ in words:

        if 

        '''        

        word += i

    if word in words:

        words[word] += 1

    elif word not in words:

        words[word] = 1
        

        if i != ' ' and word == '':

            word = i

        elif i != ' ' and word != '':

            word += i

        elif i == ' ' and word != '':

            if word in words:

                words[word] += 1

            else:

                words[word] = 1

            word = ''

    if word in words:
        words[word] += 1
        
    else: words[word] = 1
    
    maxi = word

    for j in words:

        if words[j] > words[maxi]:

            words[maxi] = words[j]

    print(words[maxi])
    print(maxi)

'''
file = input()

with open ('dataset_3363_3.txt') as inf:

    text = inf.readlines().lower().split('\n')

    score_word(text)
    
    
