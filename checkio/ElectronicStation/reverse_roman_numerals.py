def reverse_roman(roman_string):
    def func(roman_order, order):
        ln = len(roman_order)
        for index in range(ln):
            nonlocal roman_string
            roman_numeral = roman_order[ln - (index + 1)]
            roman_len = len(roman_numeral)
            if roman_numeral in roman_string[:roman_len]:
                roman_string = roman_string[len(roman_order[ln - (index + 1)]):]
                return (ln - (index + 1)) * order

    answer = 0
    T = ('', 'M', 'MM', 'MMM')
    H = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
    D = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
    U = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
    answer += func(T, 1000)
    answer += func(H, 100)
    answer += func(D, 10)
    answer += func(U, 1)
    return answer


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
