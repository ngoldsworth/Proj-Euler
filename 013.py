import numpy as np

bignumbers=np.genfromtxt('13.csv', delimiter=",")

digits=np.sum(bignumbers, axis=0)
print(digits)
