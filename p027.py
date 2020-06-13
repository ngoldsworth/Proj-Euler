from primes.primelist import primesfrom2to

# DETERMINE MAXIMUM POSSIBLE PRIME
# Largest prime will be less than (1000)^2 + (1000)(1000) + (1000),
# as that is not prime
endpoint = 1000** 2 + (1000 * 1000) + 1000

plist = list(primesfrom2to(endpoint))
b_list = list(primesfrom2to(1001))
n1_list = list(primesfrom2to(2004))


combos = []
print(len(b_list))
print(len(plist))
for b in b_list:
    for a in range(-1*b, 1001):
        if a+b+1 in n1_list:
            # print('Got one!')
            combos.append((a, b))

# n = 0
# while len(combos) >= 100:
#     for tup in combos:
#         if n**2 + tup[0]*n + tup[1]<=0:
#             j = combos.index(tup)
#             del combos[j]
#     n = n + 1
#     if n > 1000:
#         break

for n in range(1001):
    max_poss_prime = n ** 2 + 1001 * n + 1001
    nprmlst = [k for k in plist if k <= max_poss_prime]
    for tup in combos:
        if n**2 + tup[0]*n + tup[1] not in nprmlst:
            j2 = combos.index(tup)
            del combos[j2]
    print(n)
    if len(combos) <= 2:
        break

print(combos)

for tup in combos:
    cont = True
    n = 0
    a = tup[0]
    b = tup[1]
    while cont:
        if n**2 + a*n + b in plist:
            n = n + 1
        else:
            cont = False
            print(n, a*b)



