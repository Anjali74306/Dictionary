c={}
a=int(input("enter number"))
for i in range(1,1+a):
    c.update({i:i**2})
print(c)
