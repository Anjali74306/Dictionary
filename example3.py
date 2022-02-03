# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}
# for x in person:
#     print(x,person[x])

person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:{
        'organisation':'navgurukul','place':'dharamsala'
        }
    }
print(person['gender'])
print(person[4])