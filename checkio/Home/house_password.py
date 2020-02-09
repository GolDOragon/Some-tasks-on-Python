def checkio(data: str) -> bool:
    if len(data) < 10:
        return False
    digit_test: bool = False
    upper_test: bool = False
    lower_test: bool = False

    for symbol in data:
        if not digit_test:
            digit_test = symbol.isdigit()
        if not upper_test:
            upper_test = symbol.isupper()
        if not lower_test:
            lower_test = symbol.islower()
        if digit_test and upper_test and lower_test:
            return True
    return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
