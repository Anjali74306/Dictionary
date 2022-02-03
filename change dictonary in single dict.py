dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# i=0
# while i<dic1:
# print(dic1+dic2+dic3)

dic1.update(dic2)
dic1.update(dic3)
print(dic1)