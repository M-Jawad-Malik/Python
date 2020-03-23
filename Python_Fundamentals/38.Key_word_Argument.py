# keyword argument allows to change position of parameters when a function is called#
def greet(name,msg):
    print('Hello '+name,msg)
#in function defintion name was at first place but keyword argument allows me to change it's position in call#
greet(msg='how are you?',name='chao')
