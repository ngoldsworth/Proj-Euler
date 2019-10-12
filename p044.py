from itertools import combinations as combos
import numpy as np


def pentagonal(n):
    return (n*((3*n)-1)/2)

# def pentagonal_list(num):
#     return [pentagonal(j) for j in range(1, num+1)]

if __name__ == '__main__':
    upper_index_bound = 2000
    indices_list = []
    for pair in combos(range(1, upper_index_bound), 2):
        indices_list.append((pair[0], pair[1], abs(pair[0] - pair[1])))
    numpairs = len(indices_list)

    pentaglist = [pentagonal(j) for j in range(1, upper_index_bound)]
    refined_pentagonals = [] # List that will contain pairs of pentagonal numbers that satisfy said criteria

    pentarr = np.zeros((3, numpairs), dtype=int)
    for j in range(numpairs):
        tup = indices_list[j]
        pentarr[0,j] = tup[0]
        pentarr[1,j] = tup[1]
        pentarr[2,j] = tup[2]

    # sort by the pentagonal number index difference
    pentarr = pentarr[:, pentarr[2].argsort()]

    found = False
    j = 0
    print(pentaglist)
    while not found:
        col = pentarr[:,j]
        pk = pentagonal(col[0])
        pj = pentagonal(col[1])
        added = pk + pj
        diff = abs(pk - pj)
        if added in pentaglist and diff in pentaglist:
            found = True
            ans = (pk, pj)
        else:
            j += 1










