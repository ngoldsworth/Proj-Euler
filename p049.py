from primes.primelist import PrimesList
from itertools import permutations
from itertools import combinations


def find_prime_permus(num:int, primelist: list):
    charlist = list(str(num))
    permus = permutations(charlist, len(charlist))
    permlist = []
    for perm in permus:
        string = ''
        for char in perm:
            string = string + char
        newnum = int(string)
        permlist.append(newnum)

    primepermulst = []
    for p in permlist:
        if p in primelist:
            primepermulst.append(p)

    return sorted(primepermulst)


def intstrlen(num: int):
    return int(len(list(str(num))))


def find_arithmetic_triplet(numlist:list):
    arithlist = []
    for cm in combinations(numlist, 3):
        cm = sorted(cm)
        if cm[2] - cm[1] == cm[1] - cm[0] and cm[0] != cm[1] and cm[2] != cm[1] and cm[0] != cm[2]:
            arithlist.append( (cm[0], cm[1], cm[2]))

    return arithlist

def check_digits(num, digs):
    numstrlen = len(list(str(num)))
    return digs == numstrlen


if __name__ == '__main__':
    pl0 = list(PrimesList(10**5).list)
    pl = [prime for prime in pl0 if check_digits(prime, 4)]
    arithprimeslist = []
    for i in pl:
        ppl = find_prime_permus(i, pl)
        z = find_arithmetic_triplet(ppl)
        if len(z) != 0:
            tup = z[0]
            if intstrlen(tup[0]) == intstrlen(tup[1]) and intstrlen(tup[1]) == intstrlen(tup[2]):
                arithprimeslist.append(tup)

    arithprimeslist = list(set(arithprimeslist))
    for i in arithprimeslist:
        print(''.join([str(k) for k in i]))







