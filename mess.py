def fiblike(j0, j1, m):
    numlst = [j0, j1]
    for i in range(m):
        numlst.append(numlst[-1] + numlst[-2])
        # print(numlst[-1])
    return numlst

def alt_fib(j0, j1, m):
    numlst = [j0, j1]
    for i in range(m):
        k0 = numlst[-2]
        k1 = numlst[-1]
        if numlst[-1] % 2 == 0:
            numlst.append(k0 * k1 /(k0 + k1) )
        else:
            numlst.append(k0*k1/abs(k0 - k1))

    return numlst



if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    nums = alt_fib(9, 10, 100)
    # ratios = np.array([nums[j+1]/nums[j] for j in range( len(nums) -1)])

    indi = []
    for j, num in enumerate(nums):
        indi.append(j)

    plt.plot(indi, nums)
    plt.show()
