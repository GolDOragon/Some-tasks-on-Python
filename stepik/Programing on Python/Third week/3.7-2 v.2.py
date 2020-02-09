'''
В какой-то момент в Институте биоинформатики биологи перестали понимать,
что говорят информатики: они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они
использовали при общении подстановочный шифр, т.е. заменяли каждый
символ исходного сообщения на соответствующий ему другой символ. Биологи
раздобыли ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр
подстановки. Программа принимает на вход две строки одинаковой длины,
на первой строке записаны символы исходного алфавита, на второй
строке — символы конечного алфавита, после чего идёт строка, которую
нужно зашифровать переданным ключом, и ещё одна строка, которую нужно
расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в
шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с
помощью этого шифра. Получаем следующие строки, которые и передаём на
вывод программы:
*d*%*d*#*d*
dacabac

'''

def translate(a, prim_lang, follow_lang):
    for i in a:
        letter = follow_lang[prim_lang.index(i)]
        print(letter, end='')
    print()


bio_lang = input()
inf_lang = input()
b_to_i = input()
i_to_b = input()

translate(b_to_i, bio_lang, inf_lang)
translate(i_to_b, inf_lang, bio_lang)

'''
for i in b_to_i:
    letter = inf_lang[bio_lang.index(i)]
    print(letter, end='')
for i in i_to_b:
'''

