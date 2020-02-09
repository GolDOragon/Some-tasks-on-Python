def sun_angle(time):
    hours, minutes = (int(x) for x in time.split(':'))

    minutes = hours * 60 + minutes
    if (6 * 60) <= minutes <= (18 * 60):
        return (minutes - (6 * 60)) / 4
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")