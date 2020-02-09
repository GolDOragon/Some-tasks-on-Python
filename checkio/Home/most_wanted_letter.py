def checkio(text: str) -> str:
    dct = {}
    for symbol in text.lower():
        if symbol < 'a' or symbol > 'z':
            continue
        if symbol in dct.keys():
            dct[symbol] += 1
        else:
            dct[symbol] = 1

    popular_symbol = sorted(dct.keys())[0]
    for key in sorted(dct.keys()):
        if dct[key] > dct[popular_symbol]:
            popular_symbol = key

    return popular_symbol


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
