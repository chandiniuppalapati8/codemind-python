import math
def area(a,b,c):
    s=(a+b+c)/2
    ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("%.2f"%ar)
a,b,c=map(int,input().split())
area(a,b,c)