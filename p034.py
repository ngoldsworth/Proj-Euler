#!/usr/bin/env python3

from math import factorial as fact

def digit_factorial_sum(num: int):
    num = int(num)
    numlist = list(str(num))
    tot = 0
    for d in numlist:
        tot =  tot + fact(int(d))

    return tot



print(digit_factorial_sum(999))

pass_list = []
for num in range(3,200):
    if num == digit_factorial_sum(num):
        pass_list.append(num)

print(pass_list)
