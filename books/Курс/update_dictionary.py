'''Напишите функцию update_dictionary(d, key, value), которая принимает на
вход словарь d и два числа: key и value.

 Если ключ key есть в словаре d, то добавьте значение value в список,
 который хранится по этому ключу.
 Если ключа key нет в словаре, то нужно добавить значение в список
 по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key
 в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.'''

def update_dictionary(d, key, value):

    key2 = key * 2
    
    if key in d:
        d[key] += [value]

    elif key2 in d:

        d[key2] += [value]

    elif key2 not in d:
        d[key2] = [value]

d = {}

print(update_dictionary(d, 1, -1))

print(d)

update_dictionary(d, 2, -2)
print(d)

update_dictionary(d, 1, -3)

print(d)
        
