'''
В институте биоинформатики по офису передвигается робот. Недавно студенты
из группы программистов написали для него программу, по которой робот,
когда заходит в комнату, считает количество программистов в ней и
произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого n нужно использовать
верное окончание слова.

'''

i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)



NumberOfProgrammers = int(input())

# Сотни никак не влияют на склонение слова => избавляемся от них.
MinusHundreds = NumberOfProgrammers % 100

# От 21 до 99 десятки также не влияют => на этом промежутке можно
# от них избавиться
MinusTens = MinusHundreds % 10

if MinusHundreds == 0 or MinusTens == 0:
    print(NumberOfProgrammers, 'программистов')
elif MinusHundreds == 1:
    print(NumberOfProgrammers, 'программист')
elif 1 < MinusHundreds < 5:
    print(NumberOfProgrammers, 'программиста')
elif 5 <=MinusHundreds < 21:
    print(NumberOfProgrammers, 'программистов')
elif MinusTens == 1:
    print(NumberOfProgrammers, 'программист')
elif 1 < MinusTens < 5:
    print(NumberOfProgrammers, 'программиста')
elif 5 <= MinusTens <= 10:
    print(NumberOfProgrammers, 'программистов')

'''
def prog_st(i):
    print(i + ' программист')

def prog_sta(i):
    print(i + ' программиста')

def prog_stov(i):
    print(i + ' программистов')


if NumberOfProgrammers =< 10:
    if 2 <= NumberOfProgrammers < 5:
        prog_sta(NumberOfProgrammers)
    elif NumberOfProgrammers >= 5:
        prog_stov(NumberOfProgrammers)
    else: prog_st(NumberOfProgrammers)

elif NumberOfProgrammers <= 100

'''