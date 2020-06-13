fib = [1,1]
x = 1
while x < 4000000:
    f1=fib[-1]
    f2=fib[-2]
    x = f1 + f2
    fib.append(x)
SUM = sum(num for num in fib if num % 2 != 0)
print(SUM)
