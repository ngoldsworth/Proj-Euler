
# Make function to determine factors of a number
def factors_list(num):
    factors = [1]  #initalize list, 1 is always a factor 
    for i in range(2, num+1):
        if num % i == 0:
            factors.append(i)
    return(factors)

def countfactors(num):
    # returns number of whole-number factors for num
    count=0
    for i in range(1, num+1):
        if num % i == 0:
            count = count+1
    return(count)

def triangularnumber(j):
    # returns the jth triangular number
    sum=0
    for i in range(0,j+1):
        sum=sum+i
    return(sum)


count = 1
j=2
while count<=500:
    count=countfactors(triangularnumber(j))
    print(j, triangularnumber(j) , count)
    j=j+1

