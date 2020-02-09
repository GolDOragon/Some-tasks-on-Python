def checkio(data):
    # массив чисел
    NUMERALS = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    # ответ
    number = ''
    # divmod просто разбивает число на частное и остаток от деления
    thousand, hundred = divmod(data, 1000)
    hundred, decade = divmod(hundred, 100)
    decade, unit = divmod(decade, 10)

    T = ('', 'M', 'MM', 'MMM')
    H = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
    D = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
    U = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')

    return T[thousand] + H[hundred] + D[decade] + U[unit]
    # просто преобразуем арабское число в римское
    # до 4, 4, 5, до 9, 9
    # смысл в том, чтобы из NUMERALS брать нужный порядок и относительно его "играть"
    def transformation(number: int, number_order: int) -> str:
        if number < 4:
            return NUMERALS[number_order] * number
        elif number == 4:
            return NUMERALS[number_order] + NUMERALS[number_order + 1]
        elif number == 5:
            return NUMERALS[number_order + 1]
        elif number < 9:
            return NUMERALS[number_order + 1] + NUMERALS[number_order] * (number - 5)
        elif number == 9:
            return NUMERALS[number_order] + NUMERALS[number_order + 2]

    number += transformation(thousand, 6)
    number += transformation(hundred, 4)
    number += transformation(decade, 2)
    number += transformation(unit, 0)

    return number
    '''
    кортеж римских цифр 
    получить число
    разбить на порядки
    для каждого порядка 
        если цифра = 0
            ничего не пишем
        если цифра < 4 
            записываем порядок нужное число раз
        если цифра = 4:
            записать пре-пре + предыдущий
        если цифра = 5
            записать предыдущий
        если цифра < 9
            записать предыдущий + (цифра - 5) пре-пре
        если цифра = 9
            записать следующий порядок
            
    
    '''



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
