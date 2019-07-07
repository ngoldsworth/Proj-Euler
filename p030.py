
def find_power_sum(num: int, pwr: int):
    if num == 1:
        powersum = 0
    else:
        diglist = list(str(num))
        powersum = sum([int(dig) ** pwr for dig in diglist])
    return(powersum)

tot = 0
for num in range(500000):
    if num == find_power_sum(num, 5):
        tot = tot + num
        print(tot)
    # else:
    #     print('Oops ' + str(num) + ' not good')


