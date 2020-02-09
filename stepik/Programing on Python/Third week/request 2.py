'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя
следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из
этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

'''

import requests
url = ''

with open('D:\dataset_3378_3.txt', 'r') as file_in:
    url = file_in.readline().strip()

r = requests.get(url)
url = r.text
url_mane = 'https://stepic.org/media/attachments/course67/3.6.3/'

while url[:2] != 'We':
    r = requests.get(url_mane + str(url))
    url = r.text

with open('D:\out.txt', 'w') as file_out:
    file_out.write(url)
