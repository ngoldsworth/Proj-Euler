import re

def sum_of_digits(num):
    new = re.sub(r"(\d)" , "\g<1>," , str(num))
    listn = new.split(",")
    print(listn)
    results = list(map(int, listn))
    print(results)

sum_of_digits(10)
