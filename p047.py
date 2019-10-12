import primes.primelist


def prime_factors(num: int, primeslist: list):
    if num == 0 or  num == 1:
        return []

    j = 0
    pfactors = []

    while num != 1:
        if num % primeslist[j] == 0:
            pfactors.append(primeslist[j])
            num = num / primeslist[j]
        else:
            j += 1

    return pfactors


def test_distinct(set_list: list):
    distinct = True
    set0 = set_list[0]
    for setj in set_list[1:]:
        if (set0 & setj) == set():
             set0 = set0 | setj
        else:
            distinct = False
    return distinct


if __name__ == '__main__':
    import numpy as np

    primeslist = list(primes.primelist.PrimesList(10**6).list)
    upper_bound = 100 #**4
    arr = np.zeros(upper_bound, dtype=object)
    for j in range(upper_bound):
        arr[j] = prime_factors(j, primeslist)

    seq_count = 2
    for j in range(0, 1 + upper_bound - seq_count):
        set_list = [set(arr[j+k]) for k in range(seq_count)]
        print(set_list)



