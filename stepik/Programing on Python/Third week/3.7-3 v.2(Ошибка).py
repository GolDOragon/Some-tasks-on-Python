
vocabliary, text = [], []
words = []
d = int(input())
for _ in range(d):
    vocabliary.append(input().lower())
vocabliary = set(vocabliary)

L = int(input())
for _ in range(L):
    words.append(input().split())
text = set(words)

#text.difference_update(vocabliary)
print(text - vocabliary)