import math

for a in range(335,999):
    for b in range(1+math.floor((1000-a)/2),a):
        c = 1000 - a - b
        
        if (b*b + c*c == a*a) and (c>0):
            print(a*b*c)
            
