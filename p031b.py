coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = sorted(coins, reverse=True)


def sum_test(sourcelist, i, originlist):
    if sum(originlist) == 200:
        # print(originlist)
        return(originlist)
    elif sum(originlist) < 200:
        quant = len(sourcelist)
        for j in range(i, quant):
            newlist = [ *originlist, sourcelist[j]]
            sum_test(sourcelist, j, newlist)


firstlist = []
biglist = []

for i in range(len(coins)):
    biglist.append(sum_test(coins, i, firstlist))

biglist = list(set(biglist))
print(len(biglist))

