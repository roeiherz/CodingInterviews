__author__ = 'roeiherz'

"""
You are given two arrays, one shorter (with all distinct elements) and one longer. 
Find the shortest subarray in the longer array that contains all the elements in the shorter array.
The items can appear in any order.
Example: [1,5,9], [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7] -> [7,10] (5,7,9,1)
"""


def get_instances(arr):
    mapp = {}
    for x in arr:
        if x in mapp:
            mapp[x] += 1
        else:
            mapp[x] = 1
    return mapp


def shortest_seq(S, L):

    ind = 0
    inst = get_instances(S)
    min_dist = len(L) + 1
    indices = []
    start_ind = -1
    end_ind = -1
    while ind < len(L):
        candidate = L[ind]
        if candidate in S and inst[candidate] > 0:
            inst[candidate] -= 1
            indices.append(ind)

        # Find all num in S; need to init
        if sum(inst.values()) == 0:
            dist = max(indices) - min(indices) + 1
            if min_dist > dist:
                min_dist = dist
                start_ind = min(indices)
                end_ind = max(indices)
            indices = []
            inst = get_instances(S)

        ind += 1

    print("Start index: {}, end index: {}, arr: {}".format(start_ind, end_ind, L[start_ind:end_ind+1]))
    return


if __name__ == '__main__':
    short = [1, 5, 9]
    long = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    shortest_seq(short, long)
