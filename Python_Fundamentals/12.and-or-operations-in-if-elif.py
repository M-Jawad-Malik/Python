# program for checkinng whether number is greater than 0 and less than 10 or less than 0 or greater tahn 10 #
x=eval(input('Enter Number: '))
if x>0 and x<10: # two conditions with 'and' keyword #
    print('Number is greater than zero and less than 10')
elif x>10:
    print('Number is greater than 10')
else:
    print('Less than 0')