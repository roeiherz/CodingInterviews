__author__ = 'roeiherz'


def URLify(x, n):
    """"
    input: "Mr John Smith   ", 13
    output: "Mr%20John%20Smith"
    """
    # not inplace
    new_x = []
    for c in x:
        if c == ' ':
            new_x.append('%20')
        else:
            new_x.append(c)

    new_x = new_x[:n]
    print ''.join(new_x)

    # not inplace 2
    arr = [chunk for chunk in x.split(' ') if chunk != '']
    print '%20'.join(arr)


if __name__ == '__main__':
    "Write a method to replace all spaces in a string '%20'. You are given the 'true' length of the string"
    URLify("Mr John Smith   ", 13)
