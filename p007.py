import math
import time
from p003 import is_prime

if __name__ == '__main__':
    start_time = time.time()

    primes = [2]  # initialize a list of prines collected. Start with first prime is 2
    x = 10001  # want to find the xth prime
    n = 3   # start at this

    while len(primes) < x:   # is the nth number on the list yet? +1 because array starts at zero
        if is_prime(n):
            primes.append(n)   # adds that prime number to the list
        n+=1 # increment to the next number

    print("--- %s seconds ---" % (time.time() - start_time))
    print(primes[-1])
