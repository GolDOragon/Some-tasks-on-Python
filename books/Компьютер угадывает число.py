#   "Отгадай число"
# На основе алгоритма из книги сам составляю программу

print('\tЗдраствуй, незнакомец!')
print('Я хотел бы сыграть с тобой в игру...\n\n\t "Отгадай число"\n' \
      '\nПравила просты: я отгадываю загаданное тобой число \n(от одного до ста) ' \
      'за наименьшее количество попыток.')

ans = ''
x = 50
maxx = 100
minn = 1

while ans != 'Y':
    print('Это число', x, '? \nОтвечай в форме: Y - Да,' \
                '> - больше, < - меньше')
    ans = input()

    if ans == 'Y':
        break
    elif ans == '>':
        minn = x
        x = minn + (maxx - minn)//2
    elif ans == '<':
        maxx = x
        x = (maxx + minn) // 2
        
print('Это было', x)

input()
        
