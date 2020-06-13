#
# PROBLEM STATEMENT
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
import numpy as np
from primes.primelist import PrimesList


def times_divisor(number, divisor):
    """
    How many times does `divisor` evenly divide into `number`.
    For example:
        2 evenly divides 8 thrice.
        5 evenly divides 100 twice
        6 evenly divides 30 once.
        10 evenly divides 100 twice.
        10 evenly divides 1000 thrice.
    :param divisor:
    :param number:
    :return: The number of times, as an integer, that `divisor` evenly goes into `number`
    """
    times = 0   # doesnt divide evenly until we test and it does
    proceed = True # variable as flag to keep going
    while proceed:
        if number % divisor == 0:
            times += 1 # add one to the number of times divisor evenly goes into number
            number = number/divisor # pair down so the next iteration tests next relationship
        else:
            proceed = False
            # Break the loop

    return times


def least_common_multiple(numlist: list):
    """
    Find the least common multiple of a list of numbers, assuming all the integers in the given
    list are greater than one.
    If 1 or 0 are included in `numlist` they are removed.
    If integers less than zero are included, a value error is raise

    :param numlist: List of integers, each greater than one
    :return:  the least common multiple of all integers in `numlist`, as an integer
    """
    plist = list(PrimesList(max(numlist)).list)

    # DATA STRELIZATION: it is pointless to find the least common multiple of 1 and other numbers,
    # as it will just beat the least common multiple of the same list of numbers without 1
    if 1 in numlist:
        numlist = [i for i in numlist if i != 1]
    # The least common multiple of zero and any other set of numbers is zero,
    # since zero times anything is zero
    if 0 in numlist:
        numlist = [i for i in numlist if i != 0]
    # We want only positive integers. We count the number of negative numbers
    # and raise a ValueError if our count is larger than 0
    if sum(1 for i in numlist if i < 0) > 0:
        raise ValueError('List of integers contains negatives. Only positive integers allowed')

    # Create an array to store the prime-factorizations in
    # The first dimension is for each number in `numlist`
    # the second dimension is for each possible prime factor in `plist`
    prime_factor_counts = np.zeros((len(numlist), len(plist)))
    for num in numlist:
        print(num)
        powers_factor_list = []
        # Create a list that stores the number of times each prime evenly divides into `num`
        # For example, `powers_factor_list[0]` is the number of times the [0]th prime evenly
        # divides into num. `powers_factor_list[1]` is the number of times the [1]th prime
        # evenly divides into `num`. And so on.
        for p in plist:
            powers_factor_list.append(times_divisor(num, p))
        prime_factor_counts[numlist.index(num), :] = np.array(powers_factor_list)

    lcm = 1
    for j in range(len(plist)):
        lcm *= plist[j]**(max(prime_factor_counts[:,j]))

    return int(lcm)




if __name__ == '__main__':
    nums = list(range(21))
    print(max(nums))
    print(least_common_multiple(nums))

