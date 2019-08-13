import itertools


def check_palindromic(num: int):
    diglst = list(str(num))
    backlst = diglst[::-1]
    if backlst == diglst:
        return True
    else:
        return False


if __name__ == "__main__":
    numlst = list(range(100, 1000))
    pairs = list(itertools.combinations_with_replacement(numlst, 2))
    maxnum = 0
    for tup in pairs:
        num = tup[0] * tup[1]
        if check_palindromic(num):
            maxnum = max(num, maxnum)

    print(maxnum)
