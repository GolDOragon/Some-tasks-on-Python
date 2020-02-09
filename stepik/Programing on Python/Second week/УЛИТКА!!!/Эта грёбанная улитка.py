'''Выведите таблицу размером n×n, заполненную числами от 1 до n2 по
спирали, выходящей из левого верхнего угла и закрученной по часовой
стрелке

'''

n = int(input())
sheet = [[0 for i in range(n)] for j in range(n)]

# Номера строки и столбца.
i, j = 0, 0

y = 1

# Номер столба(строки), с которых надо начать и которыми надо закончить.
h, k = 0, 0

while y <= n*n:

    for j in range(h, n - k):
        sheet[i][j] = y
        y += 1
    h += 1

    for i in range(h, n - k):
        sheet[i][j] = y
        y += 1
    k += 1


    for j in range(n - k - 1, h-2, -1):
        sheet[i][j] = y
        y += 1

    for i in range(n - k - 1, h-2, -1):
        sheet[i][j] = y
        y += 1
    k += 1
    h -= 1

for i in sheet:
    print(i)
