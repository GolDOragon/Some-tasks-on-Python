def safe_pawns(pawns: set) -> int:
    lst = [['.' for i in range(9)] for j in range(9)]
    pwns = []
    count = 0
    for pawn in pawns:
        x, y = ord(pawn[0]) - 97, 8 - int(pawn[1])
        xy = x, y
        pwns.append(xy)
        lst[y][x] = 'o'

    for x,y in pwns:
        for dlt in [-1, 1]:
            try: data = lst[y + 1][x + dlt]
            except IndexError: continue

            if data == 'o':
                count += 1
                break

#######
    y = 0
    for i in lst:
        print(8 - y, end=' ')
        y += 1
        print(*i)
    print(' ', end=' ')
    for i in range(8):
        print(chr(i+97), end=' ')
    print('', end='\n  ')
    for i in range(8):
        print(i+1, end=' ')
    print('\n ----------------')
#####
    return count
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
