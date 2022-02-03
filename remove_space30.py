# Write a Python program to remove spaces from dictionary keys.
# Original_dictionary:{'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}
dictionary={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
a={}
for x,y in dictionary.items():
    name={x.replace(" ",""):y}
    a.update(name)
print(a)








   
        