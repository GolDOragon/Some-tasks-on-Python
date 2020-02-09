def frequency_sort(items):
    dct = dict()
    recorded_items, ans = [], []

    for element in items:
        if element in recorded_items:
            continue

        recorded_items.append(element)
        count_element = items.count(element)
        if count_element in dct:
            dct[count_element] += [element]
        else:
            dct[items.count(element)] = [element]

    for frequency in sorted(dct.keys(), reverse=True):
        for element in dct[frequency]:
            ans.extend([element] * frequency)

    return ans


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
