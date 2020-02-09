'''
Напишите программу, на вход которой подаётся прямоугольная матрица в
виде последовательности строк, заканчивающихся строкой, содержащей
только строку "end" (без кавычек).
Программа должна вывести матрицу того же размера, у которой каждый
элемент в позиции i, j равен сумме элементов первой матрицы на позициях
(i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по
соответствующему направлению.

'''
matrix = []

while True:
    line = [k for k in input().split()]
    if line == ['end']:
        break
    else:
        matrix.append(line)

width = len(matrix[0])
height  = len(matrix)
ans = [[0]*width for k in range(height)]

for i in range(height):
    for j in range(width):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di == -1 or di == 1) and (dj == -1 or dj == 1): continue
                x = i + di
                y = j + dj
                if (i + di) == height: x = 0
                if (j + dj) == width: y = 0
                ans[i][j] += int(matrix[x][y])
        ans[i][j] -= int(matrix[i][j])
for k in ans:
    print(*k)
