def summa(a,b,c):
    return a+b+c
d1={'a':1, 'b':2, 'c':3}
#print(summa(**d1))
def fun(a,b):
    a[0], b['a']='str', 200
    return a
x=[1,2,3]
y={'a':1,'b':2}
#print('До функции', x, y)
fun(x,y)
#print('После', x, y)
def funns(a,b):
    a=a[:]
    b=b.copy()
    a[0], b['a'] = 'str', 200
    return a

x=[1,2,3]
y={'a':1,'b':2}

#print('До функции-ss', x, y)
funns(x, y)
#print('После-ss', x, y)
#print("=====",funns(x,y))

def suuum(*s):
    fes=0
    for i in s:
        fes+=int(i)
    return fes
print(suuum(4,5,4,5454,54545,45,4545,545,45,4,54,5,45,45,454545,45345234,23452345,23452345,23452345,23452345,23452345,2345,'23323232'))

def combo(*t,**s):
    for i in t:
        print(i, end=' ')
    for i in s:
        print('{0} => {1}'.format(i, s[i]), end=' ')
combo(234342,2342342,234,5,4,3333,r=3,d=5,erere=45454,dfdfdf=2)
