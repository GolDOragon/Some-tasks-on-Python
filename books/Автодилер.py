# Урок 2 задача 3
# Автодилер
# Стоимость автомобиля без наценок ==> full cost

auto = int(input('Введите стоимость авто ($): '))

nalog = float(input('Налог (%): '))
              
reg_sbor = float(input('Регистрационный сбор (%): '))

agent_sbor = int(input('Агентный сбор ($): '))

dostavka = int(input('Цена доставки авто по месту назначения($): '))

itog = auto * ( 100 + nalog + reg_sbor )/100 + agent_sbor + dostavka

itog = int(itog // 1)
print('Full cost of auto: ', itog, '$.')

input('\n\n Enter для выхода')

