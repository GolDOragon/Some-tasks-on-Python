def from_camel_case(name):
    def is_upper(symbol):
        if 65 <= ord(symbol) <= 90:
            return True

    def save_word(start, stop):
        word = name[start:stop].lower()
        words.append(word)

    words = []
    start = 0
    for i in range(len(name)):
        if is_upper(name[i]):
            save_word(start, i)
            start = i
    save_word(start, len(name))
    name = ''
    for word in words:
        name += word + '_'
    return name[1:-1]


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")

    '''
    операции = словарь() // т.е. пары "ключ:значение"
    функция добавить_операцию (имя, выражение):
        если имя нет в операции
            добавить ключ имя в операции
            операции(ключ) = значение
    
    функция вычисление (имя_операции, число 1, число 2):
        если имя_операции есть в словаре
            операция(число 1, число 2)
        
    
    '''
'''
array = [1, 2, -3, ..., 43]
result = 0
s = 0
for i in range(0, len(array)):
    s += array[i]
    if s > result:
        result = s
        index = (0, i)
s = 0
for i in range(0, i+1):
    if


'''
