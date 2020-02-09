# Урок 4 задача 1
# Считалочка

print('Привет! Я могу посчитать любую последовательность.\nДля этого:', end='')

min = int(input(' мне нужно начало отсчета '))
max = int(input('\t конец счета '))
step = int(input('\t шаг '))

for i in range(min, max, step):
    
    print(i)

input()

