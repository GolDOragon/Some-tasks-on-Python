''' Напишите программу, на вход которой подаётся прямоугольная матрица в
 виде последовательности строк, заканчивающихся строкой, содержащей только
 строку "end" (без кавычек).

 Программа должна вывести матрицу того же размера, у которой каждый элемент
 в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j),
 (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
 с противоположной стороны матрицы.

 В случае одной строки/столбца элемент сам себе является соседом по
 соответствующему направлению.'''
mat = []
st = ''

# Ввод чисел
while True:

    st = [i for i in input().split()]

    "Если введено 'end', то ввод прекращается"
    if st == ['end']:
        break
    else:
        mat.append(st)

#Создаем матрицу такого же размера, но с нулями
ans = [[0] * len(mat[i]) for i in range(len(mat))]

#Перебираем все строки
for i in range(len(mat)):

    #Перебираем все элементы строки
    for j in range(len(mat[i])):

        # Прибавляем соседей по вертикали
        for di in (-1, 1):
            y = i + di
            if y >= len(mat):  #Если выходим за пределы матрицы - в начало
                y = 0
                
            ans[i][j] += int(mat[y][j])
           
        # Прибавляем соседей по горизонтали
        for dj in (-1, 1):

            x = j + dj
            if x >= len(mat[i]):  #Если выходим за пределы матрицы - в начало
                x = 0
                
            ans[i][j] += int(mat[i][x])

for i in ans:
    print(*i)
