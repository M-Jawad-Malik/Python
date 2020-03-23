x=eval(input('Enter Length in cm: '))
if x<0:
    print('Invalid input')
else:
    a=x/2.54
    print('Length in inches is: ',int(a))