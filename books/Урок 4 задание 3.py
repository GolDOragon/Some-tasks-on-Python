# Урок 4 задание 3
# Отгадать слово

import random

inventory = ("нож", "щит", "меч", "крушка", "ложка", "рука",
             "ручка", "тетрадь", "лист", "очки", "мышь")

num = random.randrange(11)
word = inventory[num]
point = 0

print(
"""
        Добро пожаловать!

     Сейчас мы сыграем в игру
"""
)
print('Правила просты: '  \
      'я загадываю число и сообщаю сколько в нём букв, ты отгадываешь')

print(len(word))
input()

print('Что? Сложно? ... Хорошо, можешь спросить меня какая буква есть в слове.')

while point != 5:
    letter = input("Так какая буква тебе нужна? ")
    
    if len(letter) != 1:
        print("Я сказал про ОДНУ букву!")
        continue
    elif letter in word:
        print("Есть")
    elif not letter in word:
        print("Отсутствует")
    else:
        print("Следуй правилам")

    point +=1

your_word = input("Так какое слово я загадал? ")

if your_word.lower() == word:
    print("Черт, ты угадал...")
else:
    print("Это было ", word)
    print("ха-ха... Ха-ха... ХА-ХА-ХА")

input()
    
