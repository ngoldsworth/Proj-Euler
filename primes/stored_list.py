import numpy as np
from primelist import PrimesList

if __name__ == '__main__':
    z = PrimesList(10**10).list
    print(z)
    np.save('savedlist', z)
