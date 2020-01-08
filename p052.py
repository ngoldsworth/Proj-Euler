def same_digits_check(numlist: list):
    '''

    :param numlist: List of integers
    :return: Bool, True if all ints in `numlist` have exactly same digits, just in different order
    '''
    sortedlist = [int(''.join(sorted(list(str(x))))) for x in numlist]
    if len(set(sortedlist)) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    import math
    for j in range(1, math.ceil(999999/6)+1):
        numlist = [j*k for k in [1, 2, 3, 4, 5, 6]]
        if same_digits_check(numlist):
            print(numlist)



