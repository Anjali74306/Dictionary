'# .Write a Python program to convert a given dictionary into a list of lists. 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
l=[]
for x in a.items():
    l.append([x])
print(l)

