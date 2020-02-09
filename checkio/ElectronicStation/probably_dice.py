def prob_for_1(target, sides):
    if 0 < target <= sides:
        return round(1 / sides, 5)
    else:
        return 0


def prob_for_2(target, sides):
    probability = 0
    for first in range(1, sides + 1):
        second = target - first
        prob_first = round(1 / sides, 5)
        if second > sides:
            prob_second = prob_for_2(second, sides)
        elif second <= sides:
            prob_second = round(1 / sides, 5)
        probability += round(prob_first * prob_second, 5)
    return probability


def probability(dice_number, sides, target):
    prob1 = 1 / sides

    def prob_for_2(target, sides):
        probability = 0
        for first in range(1, sides + 1):
            second = target - first
            prob_first = round(1 / sides, 5)
            if second <= sides:
                prob_second = round(1 / sides, 5)

    return 0.0


print(prob_for_2(7, 6))
print(prob_for_2(14, 6))

"""
if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
    """
