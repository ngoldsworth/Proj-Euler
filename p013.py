import numpy as np

bignumbers=np.genfromtxt('13.csv', delimiter=",")

digits=np.sum(bignumbers, axis=0)

print(digits)
print(np.size(digits))
tot=0

for j in  range(np.size(digits)):
    n=np.size(digits)-j-1
    val=digits[np.size(digits)-j-1]
    num=digits[j]*(10**n)
    tot=tot+num



#This is not working...
first_ten=int(str(tot)[:10])

print(first_ten)
