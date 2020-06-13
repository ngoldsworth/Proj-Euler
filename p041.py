import numpy as np


def string_to_chars(string: str):
    return [char for char in string]


def check_pandigital(number: int):
    """
    Check if the input number is pandigital. IE, a five-digit number uses 1, 2, 3, 4, 5.
    An 8 digit number uses 1, 2, 3, 4, 5, 6, 7, 8.
    :param number: The number to check
    :return: Boolean. If the number is pandigital, returns True, else False.
    """
    digitlist = [int(j) for j in sorted(string_to_chars(str(number)))]
    if digitlist == sorted(list(range(1, len(digitlist)+1))):
        return True
    else:
        return False

def find_first_pandigital(arr: np.ndarray):
    '''
    Given an array of integers, find and return the first pandigital number in the array
    :param arr: 1-dimensional array of numbers
    :return: the first pandigital integer in the array
    '''

    j = 0
    found_a_pandigital = False
    first_pandigital = None
    while not found_a_pandigital:
        if check_pandigital(arr[j]):
            first_pandigital = arr[j]
            found_a_pandigital = True
        elif j+1 >= arr.size:
            found_a_pandigital = True
            first_pandigital = None
        else:
            j += 1
            print(j)

    return first_pandigital


if __name__ == '__main__':
    from primes import primelist
    max_num_to_consider = 987654321
    plist = primelist.PrimesList(max_num_to_consider).list
    # Rather than checking each prime up to the max considered number, find the first
    # pandigital by starting at max and going down the list
    rev_plist = plist[::-1]
    biggest_pandigital_prime = find_first_pandigital(rev_plist)
    print(biggest_pandigital_prime)


