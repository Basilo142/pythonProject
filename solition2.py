import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d1=int(((-1*b)+(((b*b)-(4*a*c))**0.5))/(2*a))
d2=int(((-1*b)-(((b*b)-(4*a*c))**0.5))/(2*a))
print(d1)
print(d2)