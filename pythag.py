from primes.primelist import PrimesList
from math import gcd
import math

def is_square(num:int):
    if int(math.floor(math.sqrt(num))**2) == num:
        return True
    else:
        return False

def pythag_triples_under(upper_c):
    trips = []
    upper_c = 10000
    plist = list(PrimesList(upper_c+1).list)
    for c in range(1,upper_c+1):
        c2 = c**2
        for b in [b for b in plist if b < c]:
            a2 = c2 - b**2
            if a2 > 0:
                if is_square(a2):
                    a = int(a2**.5)
                    trips.append(tuple(sorted((a, b, c))))
    if len(trips) == 0:
        return None
    else:
        return trips


def gcdn(numlist: list):
    gcd_slice = []
    count = len(numlist)
    if count == 1:
        return numlist[0]
    elif count % 2 != 0:
        gcd_slice.append(numlist[-1])
        numlist = numlist[0:-1]
    for j in range(int(len(numlist)/2)):
        gcd_slice.append(gcd( numlist[2*j], numlist[(2*j)+1] ))
    return gcdn(gcd_slice)


def reduce_tuple_to_prime(tup:tuple):
    divisor = gcdn(list(tup))
    return tuple([int(j/divisor) for j in tup])




def normalize(tup:tuple):
    norm = sum([i**2 for i in tup])
    return tuple([j/norm for j in tup])

if __name__ == '__main__':
    import time
    start = time.time()

    upper_limit = 3000
    trips = []
    for a in range(1, upper_limit):
        for b in range(1, upper_limit):
            c2 =a**2 + b**2
            if is_square(c2):
                c = int(math.sqrt(c2))
                trips.append(reduce_tuple_to_prime((a, b, c)))
    print(len(set(trips)))

    # print(pythag_triples_under(1500))

    print(" --- %s seconds ---" % (time.time() - start))


