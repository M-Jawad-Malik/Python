x=eval(input('Enter Seconds: '))
c,y=x%60,x//60
b,a=y%60,y//60
print('Time in Format: ',a,':',b,':',c)