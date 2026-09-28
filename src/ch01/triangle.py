import math
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
h=(a+b+c)/2
s=math.sqrt(h*(h-a)*(h-b)*(h-c))
print(s)