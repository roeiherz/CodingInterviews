__author__ = 'roeiherz'

"""
Given any int, print an english phrase that describes the int (e.g., "One thousand, two hundred thirty four)
"""


def counter(tmp):
    cnt = 0
    while tmp > 1:
        tmp /= 10.0
        cnt += 1
    return cnt


def english_int(x):
    digits = counter(x)
    arr = [d for d in str(x)]
    # Hundreds
    if digits < 3:
        print("")

    for i in range(digits):

        pass



if __name__ == '__main__':
    x = 500
    english_int(x)
