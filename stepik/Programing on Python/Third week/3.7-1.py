'''
Напишите программу, которая принимает на стандартный вход список игр
футбольных команд с результатом матча и выводит на стандартный вывод
сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в
следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1

Порядок вывода команд произвольный.

'''
import time

def add_to_dct(team):
    if team not in dct:
        dct[team] = [0, 0, 0, 0, 0]


def end_of_match(team1, goals1, team2, goals2):
    '''
    for each team -- amount of games +1
    for winning team -- wins +1, total points +3
    for losing -- team defeat +1,
    if draw, then for each team -- draws +1, total points +1

    '''

    dct[team1][0] += 1
    dct[team2][0] += 1

    if goals1 == goals2:
        dct[team1][2] += 1
        dct[team1][4] += 1
        dct[team2][2] += 1
        dct[team2][4] += 1
    else:
        if goals1 > goals2:
            winner, looser = team1, team2
        elif goals1 < goals2:
            winner, looser = team2, team1
        dct[winner][1] += 1
        dct[winner][4] += 3
        dct[looser][3] += 1



'''   
                        Dictionary
 Team's name: -- "amount of games" => [0] -- "wins" => [1]    --
              --     "draws" => [2]       -- "defeat" => [3]  --
              -- "total points" => [4]    --
'''
dct = {}
n = int(input())
for _ in range(n):
    t1, g1, t2, g2 = input().split(';')
    add_to_dct(t1)
    add_to_dct(t2)
    end_of_match(t1, g1, t2, g2)

for key, value in dct.items():
    print(key + ':', end= ' ')
    print(*value)


