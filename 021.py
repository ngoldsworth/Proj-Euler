#!/usr/bin/env python3

from math import sqrt

def divlist(num: int):
    div_list = [1]
    upper = int(sqrt(num) + 1)
    for i in range(2, upper):
        if num % i == 0:
            div_list.append(int(i))
            if int(num / i) != int(i) and num != int(num/i):
                div_list.append(int(num/i))
    return div_list

def divsum(num: int):
    a = list(set(divlist(num)))
    b = sum(a)
    return b

def amicabletest(num: int):
    s1 = divsum(num)
    s2 = divsum(s1)
    if s2 == num:
        return True
    else:
        return False

def amicable_list(num: int):
    am_list = []
    for i in range(2, num+1):
        if amicabletest(i) == True:
            am_list.append(i)
    return am_list

print(amicabletest(10000))
print(amicable_list(10000))
print(sum(amicable_list(10000)))

