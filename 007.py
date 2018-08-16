import math
import time
start_time = time.time()
def is_prime(n):
    for j in range(3, n):
        if n % j == 0:  # aritmetic calculations
            return False
    return True

primes = []  # initialize a list of prines collected.
x = 10001
n = 2

while len(primes) !=x+1: # is the nth number on the list yet? +1 because array starts at zero
    if is_prime(n):
        primes.append(n) # adds that prime number to the listi
    n+=1 # increment to the next number

print("--- %s seconds ---" % (time.time() - start_time))
print(primes[-1])
