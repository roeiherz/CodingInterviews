__author__ = 'roeiherz'

"""
A circus is designing a tower routine consisting of people standing atop one another's shoulders.
For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
Given the heights and weights of each person in the circus, write a method to compute the largest possible number of
people in such a tower.  
Example: (ht,wt) [(65,100), (70, 150), (56,90), (75,190), (60,95), (68, 110)] -> 
length 6: (56, 90), (60,95), (65,100), (68, 110), (70, 150), (75, 190)
"""


def circus_tower(A):
    h = sorted(A, key=lambda x: x[0])

    lst = []
    for i in range(len(h)-1):
        if h[i][1] < h[i+1][1]:
            lst.append(h[i])
            if i == len(h)-2:
                lst.append(h[i+1])
    return lst


if __name__ == '__main__':
    A = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    print(circus_tower(A))
