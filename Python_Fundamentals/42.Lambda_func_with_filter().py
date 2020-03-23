# filter function get a fucntion and a list is as argument and return another list of elements accirding to function#
list=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x: x%2==0,list)
for i in even:
    print('Even numbers are',i)