__author__ = 'roeiherz'

"""
Given a list of people with their birth and death years, implement a method to compute the year with the most number
of people alive. You may assume that all people were born between 1900 and 2000 (inclusive). 
If a person was a alive during any portion of that year, they should be included in that year's count. 
For example, person (birth=1908, death=1909) is included in the counts for both 1908 and 1909.
"""


def compute(people):
    """
    O(P * Y + Y)
    """
    # Create hash map
    years = {k: 0 for k in range(1900, 2001)}

    for person in people:
        start_year = person[0]
        end_year = person[1]
        for year in range(start_year, end_year + 1):
            years[year] += 1

    max_death = 0
    max_year = 0
    for k, v in years.items():
        if v > max_death:
            max_death = v
            max_year = k
    print("Max year {} with only {} death".format(max_year, max_death))


def compute_eff(people):
    """
    """
    A = sorted([person[0] for person in people])
    B = sorted([person[1]+1 for person in people])

    n = len(A)
    birth = 0
    death = 0
    alive = 0
    year_alive = 0
    max_alive = 0
    while birth < n and death < n:

        if A[birth] == B[death]:
            birth += 1
            death += 1
            if max_alive < alive:
                max_alive = alive
                year_alive = A[birth-1]

        elif A[birth] < B[death]:
            alive += 1
            birth += 1
            if max_alive < alive:
                max_alive = alive
                year_alive = A[birth-1]
        else:
            death += 1
            alive -= 1

    print("Max year {}".format(year_alive))


if __name__ == '__main__':
    people = [(1920, 1940), (1908, 1909), (1903, 1920), (1928, 1945)]
    people = [(12, 15), (20, 90), (10, 98), (23, 82), (13, 98), (90, 98), (83, 99), (75, 94)]
    # compute(people)
    compute_eff(people)
