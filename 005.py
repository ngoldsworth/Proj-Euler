def is_div(n):
    for j in range(2,20):
        if n % j == 0:
            return True

for i in range(1,2000):
    primes_product=1*2*3*5*7*11*13*17*19
    num = i*primes_product
    if is_div(num):
        print(num)
        exit()
