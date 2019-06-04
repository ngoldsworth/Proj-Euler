# Trying to make a more efficient version of my solution to 12
from math import floor

def tri_generator(j):
    # makes a list of the first j triangular number
    trilist=[1]
    for i in range(2, j+1):
       trilist.append(trilist[-1] + i)
    return(trilist)

def countdivisors(num):
    # counts total number of divisors of a whole number
    # has possible off by one or two error
    count=0
    sqrt=num**(0.5)
    upperbound=int(floor(sqrt))
    for i in range(1, upperbound):
        if num % i == 0:
            count=count+1
    return(2*count)


bigtrilist = tri_generator(30000)

count=1
j=0
while count<=500:
    num = bigtrilist[j]
    count = countdivisors(num)
    print(j, num, count)
    j=j+1
