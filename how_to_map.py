# Q16.Write a Python program to map two lists into a dictionary.
students = ['Smith', 'John', 'Priska', 'Abhi']
marks = [89, 53, 92, 86]
students_dict = dict(zip(students, marks))
print(students_dict)-


# dic=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d={}
# for i in dic:
#     if i[0] not in dic.keys():
#         d.update({i[0]:[i[1]]})
#     elif i[0]  in dic.keys():
#         d[i[0]].append(i[1])
# print(d)
