def digital_sum(num: int):
    return sum([int(k) for k in list(str(num))])

if __name__ == '__main__':
    powerslist = []
    for a in range(100):
        for b in range(100):
            powerslist.append(a**b)

    sumslist = [digital_sum(j) for j in powerslist]
    print(max(sumslist))

import numpy as np
np.linalg.solve