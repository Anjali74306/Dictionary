a={'sonu':85, 'Kartik':90,'Deepak':96,'Aman':76,'Somesh':60,'Umesh':85,'Amarpal':70,'Roshan':57,'Riyaz':98,'Shabid':56}
n=int(input("enter the number"))
for i in range(n):
    key=input("enter the key")
    values=input("enter the values")
    a.update({key.value})
print(a)
