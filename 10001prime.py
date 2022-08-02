import math

def primeFact(n):

    temp = n
    factors = []
    noFactor = False

    if (n == 2 or n == 3):
        factors.append(int(n))
        return factors    

    while noFactor == False:

        for i in range(2,1+int(math.floor(math.sqrt(n)))):
            

            if (temp % i == 0):
                temp /= i
                factors.append(i)
                break

            if (i == int(math.floor(math.sqrt(n)))):
                noFactor = True
                if (temp != 1):
                    factors.append(int(temp))

    factors = sorted(factors)
    return factors

num = 2000000
primes = [2,3]
loop = True

while (primes[-1] <= num) and loop == True:
    
    counter = primes[-1]+2
    
    while True:
        if (len(primeFact(counter)) == 1):
            print(counter)
            if counter > num:
                loop = False
                break
            primes.append(counter)
            break
        counter += 2


##print(primes)
print(sum(primes))
        
