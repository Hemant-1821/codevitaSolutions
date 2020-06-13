import sys

def rightShift(right_word):
    new = right_word[-1]+right_word[:-1]
    return new

def leftShift(left_word):
    new = left_word[1:]+left_word[0]
    return new

def isPal(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

for _ in range(int(input())):
    string = input()
    print
    left_word = right_word = string
    shifts = 0
    flag = True
    while shifts <= len(string)//2:
        if isPal(left_word) or isPal(right_word):
            print(shifts)
            flag = False
            break
        left_word = leftShift(left_word)
        right_word = rightShift(right_word)
        shifts += 1
    if flag:
        print('-1')