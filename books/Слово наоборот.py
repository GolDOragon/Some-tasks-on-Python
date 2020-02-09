# Урок 4 задача 2
# Печатаем текст наоборот
#
#


word = input('Введите слово и получите его наоборот ')
new_word = ''

while word:

    length = len(word) - 1
    new_word += word[length : ]
    word = word [:length]

print(new_word.capitalize())

input('\nНажмите Enter для выхода')
