numArray = []
a = 0
b = 0
total = 0
totala = 0
totalb = 0

# numArray a and b are used to test the array
# is the right length
numArraya = []
numArrayb = []

while a < 1000:
    numArray.append(a)
    numArraya.append(a)
    a += 3
# This above section will add every third integer to the array.

while b < 1000:
    if b not in numArray:
        numArray.append(b)
        numArrayb.append(b)
    b += 5

for num in numArray:
    total += num
print (total)

