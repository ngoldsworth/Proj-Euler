import math

x = 1000

dthree = int(math.floor(x/3))
dfive = int(math.floor(x/5))

three_sum = int(3*dthree*(dthree+1)*0.5)
five_sum = int(5*dfive(dfive+1)*0.5)

final_sum = three_sum + five_sum
print final_sum
