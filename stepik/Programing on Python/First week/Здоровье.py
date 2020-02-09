''' Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы
 A часов в сутки, но пересыпать тоже вредно и не стоит спать более B
 часов. Сейчас Аня спит H часов в сутки. Если режим сна Ани удовлетво-
 ряет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
 Если Аня спит менее A часов, выведите “Недосып”, если же более
 B часов, то выведите “Пересып”.
Получаемое число A всегда меньше либо равно B.

На вход программе в три строки подаются переменные в следующем порядке: A, B, H.

'''

A, B, H = [int(x) for x in input().split()]

if A <= H <= B:
    print('Это нормально')
elif A > H:
    print('Недосып')
elif B < H:
    print('Пересып')
