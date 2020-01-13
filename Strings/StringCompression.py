__author__ = 'roeiherz'

"""
Implement a method to perform basic string compression using the counts of repeated chars.
If the "compressed" string would not become smaller than the original string, your method should return the original
string. You can assume the string has only uppercase and lowercase letters (a to z).
example: 'aabcccccaaa' -> a2b1c5a3
"""


def string_compression(x):
    """
    :param x: string
    :return:
    """

    cnt = 1
    # Instead of append, we can find the size of the array first, and then append
    new_str = []
    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            cnt += 1
        else:
            new_str.append("{c}{n}".format(c=x[i - 1], n=cnt))
            cnt = 1

    # Append the last counting
    new_str.append("{c}{n}".format(c=x[i - 1], n=cnt))
    return ''.join(new_str)


if __name__ == '__main__':
    print(string_compression('aabcccccaaa'))
