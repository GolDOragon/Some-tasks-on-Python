from typing import List


def checkio(game_result: List[str]) -> str:
    def ckeck(str: str) -> str:
        nonlocal result
        if str == 'XXX':
            result = 'X'
        elif str == 'OOO':
            result = 'O'

    result = ''
    line = f'{game_result[0]}{game_result[1]}{game_result[2]}'
    ckeck(line[::4])  # left-right diagonal
    ckeck(line[2:7:2])  # Right-left diagonal

    for i in [0, 1, 2]:
        ckeck(line[i::3])  # vertical lines
        ckeck(game_result[i])  # horizontal lines

    if result:
        return result
    else:
        return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
