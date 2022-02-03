# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
dict={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
for i in dict:
    if dict[i]==dict[i]:
        print("yes")
    else:
        print("no")