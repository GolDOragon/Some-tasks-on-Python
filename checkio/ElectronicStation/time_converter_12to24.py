def time_converter(time):
    tme, middle = time.split()
    hours, minutes = tme.split(':')
    hours = int(hours)
    if hours == 12:         # or hours = hours % 12
        hours = 0

    if middle == 'p.m.':
        hours += 12
    return '{:02d}:{:02d}'.format(hours, int(minutes))


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")