def clockwise_rotation(old_square):
    """ clockwise rotation"""
    turned_square = ([], [], [], [])
    for i in range(n):
        for j in range(n):
            turned_square[3 - j].append(old_square[i][j])
    return turned_square


def recall_password(cipher_grille, ciphered_password):
    def counter_clockwise_rortation(old_square):
        """ counter-clockwise rotation"""
        turned_square = ([], [], [], [])
        for i in range(n):
            for j in range(n):
                turned_square[j].append(old_square[3 - i][j])
        return turned_square

    def open_chars(grille):
        ''' If there is X -> write down symbol'''
        answer = ''
        for i in range(n):
            for j in range(n):
                if grille[i][j] == "X":
                    answer += ciphered_password[i][j]
        return answer

    n = 4
    grille = [list(i) for i in cipher_grille]
    password = ''
    for _ in range(4):
        password += open_chars(grille)
        grille = counter_clockwise_rortation(grille)
    print(password)
    return password


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
