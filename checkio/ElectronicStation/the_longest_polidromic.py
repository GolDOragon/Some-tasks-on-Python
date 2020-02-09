def longest_palindromic(a):
    longest_pal = a[0]
    polidromic_len = len(a)
    for i in range(polidromic_len):
        delta = 0
        while (i - delta) >= 0 and (i + delta) < polidromic_len:
            # if go out from index: break
            if a[i - delta] != a[i + delta]:
                break
            delta += 1
        if len(longest_pal) < (1 + 2 * (delta - 1)):
            longest_pal = a[(i - delta + 1):(i + delta)]

    return longest_pal


if __name__ == '__main__':
#    print("Example:")
#    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
#    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
