def time_converter(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    if hours == 0:
        return f'{hours + 12}:{minutes} a.m.'
    elif hours == 12:
        return f'{hours}:{minutes} p.m.'
    elif hours > 12:
        return f'{hours - 12}:{minutes} p.m.'
    elif hours < 12:
        return f'{hours}:{minutes} a.m.'




if __name__ == '__main__':
    print("Example:")
    print(time_converter('09:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")