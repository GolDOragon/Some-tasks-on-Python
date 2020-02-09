def is_covered(room, sensors):
    W, H = room
    X, Y, R = [], [], []
    for sensor in sensors:
        x0, y0, r0 = sensor
        X.append(x0)
        Y.append(y0)
        R.append(r0)

    def find_intersection(x0, y0, r0, line):
        
    '''
    проверить углы
        если не входят вернуть ложь
    для каждого сенсора отметить его пересечение с линиями
        a, b =
        b1 = (r**2 - (a - x0)**2)**0.5 + b0
        b2 = -(r**2 - (a - x0)**2)**0.5 + b0
        
        
        х изместен
        у = ()*0.5
    
    top
    left
    right
    bottom
'''
    def check(position):
        for x in (0, W):
            for y in (0, H):
                pass

    for x in (0, W):
        for y in (0, H):
            r = ((x0 - x)^2 + (y0 - y)^2)**0.5
            if r > r0:
                return False
    return True
assert is_covered([200, 150], [[100, 75, 130]]) == True  # example #1
assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True  # example #2
assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False  # example #3
