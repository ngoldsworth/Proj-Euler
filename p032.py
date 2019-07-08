from itertools import product


def pandigit_check(a: int, b: int):
    """
    Testing to see if a, b, and a*b form a pandigital identity

    :param a, b: two integers being multiplied together and tested for a pandigital identity
    :return:
    """

    prod = a*b
    alist = list(str(a))
    blist = list(str(b))
    prodlist = list(str(prod))
    if len(alist) == len(set(alist)) and len(blist) == len(set(blist)) and len(prodlist) == len(set(prodlist)):
        if len(prodlist + alist + blist) == len(set(prodlist + alist + blist)):
            print(a, b)
            if any(i in alist for i in blist) == True:
                return False
            elif any(i in alist for i in prodlist) == True or any(i in blist for i in prodlist) == True:
                return False
            else:
                checklist = alist + blist + prodlist
                checklist = [int(num) for num in checklist]
                checklist.sort()
                if len(checklist) <= 8:
                    return False
                else:
                    if checklist == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        return True
                    else:
                        return False


panlist = []

for ex in range(2, 6):
    for i in range(2, 10**ex):
         for j in range(1, 10**(10 - ex)):
            # print(i, j)
            if pandigit_check(i, j):
                panlist.extend([i, j, i*j])
                print("SUCESS")

print(panlist)