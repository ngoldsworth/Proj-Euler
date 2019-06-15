#!/usr/bin/env python3
import typing as t
import numpy as np



def val(array: np.ndarray, point: t.Tuple):
    if point[0] < 0 or point[1] < 0 or point[0] >= array.shape[0] or point[1] >= array.shape[1]:
        return 0
    else:
        return array[point]


def tree_decision(data: np.ndarray, intupl: t.Tuple):
    i = intupl[0]
    j = intupl[-1]
    if val(data, (i-1, j-1) ) > val(data, (i-1, j) ):
        return (i-1, j-1)
    elif val(data, (i-1, j-1) ) < val(data, (i-1, j) ):
        return(i-1, j)
    else: # the tree points to numbers of equal value
        treelist = [ val(data, (i-2, j-2) ), val(data, (i-2, j-1) ), val(data, (i-2, j) )]
        if max(treelist) == val(data, (i-2, j-2) ):
            return (i-1, j-1)
        else:
            return (i-1, j)

def reverse_brancher(array: np.ndarray, point: t.Tuple):
    if point[0] < 0  or point[1] < 0 or point[0] >= array.shape[0] or point[1] >= array.shape[1]:
        return str('Starting point is outside the array, which is not allowed')
    else:
        cont = True
        vallist = []
        while cont == True:
            vallist.append(val(array, point))
            if point == (0, 0):
                cont = False
            else:
                point = tree_decision(array, point)
        return vallist


def max_finder(array: np.ndarray):
    final_row = array.shape[0] - 1
    width = array.shape[1]
    max_branch_sum = 0
    for i in range(width):
        startpoint = (final_row, i)
        vallist = reverse_brancher(array, startpoint)
        new_sum = sum(vallist)
        print(new_sum, vallist)
        max_branch_sum = max(max_branch_sum, new_sum)
    return (max_branch_sum, vallist)


bigdata = np.genfromtxt('018b.csv', delimiter=',')

print(max_finder(bigdata))




