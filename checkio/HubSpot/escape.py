from fractions import Fraction


def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly

    def travel_time(delta, speed):
        if speed != 0 and delta is not None:
            time = Fraction(delta, abs(speed))
            return time
        return False

    def distance_to_wall():
        # for horizontal
        if vx > 0:
            xdelta = W - x0
        elif vx < 0:
            xdelta = x0
        else:
            xdelta = None
        # for vertical
        if vy > 0:
            ydelta = H - y0
        elif vy < 0:
            ydelta = y0
        else:
            ydelta = None
        return xdelta, ydelta

    def is_out():
        if (y0 >= H and vy > 0) and (W - d) / 2 < x0 < (W + d) / 2:
            return True
        return False

    def change_duration():
        if x0 <= 0 or x0 >= W:
            xspeed = -vx
        else:
            xspeed = vx

        if y0 <= 0 or y0 >= H:
            yspeed = -vy
        else:
            yspeed = vy

        return xspeed, yspeed

    def new_coordinates(time):
        new_x = x0 + vx * time
        new_y = y0 + vy * time
        return new_x, new_y

    if is_out():
        return True
    for i in range(20):
        dx, dy = distance_to_wall()
        x_time = travel_time(dx, vx)
        y_time = travel_time(dy, vy)

        if x_time and y_time:
            if x_time <= y_time:
                time = x_time
            else:
                time = y_time
        elif x_time:
            time = x_time
        elif y_time:
            time = y_time
        else:
            time = 0

        x0, y0 = new_coordinates(time)
        if is_out():
            return True
        vx, vy = change_duration()
    return False


if __name__ == '__main__':
    '''
    print("Example:")
    print(escape([1000, 1000, 200], [0, 0, 100, 0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"

    assert escape([1200, 2000, 400], [0, 0, -600, -200]) == False
        '''
    assert escape([1200, 2000, 350], [600, 2000, 600, 1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
