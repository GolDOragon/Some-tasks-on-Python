def popular_words(text: str, words: list) -> dict:
    ans = dict()
    for word in text.split():
        if word.lower() in words:
            if word.lower() in ans.keys():
                ans[word.lower()] += 1
            else:
                ans[word.lower()] = 1
    for key in words:
        if key not in ans.keys():
            ans[key] = 0
    return ans


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")