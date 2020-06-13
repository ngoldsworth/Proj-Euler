import math

def triangular(n):
    return int(n*(n+1)/2)

def pentagonal(n):
    return int(
        n*(3*n -1) / 2
    )

def hexagonal(n):
    return int(
        2*n**2 - n
    )

def upper_indices_from_max_number(m):
    """
    Given the number `m`,
    find the index of the highest number in the triangular, pentagonal, and hexagonal sequences that is less than `m`
    :param m:
    :return: triangular_max, pent_max, hex_max
    """
    tri_max = math.floor((1/2) * (math.sqrt(8*m + 1) - 1))
    pent_max = math.floor((1/6) * (math.sqrt(24*m + 1) + 1))
    hex_max = math.floor((1/4) * (math.sqrt(8*m + 1) + 1))
    return tri_max, pent_max, hex_max

def create_num_lists(max_num):
    tm, pm, hm = upper_indices_from_max_number(max_num)
    trilst = [triangular(j+1) for j in range(tm)]
    pentlst = [pentagonal(j+1) for j in range(pm)]
    hexlst = [hexagonal(j+1) for j in range(hm)]
    return trilst, pentlst, hexlst



if __name__ == '__main__':
    upper_bound = 10**12
    t, p, h = create_num_lists(upper_bound)

    # intersection of pents and hexs
    intersection = list( set(p) & set(h) & set(t))
    print(intersection)
