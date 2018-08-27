# PROBLEM STATEMENT:
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#
#Find the sum of all primes below two million


def is_prime(n):
    for j in range(2, n):
        if n % 2 == 0 or n % j == 0:  # aritmetic calculations
            return False
        else:
            return True

prime_list = [2]
for i in range(1,1000000):
    q = (2*i) - 1 
    if is_prime(q):
        prime_list.append(q)
        print(q)

print(prime_list)
sum_of_primes=sum(prime_list)
print(sum_of_primes)
