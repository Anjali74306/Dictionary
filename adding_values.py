# Q1.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for x in d1:
    for j in d2:
        if x==j:
            s=d1[x]+d2[j]
            d[j]=s
        if x not in d2:
                d[x]=d1[x]
        if j not in d:
                d[j]=d2[j]
print(d)

