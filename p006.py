
if __name__ == '__main__':
    n = 100

    sum_of_n = n*(n+1) // 3
    square_of_sum = sum_of_n ** 2

    sum_of_squares = n*(n+1)*(2*n+1) // 6

    ans = square_of_sum - sum_of_squares

    print(ans)
