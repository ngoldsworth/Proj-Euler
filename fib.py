import numpy as np

def nth_fibo(n):
    fibo=np.array([0,1])
    print(fibo[0])
    print(fibo[1])
    for i in range(n):
        fibi = fibo[-1] + fibo[-2]
        print(fibi)
        fibo=np.append(fibo, [fibi])
    return fibo[-1]

print(nth_fibo(50))
print(nth_fibo(2))
