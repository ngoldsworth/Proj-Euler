# This solution works, but is way too slow
from itertools import combinations_with_replacement as combi
from math import factorial as f

coins = [1, 2, 5, 10, 20, 50, 100, 200]

# count = 0
# for num in range(201):
#     coin_combos = combi(coins, num)
#     print('Currently on ' + str(num))
#     for tup in coin_combos:
#         if sum(tup) == 200:
#             count = count + 1
#
# print(count)

def nCr(n, r):
    if n < r:
        return 0
    else:
        denom = f(r) * f(n - r)
        ans = f(n) // denom
        return ans

sum = 0
for n in range(201):
    sum = sum + 5**n

print(len(list(str(sum))))
