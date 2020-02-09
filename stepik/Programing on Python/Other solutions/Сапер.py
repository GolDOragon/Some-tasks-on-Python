'''
Обычный сапер. На вход подается размеры поля, количество мин и их координаты

'''

x, y, amount = [int(i) for i in input().split()]
field = [[0]*x for _ in range(y)]
for _ in range(amount):
    i, j = [int(k) - 1 for k in input().split()]
    field[i][j] = '*'

    for ver in [-1, 0, 1]:
        for hor in [-1, 0, 1]:
            if 0 <= (i + ver) < x and 0 <= (j + hor) < y:
                if field[i + ver][j + hor] != '*':
                    field[i + ver][j + hor] += 1
''' 
alternative option
            if (i + ver) == -1 or (j + hor) == -1 or (i + ver) == x or (j + hor) == y:
                continue
            elif field[i + ver][j + hor] != '*':
                field[i + ver][j + hor] += 1
                '''

for i in range(x):
    for j in range(y):
        if field[i][j] == 0:
            field[i][j]= '.'

for line in field:
    print(*line)






