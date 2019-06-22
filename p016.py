import re

def sum_of_digits(num):
    new = re.sub(r"(\d)(?=\d)" , "\g<1>," , str(num))
    listn = new.split(",")
    results = list(map(int, listn))
    total=sum(results)
    return total

print(sum_of_digits(2**1000))
