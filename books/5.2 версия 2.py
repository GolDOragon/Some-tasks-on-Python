# Урок 5 задание 2
# "Генератор персонажей" для ролевой игры
# Распеделение 30 пунктов между Силой, Здоровьем, Мудростью и Ловкостью.

chars = {'Сила    ' : 0, 'Здоровье' : 0, 'Мудрость' : 0, 'Ловкость' : 0}
points = 30
choice3 = ""

while points > 0 or choice3 != 'Y':
    point = 31
    
    print('У вас осталось', points,'очков. На данный момент ваши характеристики:')
    for i in chars:
        print(i, end = '\t')
        print(chars[i])
        

    input('Далее...')
    print('\nРаспределите оставшиеся очки.'
          """
    "Генератор персонажей"

    0 - Выход
    1 - Сила
    2 - Здоровье
    3 - Мудрость
    4 - Ловкость

          """)
    choice1 = input('Ваш выбор: ')

    if choice1 == '0':
        break
    elif choice1 == '1':
        term = 'Сила    '
    elif choice1 == '2':
        term = 'Здоровье'
    elif choice1 == '3':
        term = 'Мудрость'
    elif choice1 == '4':
        term = 'Ловкость'
    else:
        print('Вашего выбора нет.\n')
        continue
    
    print('\tВложить хар-ки - "+" \n\tУбрать хар-ки - "-". ')

    choice2 = input('Ваш выбор: ')
    if choice2 == '+':   
        while point > points:
            print('У вас всего', points, 'очков.')
            point = int(input('Сколько очков вложить? '))
                                    
        points -= point
        chars[term] += point

    elif choice2 == '-' :
        while point > chars[term]:
            print('В характеристике', term, 'только', chars[term],'очков.')
            point = int(input('Сколько очков отнять? '))
            
        points += point
        chars[term] -= point
        
    else:
        print('Вашего выбора', choice2,'нет.')
        continue
    
    if points <= 0:
        choice3 = input('Закончить создание персонажа? Y/N ')
        choice3 = choice3.upper()
        
print('\nПерсонаж создан, его характеристики:')
for i in chars:
    print(i, end = '\t')
    print(chars[i])
print('Осталось', points, 'очков.')

input('Enter для выхода')
    
