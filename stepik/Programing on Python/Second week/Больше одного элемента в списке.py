'''
Напишите программу, которая принимает на вход список чисел в одной
строке и выводит на экран в одну строку значения, которые повторяются
в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть
произвольным.

'''

numbers = [int(i) for i in input().split()]
numbers.sort()
rez = []

for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1] and numbers[i] not in rez:
        rez.append(numbers[i])

for i in rez:
    print(i, end= ' ')