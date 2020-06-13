import numpy as np

def collatz(n):
    '''

    :param n: first number of Collatz
    :return: the next integer in a Collatz sequence that starts with `n`
    '''
    if n % 2 == 0:
        return int(n/2)
    elif n == 1:
        return None
    else:
        return int(3*n +1)


def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = collatz(n)
        seq.append(n)

    return seq


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    lengths = []
    for j in range(2, 10**6):
        lengths.append(len(collatz_sequence(j)))

    print(lengths.index(max(lengths)), max(lengths))
    plt.plot(lengths)
    plt.show()

