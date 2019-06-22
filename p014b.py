def collatz(num):
    if num % 2 == 0:
        return int(num/2)
    else:
        return int(3*num + 1)

def collatz_counter(j):
    count=1
    if j == 1:
        return count
    else:
        return count+collatz_counter(collatz(j))

maxlen= (1, 1)
for j in range (1, 1000000):
    newlen=(j, collatz_counter(j))
    if newlen[1] > maxlen[1]:
        maxlen = newlen

print(maxlen)
