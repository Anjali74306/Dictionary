# Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
user=input("enter key:")
if user=="id":
    sum=0
    for i in range(len(student)):
        for j in student[i]:
            if type(student[i][j])==int:
                sum=sum+student[i][j]
print(sum)
