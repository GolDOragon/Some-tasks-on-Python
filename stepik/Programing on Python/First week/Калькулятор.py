'''
Напишите простой калькулятор, который считывает с пользовательского ввода
три строки: первое число, второе число и операцию, после чего применяет
операцию к введённым числам ("первое число" "операция" "второе число")
и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить
строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.

'''

# First try, only 'if-else' operator
'''
FirstNumber = float(input())
SecondNumber = float(input())
Operation = input()


if Operation == '+':
    print(FirstNumber + SecondNumber)
elif Operation == '-':
    print(FirstNumber - SecondNumber)
elif Operation == '/' and SecondNumber != 0:
    print(FirstNumber / SecondNumber)
elif Operation == '*':
    print(FirstNumber * SecondNumber)
elif Operation == 'mod' and SecondNumber != 0:
    print(FirstNumber % SecondNumber)
elif Operation == 'pov':
    print(FirstNumber ** SecondNumber)
elif Operation == 'div' and SecondNumber != 0:
    print(FirstNumber // SecondNumber)
else:
    print('Деление на 0!')

'''


# Second try, I using a dictionary to avoid repetitions and simplify code

# dictionary for required operations
import operator
Operations = {'+': operator.add, '-': operator.sub, '/': operator.truediv,
              '*': operator.mul, 'mod': operator.mod, 'pow': operator.pow,
              'div': operator.floordiv}

FirstNumber = float(input())
SecondNumber = float(input())
Operation = input()

if (Operation in ['+', '-', '*', 'pow'] or
    Operation in ['/', 'mod', 'div'] and SecondNumber != 0):

    print(Operations[Operation](FirstNumber, SecondNumber))

else:
    print('Деление на 0!')

