def next_collatz(n: int):
    '''

    :param n: first number of Collatz
    :return: the next integer in a Collatz sequence that starts with `n`
    '''
    if n % 2 == 0:
        return int(n / 2)
    elif n == 1:
        return 1
    else:
        return int(3 * n + 1)


def initial_collatz_dict(max_n: int):
    d = {}
    for j in range(max_n + 1):
        d[j] = next_collatz(j)

    return d


# def collatz_sequence(
#         num: int,
#         known_sequences: list
# ):
#     if known_sequences[num] is not None:
#         sequence = known_sequences[num]
#     else:
#         sequence = [num]
#         sequence.append()


if __name__ == '__main__':
    largest_number = 10 ** 6
    dic = initial_collatz_dict(largest_number)

    for j in range(largest_number - 5, largest_number + 10):
        try:
            z = dic[j]
            print('Hi')
        except KeyError:
            dic[j] = next_collatz(j)
            print(dic[j])
