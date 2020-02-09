def probability(dice_number, sides, target):
    def prob(dice_number, sides, target):
        probability = 0.0
        for i in range(1, sides + 1):
            # target = value(1dice) + value(other dises)
            # or target = one + other
            one = i
            other = target - i
            # probability(values(xdy) < x) == 0 and
            # probability(values(xdy) > x * y) == 0
            if other < dice_number or other > dice_number * sides: continue
            prob_first = worklist[0][one]
            prob_second = worklist[dice_number - 1][other]
            probability += round(float(prob_first * prob_second), 5)
        return round(probability, 5)


    # create work list and write probability for 1 dice
    worklist = [[0.0 for j in range(target + 1)] for i in range(dice_number)]
    for i in range(1, target + 1):
        if i > sides: break
        worklist[0][i] = round(1 / sides, 5)
    '''worklist for xdy target = n
    dices\value|  0  |  1  |  2  |  3  | ... |  n   
    1dice      | 0.0 | 1/y | 1/y | 1/y | ... |  ?
    2dice      | 0.0 | 0.0 |  ?  |  ?  | ... |  ?
    ..............................................
    xdice      |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  

    '''
    print('dices\\value ', end='')
    for i in range(len(worklist[0])):
        if i < 10:
            print(i, end='  |  ')
        else:
            print(i, end=' |  ')
    print()
    j = 0
    for i in worklist:
        print(f'  {j + 1}dice', end='  | ')
        j += 1
        print(*i, sep=' | ')

    # write probability for each cell, start with probability(2d0)
    for dice in range(1, dice_number):
        for cell in range(len(worklist[dice])):
            worklist[dice][cell] = prob(dice, sides, cell)


    print('          ', end='')
    for i in range(len(worklist[0])):
        if i < 10:
            print(i, end=' --- ')
        else:
            print(i, end=' -- ')
    print()
    j = 0
    for i in worklist:
        print(f'{j + 1}dice', end=' -- ')
        j += 1
        print(*i, sep='---')

    print(round(worklist[dice_number - 1][target], 4))
    return round(worklist[dice_number - 1][target], 4)



if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    probability(4, 10, 9)
    '''
    assert probability(2, 6, 3) == 0.0556
    assert probability(2, 6, 4) == 0.0833
    assert probability(2, 6, 7) == 0.1667
    assert probability(2, 3, 5) == 0.2222
    assert probability(2, 3, 7) == 0.0000
    assert probability(3, 6, 7) == 0.0694
    assert probability(10, 10, 50) == 0.0375
    print('Complete!')

    probability(1, 2, 999)
    '''