class My:
    x=10
    def __init__(self):
        self.x=20


My.x = 0
My.y = 0

c1 = My()
c2 = My()

print("c1.y=", c1.y, "\n","c1.x= ", c1.x)
print("c2.y=", c2.y, "\n","c2.x= ", c2.x)
print("My.x= ",My.x,"My.y= ",My.y)



print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


#print("c1.y=", c1.y)
#print("c2.y=", c2.y)
c1.x=11
c1.y=21

print("c1.y=", c1.y, "\n","c1.x= ", c1.x)
print("c2.y=", c2.y, "\n","c2.x= ", c2.x)
print("My.x= ",My.x,"My.y= ",My.y)