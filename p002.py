# This block is a definition for functionalizing my process
def fiblist(n):
    '''
    Generates list of the first n fibonacci numbners, starting with f0 = 0
    '''
    fib = [0,1]
    for j in range(n-1):
        fib.append(fib[-1] + fib[-2])
    return fib


# the main sequence
if __name__ == "__main__":

    # This first block is my first attempt
    fib = [1,1]
    x = 1
    while x < (4 * 10**6)+1:
        f1=fib[-1]
        f2=fib[-2]
        x = f1 + f2
        fib.append(x)
    SUM = sum(num for num in fib if num % 2 != 0)
    print(SUM)



