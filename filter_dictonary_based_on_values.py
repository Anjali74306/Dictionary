# # Write a Python program to filter a dictionary based on values. 
# # Original Dictionary:
# # {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# # Marks greater than 170:
# # {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
# dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# # c={}
# for i in dic:
#     if dic[i]>170:
#         # c.update(dic[i])
#         # print(c)
#         print(i,dic[i])

dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
c={}
for key , value in dic.items():
    if value>=170:
        c={key:value}
        print(c)