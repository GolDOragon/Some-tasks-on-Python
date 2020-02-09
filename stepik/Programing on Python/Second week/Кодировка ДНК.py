'''
Узнав, что ДНК не является случайной строкой, только что поступившие в
Институт биоинформатики студенты группы информатиков предложили
использовать алгоритм сжатия, который сжимает повторяющиеся символы в
строке.
Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых
символов исходной строки заменяются на этот символ и количество его
повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным
алгоритмом и выводит закодированную последовательность на стандартный
вывод. Кодирование должно учитывать регистр символов.

'''

genome = input() + ' '
s = 0
zip_genome = ''

for i in range(1, len(genome)):
    nukl = genome[i - 1]
    s += 1
    if genome[i - 1] != genome[i]:
        zip_genome += nukl + str(s)
        s = 0
print(zip_genome)