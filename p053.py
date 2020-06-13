from math import factorial as fact

def nCr(n, r):
    if n < r:
        return 0
    else:
        numerator = fact(n)
        denominator = fact(r) * fact(n-r)
        return int(numerator/denominator)

if __name__ == '__main__':
    list_of_greater_than_million = []
    for n in range(1, 100 + 1):
        for r in range(0, n+1):
            num = nCr(n, r)
            if num > 10**6:
                list_of_greater_than_million.append(num)

    print(len(list_of_greater_than_million))

