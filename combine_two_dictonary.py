# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}

    
# dict1={"mercy":"kind & dayalu","good":"Acha","churn":"Mathana"}
# print(dict1.keys())
# s=input("Enter the word from the dictionary whose meaning you want: ")
# print(dict1[s])

# print("Welcome to Dictionary")
# Dictionary={"abase":" cause to feel shame", "benefit":"advantage", "callow":"young and inexperienced", "dally":"waste time", "endear":"make attractive"}
# print("The required meaning is:")
# Search=input("enter word")
# print(Dictionary[Search])
# print("Thanks for using Dictionary")
# print("\U0001F618")




# a=input("enter :")
# b=a[-1::-1]
# if (a==b):
#     print("pali")
# else:


# Q1.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for i, j in d1.items():
    for x, y in d2.items():
        if i == x:
            d3[i]=(j+y)
print(d3)






