# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(N):
    # write your code in Python 3.6

    str_n = str(N)
    length = len(str_n)

    digit_count = {}

    for number in str_n:
        if number in digit_count:
            digit_count[number] += 1
        else:
            digit_count[number] = 1

    zeros = 0

    if '0' in digit_count.keys():
        zeros = digit_count['0']

    numerator = (length - zeros) * math.factorial(length - 1)

    denominator = 1
    for digit in digit_count.keys():
        if digit_count[digit] > 1:
            denominator *= math.factorial(digit_count[digit])

    combinations = numerator // denominator

    return combinations


user_number = input("Enter a number: ")
print("Combinations: {0}".format(solution(user_number)))
