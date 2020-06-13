from p021 import divsum
import itertools

def det_abundant(num: int):
    '''
    Determine if a number `n` is an `abundant` number.
    :param num: Input integer
    :return: True or False
    '''
    for i in range(num + 1):
        if divsum(num) > num:
            return True
        else:
            return False

# Generate list of abundant numbers less than 28123

abundants = []

for num in range(1, 28123):
    if det_abundant(num) == True:
        abundants.append(num)

print(len(abundants))
combos = itertools.combinations_with_replacement(abundants, 2)

ilist = list(range(1, 28123))
maxint = max(ilist)

for pair in combos:
    n = sum(pair)
    if n < maxint and n in ilist: ilist.remove(n)

print(sum(ilist))

