import math

x = 1000

d3 = int(math.floor(x/3))
d5 = int(math.floor(x/5))

three_sum = int(3*d3*(d3+1)*0.5)
five_sum = int(5*d5(d5+1)*0.5)

final_sum = three_sum + five_sum
