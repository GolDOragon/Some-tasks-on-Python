def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    max_count, count = 0, 0
    letter = ''
    for symbol in line:
        if symbol == letter:
            count += 1
            if count > max_count: max_count = count
        elif symbol != letter:
            count = 1
            letter = symbol

    return max_count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4
    assert long_repeat('ddvvrwwwrggg') == 3
    assert long_repeat('abababaab') == 2
    assert long_repeat('') == 0
    print('"Run" is good. How is "Check"?')
