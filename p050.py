from primes.primelist import PrimesList

def prime_series_sum(plist, jstart, maxnum):
    """

    :param plist: The list of prime numbers
    :param jstart: Index of number to start with
    :param maxnum:
    :return: The largest prime number less than maxnum possibly produced by adding all consecutive numbers in plist
            after and including plist[jstart]
    """
    # when no numbers have yet been considered, the series sums to zero
    sum = 0
    maxprime = None
    maxrange = None
    j = 0
    while sum <= maxnum:
        sum += plist[jstart + j]
        if sum in plist and sum <= maxnum:
            maxprime = sum
            maxrange = (jstart, jstart + j)

        j += 1

    return maxprime, maxrange


if __name__ == '__main__':
    upper_bound = 10**4
    plist = list(PrimesList(upper_bound).list)
    max_range = (0, 0)
    max_range_prime = 0
    for j in range(len(plist)):
        a, b = prime_series_sum(plist, j, upper_bound)
        if a != None:
            if b[1] - b[0] > max_range[1] - max_range[0]:
                max_range = b
                max_range_prime = a

    print(max_range, max_range_prime)




