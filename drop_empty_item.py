# Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
a={}
for x in dic:
    if dic[x] is None:
        pass
    else:
        a[x]=dic[x]
print(a)
    



