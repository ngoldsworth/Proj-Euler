def check_pyth(a, b, c):
    if a < b < c:
        if a**2 + b**2 == c**2:
            return True

if __name__ == '__main__':
    for a in range (0, 999):
        for b in range (0, 998):
            c = 1000 - b - a
            if check_pyth(a, b, c):
                print(a, b, c, a*b*c)
