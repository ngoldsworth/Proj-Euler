from eulerlib import prime

num = 600851475143
#num = 13195 # test

pArray=prime(10000)

for i in range(1, len(pArray)):
    divisor=pArray(-i)
    factor = num/i
    if num % i == 0:
        if is_prime(factor):
            print(i, factor, i*factor)
            exit()
