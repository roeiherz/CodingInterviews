__author__ = 'roeiherz'

"""
Given two words of equal length that are in a dict, write a method to transform one word into another word by 
changing only one letter at a time. The new word you get in each step must be in the dict.
Example: DAMP, LIKE : DAMP -> LAMP -> LIMP -> LIME -> LIKE
"""


def create_wild_card(words):

    mapp = {}
    for word in words:
        for i in range(len(word)):
            wild_card = word[:i] + "*" + word[i + 1:]

            candidates = []
            for i in range(97, 123):
                ch = chr(i)
                candidate = wild_card.replace('*', ch)
                if candidate in words:
                    candidates.append(candidate)

            mapp[wild_card] = candidates

    return mapp


def word_transformer(curr_word, end_word, wild_cards, visited):

    if curr_word == end_word:
        visited.append(curr_word)
        return visited

    if curr_word in visited:
        return None

    # Append
    visited.append(curr_word)

    for i in range(len(curr_word)):
        wild_card = curr_word[:i] + "*" + curr_word[i + 1:]
        new_words = wild_cards[wild_card]
        for new_word in new_words:
            res = word_transformer(new_word, end_word, wild_cards, visited)
            if res is not None:
                return visited

    return None


if __name__ == '__main__':
    start_word = 'DAMP'
    end_word = "LIKE"
    words = ["DAMP", "LAMP", "LIMP", "LIME", "LIKE"]

    if end_word not in words:
        print("The end word is not in dict")
        exit()

    # Lower case
    start_word = start_word.lower()
    end_word = end_word.lower()
    words = [word.lower() for word in words]

    # Preprocess
    wild_cards = create_wild_card(words)
    visited = []

    # Main
    res = word_transformer(start_word, end_word, wild_cards, visited)
    if res is None:
        print("None")
    else:
        # Upper case
        visited = [visit.upper() for visit in visited]
        print(visited)
