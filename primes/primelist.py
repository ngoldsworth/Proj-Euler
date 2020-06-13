import numpy as np
from math import ceil


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


class PrimesList():

    def __init__(self, num):
        self.list = primesfrom2to(num)

    def nthprime(self, n):
        """
        Find the vale of the nth prime
        :param n:
        :return: value of the `n`th prime.
        """
        num = self.list[n-1]
        return num

    def less_than(self, num):
        # THIS MIGHT NOT ACTUALLY BE ALL THAT USEFUL
        """

        :param num:
        :return: List of all primes strictly less than `num`, exclusive of `num` should it be prime
        """
        # create index for place to cut in half
        midl =  ceil(self.list.size() * 0.5)
        low = 0
        high = self.list.size() - 1
        while high - low > 5:
            if num < self.list[midl]:
                low = low
                high = midl
                midl = ceil((midl - low) * 0.5)
            elif num > self.list[midl]:
                low = midl
                high = high
                midl = ceil((high - midl) *0.5)
            elif num == self.list[midl]:
                indx = midl - 1 # since want all exclusively less than num
            else:
                break

        for i in self.list[low:high]:
            if self.list[i] < num and num < self.list[i+1]:
                indx = i

        less_than_list = self.list[:indx]
        return less_than_list

    def is_prime(self, n):
        """
        For a given n, is n prime?
        :param n: Number to test for prime
        :return: Boolean, True if n is prime, False if n is not prime
        """
        if n in self.list:
            return True
        else:
            return False


def prime_factors_of(num, primelist=None):
    '''
    Find the prime factors of a given number
    :param num: the number to find prime factors of
    :param primelist: optional argument, assumes providing a list of at least all prime numbers
     less than `num`. Use this to only generate one primeslist externally, as opposed
     to generating a new list of primes each time this function is called
    :return: list of prime factors of `num`
    '''
    if not primelist:
        # If no primelist is given in the function input,
        # generate a list of all prime numbers less than or equal to `num`
        primelist = PrimesList(num)

    # List for storing prime factors
    prime_factors = []
    for p in primelist:
        # If p is a factor of `num`, append it to the lis
        if num % p == 0:
            prime_factors.append(p)

    # Return the list of prime factors
    return prime_factors
