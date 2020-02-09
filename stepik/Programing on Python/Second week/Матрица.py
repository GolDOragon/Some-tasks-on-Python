'''
Напишите программу, на вход которой подаётся прямоугольная матрица в
виде последовательности строк, заканчивающихся строкой, содержащей только
строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент
в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j),
(i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по
соответствующему направлению.

'''
matrix = []
str = []


while True:
    line = [k for k in input().split()]
    if line == ['end']:
        break
    else:
        for m in line:
            str.append(int(m))
        matrix.append(str)
        str = []

w_matrix = len(matrix[0])
h_matrix =len(matrix)

ans = [[0]*w_matrix for _ in range(h_matrix)]


for i in range(h_matrix):
    for j in range(w_matrix):
        for ver in [-1, 1]:
            for hor in [-1, 1]:
                if (i + ver) == h_matrix:
                    ans[i][j] += matrix[0][j + hor]
                elif (j + hor) == w_matrix:
                    ans[i][j] += matrix[i + ver][0]
                else:
                    ans[i][j] += matrix[i + ver][j + hor]
'''           
                if (i + ver) < h_matrix and  (j + hor) < w_matrix:
                    ans[i][j] += matrix[i + ver][j + hor]
                elif (i + ver) == h_matrix and (j + hor) == w_matrix:
                    ans[i][j] += matrix[i + ver - h_matrix][j + hor - w_matrix]
                else:
                    if (i + ver) == h_matrix:
                        ans[i][j] += matrix[i + ver - h_matrix][j+ hor]
                    if (j + hor) == w_matrix:
                        ans[i][j] += matrix[i + ver][j + hor - w_matrix]
'''
for i in ans:
    print(*i)


