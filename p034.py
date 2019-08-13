#!/usr/bin/env python3

from math import factorial as fact

def digit_factorial_sum(num: int):
    num = int(num)
    numlist = list(str(num))
    tot = 0
    for d in numlist:
        tot =  tot + fact(int(d))

    return tot

if __name__ == "__main__":
    pass_list = []
    for num in range(3,10**8):
        if num == digit_factorial_sum(num):
            print(num, num/10**8 * 100)
            pass_list.append(num)


    print(pass_list)
