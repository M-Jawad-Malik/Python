# Here a function for checking a number either it is odd or even is defied#
def even_odd(number):
    if number%2==0:
        return True
    else:
        return False
# _________________________________#
# Here main function is defined#
def main():
    number=[1,2,3,4,5,6,7]
    for i in number:
        if even_odd(i):
            print(i,' is even number.')
        else:
            print(i,' is odd number')
#__________________________________#
# here main function is called#
main()
#_____________________________#