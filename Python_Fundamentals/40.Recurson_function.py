# a function taht calls it self again anfd again is called recursion function#
def fact(x):
    if x == 1:
        return 1
    else:
        return (x*fact(x-1))

x = eval(input('Enter number'))
x = fact(x)
print('factorial of entered number is : ',x)