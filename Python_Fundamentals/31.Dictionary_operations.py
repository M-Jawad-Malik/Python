# following are some operations that can be applied on dictionary#
dic={'name': 'toddler','age': 20,'Gender': 'Male'}
print('Dictionary dic : ',dic)
# adding element#
dic['color']='smokewhite'
print('Dictionary dic after addition of element : ',dic)
# updating element#
dic['color']='Black'
print('Dictionary dic after updation of element : ',dic)
# removing element#
del dic['color']
print('Dictionary dic after deletion of element : ',dic)
# removing whole dictionary#
del dic
print(dic)