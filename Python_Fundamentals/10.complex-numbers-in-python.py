from math import sqrt
x=complex(input('Enter complex numbers: '))
a=x.real
b=x.imag
c=sqrt(a**2+b**2) # magnitude of compex number using formula sqrt(real^2+imag^2)
print('Magnitude of ',x,'is','{:f}'.format(c))

c=abs(x) # abs() function is also used for finding magnitude of complex numbers #
print('Magnitude of ',x,'is','{:f}'.format(c))