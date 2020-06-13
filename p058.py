from primes.primelist import PrimesList


def corners(n:int):
    if n == 1:
        raise ValueError('Square containing only 1 does not have corners')
    if n % 2 == 0:
        raise ValueError('Side length will always be odd in this problem')
    corners = []
    max_corner = n**2
    for j in range(4):
        corners.append(max_corner - j*(n-1))
    return corners


def intersection(A, B):
    return list(set(A) & set(B))


def count_prime(numlist:list, primes):
    if not primes:
        primes = PrimesList(max(numlist)+1).list

    return len(intersection(numlist, primes))


if __name__ == '__main__':
    j = 3      # start with a 3x3 square, going from 1 to 9 in spiral
    ratio = 1  # Assume all corners are primes at start
    cornlst = []
    primelist = list(PrimesList(101 ** 2 + 1).list)
    while ratio >= .1:
        cornlst.extend(corners(j))
        ratio = count_prime(cornlst, primelist)/len(cornlst)
        print(ratio)
        j += 2

    print(j)



