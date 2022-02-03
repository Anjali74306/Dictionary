name={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
short={}
for i in name:
    s=name[i]
    for j in name:
        a=name[j]
        if a<=s:
            short[j]=a
print(short)




