def sum_of_digits(num):
    new = re.sub(r"(\d)(?=\d)" , "\g<1>," , str(num))
    listn = new.split(",")
    results = list(map(int, listn))
    total=sum(results)
    return total

def factorial(j: int):
    prod = 1
    for num in range(1 , int(j)):
        prod = prod*int(num)

n = factorial(100)
print(n)
print(sum_of_digits(factorial(n)))
