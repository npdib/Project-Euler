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

def countFactors(factors):
    diffFactors = []
    numOfFacts = 1
    
    for f in factors:
        if diffFactors.count(f) == 0:
            diffFactors.append(f)

    for d in diffFactors:
        numOfFacts *= (factors.count(d) + 1)

    return numOfFacts


num = 500
triangleNum = 1
counter = 1
factors = 0
while factors < num:
    triangleNum += counter + 1
    counter += 1

    factors = countFactors(primeFact(triangleNum))

print(triangleNum)
