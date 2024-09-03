import math
a = 12
b = 13
c = 14
d = b*b-(4*a*c)
if(d==0):
    r1 = -b/(2*a)
    r2 = -b/(2*a)
elif(d>0):
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b + math.sqrt(d))/(2*a)
else:
    x = -b / (2*a)
    y = math.sqrt(-d)/(2*a)
    r1 = complex(x,y)
    y = y*(-1)
    r2 = complex(x,y)
print("ROOT 1 : ",r1," , ROOT 2 : ",r2)