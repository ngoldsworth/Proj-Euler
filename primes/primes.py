import numpy
from pathlib import Path as plp


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

if __name__ == "__main__":
    z = primesfrom2to(10**9)
    fn = plp('/home/nelson/projeuler/primes/primes.bin')
    z.tofile('/home/nelson/projeuler/primes/primes.bin')
