from p021 import divlist as dl
from itertools import permutations as perm
import numpy as np

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def pandigit_identity_check(sequence):
    # make list to store matches in
    pandigit_list = []

    # Check if A * BCDE == FGHI
    a = sequence[0]

    b = sequence[1] * 1000
    c = sequence[2] * 100
    d = sequence[3] * 10
    e = sequence[4] * 1

    f = sequence[5] * 1000
    g = sequence[6] * 100
    h = sequence[7] * 10
    i = sequence[8] * 1

    num1 = a
    num2 = b + c + d + e
    num3 = f + g + h + i
    if num1 * num2 == num3:
        pandigit_list.append(num1)
        pandigit_list.append(num2)
        pandigit_list.append(num3)

    # Check if JK * LMN = PQRS
    j = sequence[0] * 10
    k = sequence[1] * 1

    l = sequence[2] * 100
    m = sequence[3] * 10
    n = sequence[4] * 1

    p = sequence[5] * 1000
    q = sequence[6] * 100
    r = sequence[7] * 10
    s = sequence[8] * 1

    num4 = j + k
    num5 = l + m + n
    num6 = p + q + r + s

    if num4 * num5 == num6:
        pandigit_list.append(num4)
        pandigit_list.append(num5)
        pandigit_list.append(num6)

    return pandigit_list

permutations = list(perm(digits))

panlist = []
for tup in permutations:
    panlist.extend(pandigit_identity_check(tup))
print(panlist)
print(sum(list(set(panlist))))
