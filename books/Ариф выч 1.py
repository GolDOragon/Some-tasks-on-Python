#Сумма остатков от деления числа на 2, 4, 5, 9, 10, 25


chislo = int(input('Введите целое число: '))

ost_2 = chislo % 2

ost_4 = chislo % 4

ost_5 = chislo % 5

ost_9 = chislo % 9

ost_10 = chislo % 10

ost_25 = chislo % 25

summ = ost_2 + ost_4 + ost_5 + ost_9 + ost_10 + ost_25

print('\nСумма Остаток от деления на 2: ', summ)

input()
