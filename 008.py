import numpy as np

data =  np.genfromtxt('08.csv', delimiter=',')

for i in range(0, np.size(data)):
    prod = data[i]
    for j in range(1,12):
        prod = prod * data[i+j]



