fib = [1,1]
x = 1
while x < 4000000:
    f1=fib[-1]
    f2=fib[-2]
    x = f1 + f2
#    print(x)
    fib.append(x)
# if x % 2 != 0 and x <= 4000000:

SUM = sum(num for num in fib if num % 2 != 0)
print(SUM)
