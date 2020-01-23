import math

def func(x):
    if x == 100:
        return -1
    return (5000-100*x)/(100-x)

for a in range(1,998):
    b = func(a)
    if a == 100:
        continue
    if b.is_integer() and b>0:
        c = math.sqrt(a**2+b**2)
        print(a,b,c,a+b+c)
print("done")
