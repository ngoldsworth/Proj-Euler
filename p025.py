kdigits = False

def nextfib(index: int, a: int, b: int):
    """

    :param a:
    :param b:
    :return: current index of highest number, highest number and next highest number in sequence
    """
    if index == 0 or index == 1:
        a = 1
        b = 1
        index = 2

    index = index + 1
    newupper = a + b
    newlower = max(a, b)
    return index, newupper, newlower

def fib_dig_test(index: int, upper: int, digits: int):
    if len(str(upper)) >= digits:
        print(upper)
        return True
    else:
        return False


i, u, l = nextfib(0, 1, 1 )

while kdigits == False:
    kdigits = fib_dig_test(i, u, 1000)
    i, u, l = nextfib(i, u, l)
