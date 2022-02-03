# .Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
my_dict={2:56,4:3,5:4,8:4,4:56}
max1=[]
for i in  range (3):
    max=0
    for j in my_dict:
        if my_dict[j]>max:
            max=my_dict[j]
            c=j
    max1.append(my_dict[c])
    my_dict.pop(c)
print(max1)




    