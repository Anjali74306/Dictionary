# Q46.Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
# Original list:

a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# [print(a)]
# for i in a:
#     for j in i:
#         if i[j].isdigit():
#             num=int(i[j])
#             i[j]=num
# print(a)                                                                                                                                                                                        

for i in a:
    for j in i:
        if type(i[j]) is str:
            num=int(i[j])
            i[j]=num
print(a)                                                                                                                                                                                        

        
