
'''
#ex.1 p.7
h = int(input("Hour: ")) * 60 * 60
m = int(input("Minute: ")) * 60
s = int(input("Second: "))
sum1 = h + m + s
print(sum1)
'''

'''
#ex.2 p.7
import math
x = int(input("x: "))
y = 2 - x + (3/7)*(x**2) - (5/11)*(x**3) + math.log(x, 10)
print(y)
'''

'''
#ex.3 p.8
a = int(input("a: "))
x = 1
x = (x + a/x)/2
x = (x + a/x)/2
x = (x + a/x)/2
x = (x + a/x)/2
print(x)
'''

'''
#ex.4 p.9
v1, v2, v3 = [float(e) \
              for e in input().split()]
u1, u2, u3 = [float(e) \
              for e in input().split()]
dotp = v1*u1 + v2*u2 + v3*u3
print(dotp)
'''

'''
#ex.8 p.9
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))
total = (a + b + c + d + e) / 5
print(total)
'''

