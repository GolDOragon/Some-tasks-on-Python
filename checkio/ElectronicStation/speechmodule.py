FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

"""
def checkio(number):
    unit = number % 10
    ten = number % 100 // 10
    hundred = number // 100

    if hundred != 0:
        first = f'{FIRST_TEN[hundred - 1]} {HUNDRED}'
    else:
        first = ''

    if ten > 1:
        second = f' {OTHER_TENS[ten - 2]}'
        third = f' {FIRST_TEN[unit - 1]}'
    elif ten == 1:
        second = f' {SECOND_TEN[number % 100 - 10]}'
        third = ''
    else:
        second = ''
        third = f' {FIRST_TEN[unit - 1]}'
    if unit == 0:
        third = ''
    return f'{first}{second}{third}'.lstrip()
"""

def checkio(number):
    res = []
    hundred, other = divmod(number, 100)
    if hundred:
        res.append(f'{FIRST_TEN[hundred - 1]} {HUNDRED}')
    if 10 < other < 19:
        res.append(SECOND_TEN[other - 10])
    else:
        ten, unit = divmod(other, 10)
        if ten:
            res.append(f'{OTHER_TENS[ten - 2]}')
        if unit:
            res.append(f'{FIRST_TEN[unit - 1]}')
    return ' '.join(res)
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')