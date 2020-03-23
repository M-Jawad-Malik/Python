def check_EO(no):
    if no%2==0:
        return True
    else:
        return False
def check_od(alpha):
    if alpha%2!=0:
        return True
    else:
        return False
list=[1,2,3,4,5,6,7,8]
filter_even=filter(check_EO,list)
filter_even=tuple(filter_even)
filter_odd=filter(check_od,list)
filter_odd=tuple(filter_odd)
print('Even no are: ')
print(filter_even)
print('odd numbers are: ')
print(filter_odd)
