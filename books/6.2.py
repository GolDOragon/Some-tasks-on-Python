# Урок 6 задание
# "Откгадай число" исполненная с применением ask_number()
#


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def make_number():
    """Make a number 1-100."""
    import random
    num = random.randint(1, 100)
    return num

def more_less(ans, num):
    """Выводит больше или меньше число"""
    if ans > num:
        print('Введенное число больше загадонного.')
    elif ans < num:
        print('Введенное число меньше загадонного.')
    else:
        print('Ты угадал число!.')       

def main():
    num = make_number()
    ans = None

    low = 1
    high = 100

    while ans != num:
        ans = ask_number('Какое число я загадал? ', low, high)
        more_less(ans, num)

        if ans > num and ans <= high:
            high = ans
            print('Верхний предел: ', high)
        elif ans < num and ans >= low:
            low = ans       
            print('Нижний предел: ', low)
    print('Поздравляю ты угадал это', num)

input()
main()
input()

