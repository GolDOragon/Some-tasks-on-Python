def is_stressful(subj):
    """
        recoognise stressful subject
    """

    # find 3 last exclamation marks
    def marks_test(sub):
        for i in [-1, -2, -3]:
            if sub[i] != '!':
                return False
        return True

    def upper_test(letter):
        if 'a' <= letter <= 'z':
            return False
        return True

    def words_test(testing_word):
        nonlocal test2
        convert_word = testing_word[0].lower()  # I didn't check first symbol on alphabet
        for letter in testing_word:
            if letter.isalpha():
                if test2:  # default test2 == True
                    test2 = upper_test(letter)
                if letter.lower() != convert_word[-1]:
                    convert_word += letter.lower()
        if convert_word in ['help', 'asap', 'urgent']:
            return True

    test1 = marks_test(subj)
    if test1: return True

    test2, test3 = True, False

    text = subj.split()
    for word in text:
        test3 = words_test(word)
        if test3:
            return True
    if test2:
        return True
    return False


print(is_stressful("HOW ARE YOU?"))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
