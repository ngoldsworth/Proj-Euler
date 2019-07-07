import typing as t

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = sorted(coins, reverse=True)


def sum_test(sourcelist, i,  inputlist):
    init_tot = sum(inputlist)
    if init_tot == 200:
        print(inputlist)
        return True
    elif init_tot > 200:
        return False
    else:
        quant = len(sourcelist)
        for j in range(i, quant):
            newlist = inputlist.append(sourcelist[j])
            sum_test(sourcelist, j, newlist)


firstlist = [0, 0, 0, 0, 0]

for i in range(len(coins)):
    sum_test(coins, 0, firstlist)
