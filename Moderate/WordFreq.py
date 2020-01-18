__author__ = 'roeiherz'

"""
Design a method to find the frequency of occurrences of any given word in a book. 
What if we were running this algorithm multiplies times.
"""


def create_hashmap(book):
    hash_map = {}
    words = book.split(' ')
    for word in words:
        process_word = word.lower().replace(',', '').replace(".", "")
        if process_word in hash_map:
            hash_map[process_word] += 1
        else:
            hash_map[process_word] = 1
    return hash_map


def word_freq_multiplies(hash_map, word=''):
    """
    Keep dict of occurrences for each word
    """
    if word not in hash_map:
        return None

    return hash_map[word]


def word_freq_single(book, word=''):
    """
    O(n) to go all over the book
    """

    words = book.split(' ')
    tmp = 0
    for wordd in words:
        process_word = wordd.lower().replace(',', '').replace(".", "")
        if process_word == word:
            tmp += 1
    return tmp


if __name__ == '__main__':
    book = "hello world"
    hash_map = create_hashmap(book)
    word_freq_multiplies(hash_map, word='')
