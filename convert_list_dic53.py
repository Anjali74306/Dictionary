# Write a Python program to convert a given list of lists to a dictionary. 
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['
# b=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# d={}
# for i in range(len(b)):
#     c=[]
#     for j in range(1,len(b[i])):
#         c.append(b[i][j])
#         d.update({b[i][0]:c})
# print(d)

a=[1,2,3,4,5,6,]
a={}
for i in range(len(a)):
    for j in a[i]+len(a):
print(a[i],":",len(a))



