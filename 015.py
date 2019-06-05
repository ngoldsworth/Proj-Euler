from math import factorial as fact

def number_of_paths(n):
    # number of paths for a square, n x n grid
    totlen = 2*n
    rights = n
    downs = n
    paths = fact(totlen)/(fact(rights) * fact(downs))
    return int(paths)

print(number_of_paths(2))
print(number_of_paths(20))

