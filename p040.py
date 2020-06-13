def split(word: str):
    return [char for char in word]

def champernowne(n: int):
    champstring = '0'
    for j in range(1,n):
        champstring = champstring + str(j)
    return champstring

if __name__ =='__main__':
    aggh = champernowne(1000000)
    aggh_list = split(aggh)
    prod = 1
    for j in range(7):
        prod = int(aggh_list[10**j]) * prod
    print(prod)
