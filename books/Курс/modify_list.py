'''Напишите функцию modify_list(l), которая принимает на вход список
целых чисел, удаляет из него все нечётные значения, а чётные нацело
делит на два. Функция не должна ничего возвращать, требуется только
изменение переданного списка. '''


def modify_list(a):

    
    spis = []

    for i in range(len(a)):

        if a[i] % 2 == 0:

            spis.append((a[i] // 2))

    a[:] = spis

   

    
    


lst = [1, 2, 3, 4, 5, 6]
print('first')
print(modify_list(lst))
print('second')
print(lst)

modify_list(lst)
print('third')
print(lst)
