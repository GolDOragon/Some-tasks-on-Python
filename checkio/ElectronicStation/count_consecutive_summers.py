def count_consecutive_summers(num):
    s, count = 0, 0
    i, first_num = 0, 0
    while i <= num:
        if s == num:
            count += 1
            s -= first_num
            first_num += 1
        elif s < num:
            s += i
            i += 1
        elif s > num:
            s -= first_num
            first_num += 1
    return count

print(count_consecutive_summers(42))