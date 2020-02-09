def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    start = text.index(begin)
    finish = text.index(end)
    return text[(start + 1):finish]
'''
    ans = ''
    read = False
    for symbol in text:
        if symbol == begin:
            read = True
        elif symbol == end:
            read = False
            break
        elif read:
            ans += symbol
    return ans
'''

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')