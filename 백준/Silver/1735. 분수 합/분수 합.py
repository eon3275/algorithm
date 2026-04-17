from math import gcd
a, b = map(int, input().split())
c, d =map(int, input().split())
mo = a*d + b*c
de = b*d
g = gcd(de, mo)
print(mo//g, de//g)