__author__ = 'roeiherz'

"""
You have a large text file containing words. Given any two words, find the shortest distance 
(in terms of number of words) between them in the file. If the operation will be repeated many times
for the same file (but different pairs of words), can you optimize your solution?
"""


def create_map(text):
    mapp = {}
    words = text.replace(',', '').replace('.', '').split(' ')
    for i in range(len(words)):
        word = words[i]
        if word in mapp:
            mapp[word].append(i)
        else:
            mapp[word] = [i]

    return mapp


def word_distance(text, word_a, word_b):
    mapp = create_map(text)
    lst_a = mapp[word_a]
    lst_b = mapp[word_b]
    distance = min(max(lst_a) - min(lst_b), max(lst_b) - min(lst_a))
    print("Distance: {}".format(distance))


if __name__ == '__main__':
    text = "hello world, I'm Roei a senior researcher in the world which is a senior"
    word_a = 'world'
    word_b = 'senior'
    word_distance(text, word_a, word_b)
