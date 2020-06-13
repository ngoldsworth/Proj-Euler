from primes.primelist import PrimesList
from math import ceil, sqrt


def is_prime(n:int):
    is_it_prime = True      # Boolean variable to hold whether n is prime or not
                            # n is assumed prime until proven otherwise

    root = ceil(sqrt(n))    # if a number isn't prime, it has factors both above and below its square root

    for j in range(2,root+1): # start at 2, since every number is divisible by 1
        if n % j == 0:      # if j divides evenly into n, then n is not prime
            is_it_prime = False
            break           # Don't need to test more now that we know n is not prime

    return is_it_prime


def largest_prime_factor(num: int):
    if not isinstance(num, int):
        raise TypeError('Need an integer, you dimwit')
    found_largest_prime_factor = False # Haven't found a prime factor of num, until we do
    i = 1       # start at i=1, that way if num/1 is a factor, then we know it is its own largest prime factor
    while not found_largest_prime_factor:
        if int(num/i) == num/i and is_prime(int(num/i)):
            return int(num/i)
        elif i >= num:
            raise ValueError('You broke math. Somehow `num` has no prime factors and is not prime')
        i += 1

