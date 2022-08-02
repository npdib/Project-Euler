import math

num = 20
total = 1


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

for i in range(2,num+1):
    factors = primeFact(i)
    prevF = 1

    temp = total
    if i==16:
        print(total)
    
    print(factors)
    for f in factors:
    

        if (prevF == f) and (temp % f == 0):
            temp /= f
            prevF = f
            continue
        elif (prevF == f and temp % f != 0):
            total *= f
            temp = num
            continue
        else:
            if (total % f == 0):
                temp /= f
                prevF = f
                continue
            else:
                total *= f
                
        prevF = f

print(total)
