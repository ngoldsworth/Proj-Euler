def checkp(num: int):
    diglst = list(str(num))
    backlst = diglst[::-1]
    if backlst == diglst:
        return True
    else:
        return False

if __name__ == "__main__":
    tot = 0
    for j in range(10**6):
        if checkp(j):
            binj = list(bin(j))
            del binj[0:2]
            if binj == binj[::-1]:
                tot = tot + j

    print(tot)
