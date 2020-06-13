import numpy as np

data =  np.genfromtxt('008.csv', delimiter=',')
maxprod = 1
for j in range(1000):
    prod = max(np.prod(data[j:j+12]), maxprod)
    print(maxprod)
