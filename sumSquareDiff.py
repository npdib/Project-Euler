num = 100
sumSquare = 0
squareSum = 0


for i in range(1,num+1):
    sumSquare += i*i
    squareSum += i

squareSum *= squareSum

print(squareSum-sumSquare)
