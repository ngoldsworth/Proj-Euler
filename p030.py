
def find_power_sum(num: int, pwr: int):
    diglist = list(str(num))
    powersum = sum([int(dig) ** pwr for dig in diglist])
    return(powersum)

tot = 0
for num in range(10000):
    if num == find_power_sum(num, 4):
        tot = tot + num
        print(tot)
    # else:
    #     print('Oops ' + str(num) + ' not good')
