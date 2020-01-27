
__author__ = 'roeiherz'


"""
Given a list of words, write a program to find the longest word made of other words.
Example: cat, banana, dog, nana, walk, walker, dogwalker -> dogwalker
"""


def split_word(word, A, prefix, new_set, original_word):
    """
    Here we calc all the permutations, hence, not efficient
    """
    # Stop if
    if prefix in A and word in A:
        new_set.add(prefix)
        return True

    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        new_prefix = prefix + word[i]
        if original_word != new_prefix and split_word(new_word, A, new_prefix, new_set, original_word):
            return True

    return False


def split_word_eff(word, A, original_word=False):
    # Stop if
    if word in A and not original_word:
        return True

    for i in range(len(word)):
        left = word[:i]
        right = word[i:]
        if split_word_eff(left, A) and split_word_eff(right, A):
            return True

    return False


def split_word_cnt_eff(word, A, sett, origin, original_word=False):
    """
    Adding sett mapping for counting
    :param word: string of the curr word
    :param A: array of words
    :param sett: adding the mapping
    :param origin: origin word string
    :param original_word: boolean flag
    :return:
    """
    # Stop if
    if word in A and not original_word:
        return True

    for i in range(len(word)):
        left = word[:i]
        right = word[i:]
        if split_word_cnt_eff(left, A, sett, origin) and split_word_cnt_eff(right, A, sett, origin):
            if origin not in sett:
                sett[origin] = set()

            sett[origin].add(left)
            sett[origin].add(right)
            return True

    return False


def longest_word(A):
    for i in range(len(A)):
        word = A[i]
        # sett = set()
        # if split_word(word, A, "", sett, original_word=word):
        #     print(word)
        if split_word_eff(word, A, original_word=True):
            print(word)
        # sett = {}
        # if split_word_cnt_eff(word, A, sett, origin=word, original_word=True):
        #     print(word)


if __name__ == '__main__':
    A = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
    # A = ['dogwalker', 'walk', 'dog', 'er']
    longest_word(A)
