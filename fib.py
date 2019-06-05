import numpy as np

def nth_fibo(n):
    fibo=np.array([0,1])
    #print(fibo[0])
    #print(fibo[1])
    for i in range(n):
        fibi = fibo[-1] + fibo[-2]
    #    print(fibi)
        fibo=np.append(fibo, [fibi])
    return fibo[-1]

#print(nth_fibo(50))
#print(nth_fibo(2))

@memoize
def recur_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

print(recur_fibo(1000))
